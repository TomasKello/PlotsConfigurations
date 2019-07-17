#include "LatinoAnalysis/MultiDraw/interface/TTreeFunction.h"
#include "LatinoAnalysis/MultiDraw/interface/FunctionLibrary.h"

#include "TVector2.h"

#include <string>
#include <unordered_map>
#include <iostream>
#include <tuple>
#include <array>

class ReCleanJet : public multidraw::TTreeFunction {
public:
  ReCleanJet(char const* bname);
  ~ReCleanJet();

  char const* getName() const override { return "ReCleanJet"; }
  TTreeFunction* clone() const override { return new ReCleanJet(bname_.c_str()); }

  int getMultiplicity() override { return 1; }
  unsigned getNdata() override;
  double evaluate(unsigned) override;

protected:
  void bindTree_(multidraw::FunctionLibrary&) override;

  std::string bname_{};

  enum ReturnType {
    kPt,
    kEta,
    kJetIdx,
    nReturnTypes
  };

  // this is horrible
  static std::tuple<UInt_t, UInt_t, ULong64_t> currentEvent;
  static UIntValueReader* nJet;
  static FloatArrayReader* Jet_pt;
  static FloatArrayReader* Jet_eta;
  static FloatArrayReader* Jet_phi;
  static IntArrayReader* Jet_jetId;
  static IntArrayReader* Jet_puId;
  static UIntValueReader* nLepton;
  static FloatArrayReader* Lepton_pt;
  static FloatArrayReader* Lepton_eta;
  static FloatArrayReader* Lepton_phi;

  static void setValues(UInt_t, UInt_t, ULong64_t);

  static std::vector<std::array<double, nReturnTypes>> returnValues;

  ReturnType returnType_{nReturnTypes};
  UIntValueReader* run{};
  UIntValueReader* luminosityBlock{};
  ULong64ValueReader* event{};
};

std::tuple<UInt_t, UInt_t, ULong64_t> ReCleanJet::currentEvent{};
UIntValueReader* ReCleanJet::nJet{};
FloatArrayReader* ReCleanJet::Jet_pt{};
FloatArrayReader* ReCleanJet::Jet_eta{};
FloatArrayReader* ReCleanJet::Jet_phi{};
IntArrayReader* ReCleanJet::Jet_jetId{};
IntArrayReader* ReCleanJet::Jet_puId{};
UIntValueReader* ReCleanJet::nLepton{};
FloatArrayReader* ReCleanJet::Lepton_pt{};
FloatArrayReader* ReCleanJet::Lepton_eta{};
FloatArrayReader* ReCleanJet::Lepton_phi{};
std::vector<std::array<double, ReCleanJet::nReturnTypes>> ReCleanJet::returnValues{};

ReCleanJet::ReCleanJet(char const* bname) :
  TTreeFunction(),
  bname_(bname)
{
  if (bname_ == "pt")
    returnType_ = kPt;
  else if (bname_ == "eta")
    returnType_ = kEta;
  else if (bname_ == "jetIdx")
    returnType_ = kJetIdx;
}

ReCleanJet::~ReCleanJet()
{
}

unsigned
ReCleanJet::getNdata()
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues.size();
}

double
ReCleanJet::evaluate(unsigned iJ)
{
  setValues(*run->Get(), *luminosityBlock->Get(), *event->Get());
  return returnValues[iJ][returnType_];
}

void
ReCleanJet::bindTree_(multidraw::FunctionLibrary& _library)
{
  _library.bindBranch(run, "run");
  _library.bindBranch(luminosityBlock, "luminosityBlock");
  _library.bindBranch(event, "event");

  if (nJet == nullptr) {
    _library.bindBranch(nJet, "nJet");
    _library.bindBranch(Jet_pt, "Jet_pt");
    _library.bindBranch(Jet_eta, "Jet_eta");
    _library.bindBranch(Jet_phi, "Jet_phi");
    _library.bindBranch(Jet_jetId, "Jet_jetId");
    _library.bindBranch(Jet_puId, "Jet_puId");
    _library.bindBranch(nLepton, "nLepton");
    _library.bindBranch(Lepton_pt, "Lepton_pt");
    _library.bindBranch(Lepton_eta, "Lepton_eta");
    _library.bindBranch(Lepton_phi, "Lepton_phi");

    currentEvent = std::make_tuple(0, 0, 0);

    _library.addDestructorCallback([]() {
        nJet = nullptr;
        Jet_pt = nullptr;
        Jet_eta = nullptr;
        Jet_phi = nullptr;
        Jet_jetId = nullptr;
        Jet_puId = nullptr;
        nLepton = nullptr;
        Lepton_pt = nullptr;
        Lepton_eta = nullptr;
        Lepton_phi = nullptr;
      });
  }
}

/*static*/
void
ReCleanJet::setValues(UInt_t _run, UInt_t _luminosityBlock, ULong64_t _event)
{
  if (std::get<0>(currentEvent) == _run && \
      std::get<1>(currentEvent) == _luminosityBlock && \
      std::get<2>(currentEvent) == _event)
    return;

  currentEvent = std::make_tuple(_run, _luminosityBlock, _event);

  returnValues.clear();

  unsigned nL(*nLepton->Get());

  auto matchLepton([nL](double eta, double phi)->bool {
      for (unsigned iL(0); iL != nL; ++iL) {
        if (Lepton_pt->At(iL) < 10.)
          continue;
        double dEta(eta - Lepton_eta->At(iL));
        double dPhi(TVector2::Phi_mpi_pi(phi - Lepton_phi->At(iL)));
        if (dEta * dEta + dPhi * dPhi < 0.09)
          return true;
      }
      return false;
    });

  unsigned nJ(*nJet->Get());
  returnValues.reserve(nJ);

  for (unsigned iJ(0); iJ != nJ; ++iJ) {
    if (Jet_jetId->At(iJ) < 2)
      continue;

    double pt(Jet_pt->At(iJ));
    if (pt < 15.)
      continue;

    double eta(Jet_eta->At(iJ));
    
    double absEta(std::abs(eta));

    if (absEta > 4.7)
      continue;

    if (pt < 50. && (Jet_puId->At(iJ) & (1 << 2)) == 0)
      continue;

    double phi(Jet_phi->At(iJ));

    if (matchLepton(eta, phi))
      continue;

    returnValues.resize(returnValues.size() + 1);
    returnValues.back()[0] = pt;
    returnValues.back()[1] = eta;
    returnValues.back()[2] = iJ;
  }
}
