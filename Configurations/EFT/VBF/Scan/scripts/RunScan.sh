
# input : H0M, H0PH, H0L1

combineCards.py \
hww2l2v_13TeV_SRVBF=../Full2016/datacards/hww2l2v_13TeV_SRVBF/KD_$1/datacard.txt \
hww2l2v_13TeV_SRVH=../Full2016/datacards/hww2l2v_13TeV_SRVH/KD_$1/datacard.txt \
> cards/$1.txt

text2workspace.py cards/$1.txt -o cards/$1.root -P HiggsAnalysis.CombinedLimit.HWWCouplings:HWWCouplings --PO $1 > cards/scale.txt

combine -d cards/$1.root -n $1 -M MultiDimFit -t -1 -m 125 --algo grid --points 1000 --setParameters muV=1.0,Fai=0.0 --redefineSignalPOIs=Fai

# Verbosity : -v 7 
# Seed? : -s 1
# --X-rtd OPTIMIZE_BOUNDS=0 --X-rtd TMCSO_AdaptivePseudoAsimov=0 --alignEdges=1
# --setParameterRanges Fai=-0.02,0.02 
# --freezeParameters muV 
# --robustFit=1

rm combine_logger.out
mv higgsCombine$1.MultiDimFit.mH125*.root hists/higgsCombine$1.MultiDimFit.mH125.root

# --redefineSignalPOIs=Fai,muV
# root -l hists/higgsCombine'$1'.MultiDimFit.mH125.root
# limit->Draw("2*deltaNLL:Fai")
# limit->Draw("2*deltaNLL:Fai:muV>>h(40,0,10,40,-1,1)","","prof colz")


