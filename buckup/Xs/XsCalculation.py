#!/usr/bin/env python
# -*-coding:Latin-1 -*

# ==============================================================================
#  Description:
#       Unfolding using for pT(W), mT(W), pT(lepton) and eta(lepton)
#  Author:  ATMANI Hicham
# ==============================================================================
import ROOT
from ROOT import gRandom, TH1, TH1D, cout
from ROOT import TFile
from math import *

import yaml

def GetTheCalibVariation(Charge, Energy):

        CalibSystVariation = []

        for i in range(1, 25):
            CalibSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/ElCalibVar/Merge/mc16_'+str(Energy)+'TeV.varscaleDownbin'+str(i)+'.root'))
          
        for i in range(1, 25):
            CalibSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/ElCalibVar/Merge/mc16_'+str(Energy)+'TeV.varcDownbin'+str(i)+'.root'))
             
        return CalibSystVariation

def GetTheRecoilVariation(Charge, Energy):

        RecoilSystVariation = []

        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varSET_SYSbin1.root'))
        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_SYS_DOWNbin1.root'))
        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))

        for i in range(1, 20):
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))

        for i in range(1, 12):
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

        return RecoilSystVariation

def GetSystematics(CalibVariation, truth_hist, reco_hist, data_hist, lum, Calib):

	Systematic = 0
	Xs         = (data_hist.Integral() / lum)*(truth_hist.Integral()/reco_hist.Integral())
	print(len(CalibVariation))

	for i in range(0, len(CalibVariation)):

	    recoVaried = CalibVariation[i].Get("WminusenuSelection/WpT_Reco_cut7")
	    XsVaried   = (data_hist.Integral() / lum)*(truth_hist.Integral()/recoVaried.Integral())
	    #print((XsVaried - Xs), CalibVariation[i].GetName(), reco_hist.Integral(), recoVaried.Integral())
	    #print( (XsVaried - Xs) )
	    Systematic = Systematic + (XsVaried - Xs)*(XsVaried - Xs)
	if (Calib != 0):
	    print("Calib Variation %f"%(100*sqrt(Systematic)/Xs))
	if (Calib == 0):
	    print("Recoil Variation %f"%(100*sqrt(Systematic)/Xs))
	return Systematic

def GetVariations(InputSyst, Channel, Energy, Variable, Syst, truth_hist, reco_hist, data_hist, lum, Name):

	Variation_1D_down  = []        
	DireName       	   = Channel + "Selection_WeightVariations"
	Input	  	   = TFile( InputSyst )
        directory          = Input.GetDirectory(DireName)

        for key in directory.GetListOfKeys():
            hist = key.ReadObj()
            if ((hist.GetName()).find("sumEt") == -1 and (hist.GetName()).find("coarseHigh") == -1 and (hist.GetName()).find("eta") == -1 and (hist.GetName()).find('_down') != -1 ):
               if ( hist.ClassName() == 'TH1F' and (hist.GetName()).find(Variable) != -1 and (hist.GetName()).find(Syst) != -1 ):
                  #print(hist.GetName())
                  Variation_1D_down.append(hist)

        for i in range(0, len(Variation_1D_down)):
            Variation_1D_down[i].Add(reco_hist)

        Xs      = (data_hist.Integral() / lum)*(truth_hist.Integral()/reco_hist.Integral())
        Syst    = 0
        SystTot = 0

        for i in range(0, len(Variation_1D_down)):
            Syst = (data_hist.Integral() / lum)*(truth_hist.Integral()/Variation_1D_down[i].Integral()) - Xs
            SystTot = SystTot + Syst*Syst
        
        SystTot = 100*sqrt(SystTot)/Xs
        print(Name+" syst: %f "%SystTot)

	return SystTot
	
# ==============================================================================
#                               Read the config file
# ==============================================================================

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# read config file:
print("")
print("************ read config file ************")
print("")
print("Lum              : %s" %cfg['Lum'])
print("Energy           : %s" %cfg['Energy'])
print("Channel          : %s" %cfg['Channel'])
print("Variable         : %s" %cfg['Variable'])
print("Niterations      : %s" %cfg['Niterations'])
print("")

# ********************************************************************
# 			Read the input Files
# ********************************************************************
print("  ")
print("      The unfolding Syst   ")
print("  ")

Wplusenu5          = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Summarize_Wminusenu5.root")
Wplusenu5_idSyst   = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Syst_ElIDSys.root")
Wplusenu5_IsoSyst  = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Syst_ElIsoSys.root")
Wplusenu5_RecoSyst = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Syst_RecoSys.root")
Wplusenu5_TrigSyst = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Syst_TrigSys.root")

Wplusenu5_Recoil   = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Recoil_Syst.root")
Wplusenu5_Calib    = TFile("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/WpT/Calib_Syst.root")

Unfolded_data1     = Wplusenu5.Get("unfolded_data1")
Covariance_Id1     = Wplusenu5_idSyst.Get("ElIDSys_Covariance_Iter1")
Covariance_Iso1    = Wplusenu5_IsoSyst.Get("ElIsoSys_Covariance_Iter1")
Covariance_Reco1   = Wplusenu5_RecoSyst.Get("RecoSys_Covariance_Iter1")
Covariance_Trig1   = Wplusenu5_TrigSyst.Get("TrigSys_Covariance_Iter1")
Covariance_Recoil1 = Wplusenu5_Recoil.Get("Recoil_Covariance_Iter1")
Covariance_Calib1  = Wplusenu5_Calib.Get("Calib_Covariance_Iter1")

SumId     = 0
SumIso    = 0
SumReco   = 0
SumTrig   = 0 
Sumrecoil = 0 
SumCalibr = 0 


for i in range(1, 1 + Unfolded_data1.GetNbinsX()):
    for j in range(1, 1 + Unfolded_data1.GetNbinsX()):
	Sumrecoil = Sumrecoil + Covariance_Recoil1.GetBinContent(i, j)
	SumCalibr = SumCalibr + Covariance_Calib1.GetBinContent(i, j)
	SumId   = SumId   + Covariance_Id1.GetBinContent(i, j)
        SumIso  = SumIso  + Covariance_Iso1.GetBinContent(i, j)
        SumReco = SumReco + Covariance_Reco1.GetBinContent(i, j)
        SumTrig = SumTrig + Covariance_Trig1.GetBinContent(i, j)
	
Id_Syst   = sqrt(SumId)  *100/Unfolded_data1.Integral()
Iso_Syst  = sqrt(SumIso) *100/Unfolded_data1.Integral()
Reco_Syst = sqrt(SumReco)*100/Unfolded_data1.Integral()
Trig_Syst = sqrt(SumTrig)*100/Unfolded_data1.Integral()

Recoi_Syst   = sqrt(Sumrecoil)  *100/Unfolded_data1.Integral()
Calib_Syst   = sqrt(SumCalibr)  *100/Unfolded_data1.Integral()

print("Id   syst: %f "%Id_Syst)
print("Iso  syst: %f "%Iso_Syst)
print("Reco syst: %f "%Reco_Syst)
print("Trig syst: %f "%Trig_Syst)

print("Recoil syst: %f "%Recoi_Syst)
print("Calibr syst: %f "%Calib_Syst)

print("  ")
print("      The direct Syst   ")
print("  ")

truth_hist    = Wplusenu5.Get("truth_hist")
reco_hist     = Wplusenu5.Get("reco_hist")
data_hist     = Wplusenu5.Get("data_hist")

Id_Variations    = GetVariations(cfg['Wminusenu5_IdSF'],   cfg['Channel'], cfg['Energy'], cfg['Variable'], "ElIDSys",  truth_hist, reco_hist, data_hist, 256.827, "Id")
Iso_Variations   = GetVariations(cfg['Wminusenu5_IsoSF'],  cfg['Channel'], cfg['Energy'], cfg['Variable'], "ElIsoSys", truth_hist, reco_hist, data_hist, 256.827, "Iso")
Reco_Variations  = GetVariations(cfg['Wminusenu5_recoSF'], cfg['Channel'], cfg['Energy'], cfg['Variable'], "RecoSys",  truth_hist, reco_hist, data_hist, 256.827, "reco")
Trig_Variations  = GetVariations(cfg['Wminusenu5_TrigSF'], cfg['Channel'], cfg['Energy'], cfg['Variable'], "TrigSys",  truth_hist, reco_hist, data_hist, 256.827, "Trig")

CalibVariation   = GetTheCalibVariation(cfg['Charge'], cfg['Energy'])
GetSystematics(CalibVariation, truth_hist, reco_hist, data_hist, 256.827, 1)

RecoilVariation  = GetTheRecoilVariation(cfg['Charge'], cfg['Energy'])
GetSystematics(RecoilVariation, truth_hist, reco_hist, data_hist, 256.827, 0)















