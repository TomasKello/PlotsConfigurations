# nuisances
# name of samples here must match keys in samples.py    

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []

#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WZ', 'Zg'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WZ', 'Zg'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WZ', 'Zg'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WZ', 'Zg'])
}

#### Theoretical Systematics

# Scale
from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()

nuisances['QCDscale_VH']  = {
  'name'  : 'QCDscale_VH',
  'samples'  : {
    'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
    'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
  },
  'type'  : 'lnN',
}

variations = ['LHEScaleWeight[%d]' % i for i in [0, 1, 3, 5, 7, 8]]
nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'Zg': variations,
        'WZ': variations,
        'ZZ': variations
    }
}

#TODO update?
nuisances['QCDscale_qqbar_ACCEPT']  = {
  'name'  : 'QCDscale_qqbar_ACCEPT', 
  'type'  : 'lnN',
  'samples'  : {
    'WH_htt'  : '1.05',
    'ZH_htt'  : '1.04',
  },
}

nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'WH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   },
              }

#TODO update?
nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'WH_htt'  : '1.007',
                   'ZH_htt'  : '1.012',
                   },
              }

#TODO update?
nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'WZ'      : '1.005',
                   'ZZ'      : '1.005',
                   },
              }

#TODO update with measurement from PSweights
nuisances['PS_whss']  = {
                'name'  : 'PS_whss',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : {
                   'WH_htt'   : '1.037',
                },
}

nuisances['UE_whss']  = {
                'name'  : 'UE_whss',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : {
                   'WH_htt'   : '1.010',
               },
}

nuisances['WZ3l2jnorm']  = {
               'name'  : 'CMS_hww_WZ3l2jnorm',
               'samples'  : {
                   'WZ'       : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : ['zh3l_Zg_CR_2j',
                          'zh3l_WZ_CR_2j',
                          'zh3l_SR_ptv_lt150_2j',
                          'zh3l_SR_ptv_gt150_2j']
              }

nuisances['WZ3l1jnorm']  = {
               'name'  : 'CMS_hww_WZ3l1jnorm',
               'samples'  : {
                   'WZ'       : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : ['zh3l_Zg_CR_1j',
                          'zh3l_WZ_CR_1j',
                          'zh3l_SR_ptv_lt150_1j',
                          'zh3l_SR_ptv_gt150_1j']
              }

nuisances['Zg3l2jnorm']  = {
               'name'  : 'CMS_hww_Zg3l2jnorm',
               'samples'  : {
                   'Zg'       : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : ['zh3l_Zg_CR_2j',
                          'zh3l_WZ_CR_2j',
                          'zh3l_SR_ptv_lt150_2j',
                          'zh3l_SR_ptv_gt150_2j']
              }

nuisances['Zg3l1jnorm']  = {
               'name'  : 'CMS_hww_Zg3l1jnorm',
               'samples'  : {
                   'Zg'       : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : ['zh3l_Zg_CR_1j',
                          'zh3l_WZ_CR_1j',
                          'zh3l_SR_ptv_lt150_1j',
                          'zh3l_SR_ptv_gt150_1j']
              }

#### FAKES

fakeW_EleUp       = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_EleDown     = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lElDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_MuUp        = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuUp       / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_MuDown      = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lMuDown     / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_statEleUp   = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_statEleDown = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatElDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_statMuUp    = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuUp   / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'
fakeW_statMuDown  = '( fakeW_ele_'+eleWP+'_mu_'+muWP+'_3lstatMuDown / fakeW_ele_'+eleWP+'_mu_'+muWP+'_3l )'

nuisances['fake_syst_e']  = {
               'name'  : 'CMS_fake_syst_e',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_e' : '1.30',
                             },
}

nuisances['fake_syst_m']  = {
               'name'  : 'CMS_fake_syst_m',
               'type'  : 'lnN',
               'samples'  : {
                             'Fake_m' : '1.30',
                             },
}

nuisances['fake_ele']  = {
                'name'  : 'CMS_fake_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_EleUp , fakeW_EleDown ],
                             },
}

nuisances['fake_ele_stat']  = {
                'name'  : 'CMS_fake_stat_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'      : [ fakeW_statEleUp , fakeW_statEleDown ],
                             },
}

nuisances['fake_mu']  = {
                'name'  : 'CMS_fake_m_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_MuUp , fakeW_MuDown ],
                             },
}

nuisances['fake_mu_stat']  = {
                'name'  : 'CMS_fake_stat_m_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                              'Fake'     : [ fakeW_statMuUp , fakeW_statMuDown ],
                             },
}

###### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

#### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_3l_u)/(TriggerEffWeight_3l))*(TriggerEffWeight_3l>0.02) + (TriggerEffWeight_3l<=0.02)', '(TriggerEffWeight_3l_d)/(TriggerEffWeight_3l)']

nuisances['trigg']  = {
                'name'  : 'CMS_eff_hwwtrigger_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, trig_syst) for skey in mc),
}

##### Electron Efficiency and energy scale

id_syst_ele = [ 'LepSF3l__ele_'+eleWP+'__Up' , 'LepSF3l__ele_'+eleWP+'__Do' ]

nuisances['eff_e']  = {
                'name'  : 'CMS_eff_e_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_ele) for skey in mc),
}

nuisances['electronpt']  = {
                'name'  : 'CMS_scale_e_2018',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : dict((skey, ['1', '1']) for skey in mc),
                'folderUp'   : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__ElepTup', 
                'folderDown' : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__ElepTdo', 
}

###### Muon Efficiency and energy scale

id_syst_mu = [ 'LepSF3l__mu_'+muWP+'__Up' , 'LepSF3l__mu_'+muWP+'__Do' ]

nuisances['eff_m']  = {
                'name'  : 'CMS_eff_m_2018',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, id_syst_mu) for skey in mc),
}

nuisances['muonpt']  = {
                'name'  : 'CMS_scale_m_2018',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : dict((skey, ['1', '1']) for skey in mc),
                'folderUp'   : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__MupTup',
                'folderDown' : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__MupTdo',
}

# ###### Jet energy scale

nuisances['jes']  = {
                'name'  : 'CMS_scale_j_2018',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : dict((skey, ['1', '1']) for skey in mc),
                'folderUp'   : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__JESup',
                'folderDown' : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__JESdo',
}


##### MET energy scale

nuisances['met']  = {
                'name'  : 'CMS_scale_met_2018',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : dict((skey, ['1', '1']) for skey in mc),
                'folderUp'   : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__METup',
                'folderDown' : treeBaseDir+'Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5__MCCorr2018v5__l2loose__l2tightOR2018v5__METdo',
}

# Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }

for n in nuisances.values():
    n['skipCMS'] = 1
