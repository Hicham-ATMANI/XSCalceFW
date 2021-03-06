#!/usr/bin/env python
# -*-coding:Latin-1 -*

# ==============================================================================
#  Description:
#       Unfolding using for pT(W), mT(W), pT(lepton) and eta(lepton)
#  Author:  ATMANI Hicham
# ==============================================================================

from ROOT import TFile, TH1F, TH2F, TCanvas, TPad, TLegend, gStyle, gROOT, gPad, gDirectory, TVector2, TPaveStats, TStyle, TLatex
from ROOT import TColor, kBlack, kRed, kBlue, kMagenta, kYellow, kCyan, kGreen, kOrange, kTeal, kPink, kGray
from ROOT import TArrayD, TAxis, TMath, TVectorF, TMatrixF
from ROOT import kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from root_numpy import *
from source.source import *
from source.Migration import *

import yaml

# ==============================================================================
#  				Read the config file
# ==============================================================================

with open("config_2d.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# read config file:
print("")
print("************ read config file ************")
print("")
print("Lum    		: %s" %cfg['Lum'])
print("Energy  		: %s" %cfg['Energy'])
print("Channel 		: %s" %cfg['Channel'])
print("Variable   	: %s" %cfg['Variable'])
print("Niterations     	: %s" %cfg['Niterations'])
print("")

# read the Input files:
if( cfg['Channel'] == "Wminusenu" and cfg['Energy'] == 5):
	fInput_MC    = TFile( cfg['Wminusenu5_MC'] );       fInput_Data  = TFile( cfg['Wminusenu5_data'] );    fInput_Data_BS  = TFile( cfg['Wminusenu5_BSdata']);   Input_Bkgd1  = TFile( cfg['Wminusenu5_Bkgd1'] );
	Input_Bkgd2  = TFile( cfg['Wminusenu5_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wminusenu5_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wminusenu5_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wminusenu5_Bkgd5'] );
	Input_SFid   = TFile( cfg['Wminusenu5_IdSF'] );     Input_SFiso  = TFile( cfg['Wminusenu5_IsoSF'] );   Input_SFreco    = TFile( cfg['Wminusenu5_recoSF'] );  Input_SFTrig = TFile( cfg['Wminusenu5_TrigSF'] ); 

if( cfg['Channel'] == "Wplusenu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wplusenu5_MC'] );        fInput_Data  = TFile( cfg['Wplusenu5_data'] );     fInput_Data_BS  = TFile( cfg['Wplusenu5_BSdata']);   Input_Bkgd1  = TFile( cfg['Wplusenu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusenu5_Bkgd2'] );     Input_Bkgd3  = TFile( cfg['Wplusenu5_Bkgd3'] );    Input_Bkgd4     = TFile( cfg['Wplusenu5_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wplusenu5_Bkgd5'] );
        Input_SFid   = TFile( cfg['Wplusenu5_IdSF'] );      Input_SFiso  = TFile( cfg['Wplusenu5_IsoSF'] );    Input_SFreco    = TFile( cfg['Wplusenu5_recoSF'] );  Input_SFTrig = TFile( cfg['Wplusenu5_TrigSF'] );

if( cfg['Channel'] == "Wminusmunu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wminusmunu5_MC'] );      fInput_Data  = TFile( cfg['Wminusmunu5_data'] );   fInput_Data_BS  = TFile( cfg['Wminusmunu5_BSdata']); Input_Bkgd1  = TFile( cfg['Wminusmunu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wminusmunu5_Bkgd2'] );   Input_Bkgd3  = TFile( cfg['Wminusmunu5_Bkgd3'] );  Input_Bkgd4     = TFile( cfg['Wminusmunu5_Bkgd4']);  Input_Bkgd5  = TFile( cfg['Wminusmunu5_Bkgd5'] );
        Input_SFiso  = TFile( cfg['Wminusmunu5_IsoSF'] );   Input_SFreco = TFile( cfg['Wminusmunu5_recoSF'] );  Input_SFTrig   = TFile( cfg['Wminusmunu5_TrigSF'] );

if( cfg['Channel'] == "Wplusmunu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wplusmunu5_MC'] );       fInput_Data  = TFile( cfg['Wplusmunu5_data'] );    fInput_Data_BS  = TFile( cfg['Wplusmunu5_BSdata']);  Input_Bkgd1  = TFile( cfg['Wplusmunu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusmunu5_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wplusmunu5_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wplusmunu5_Bkgd4']);   Input_Bkgd5  = TFile( cfg['Wplusmunu5_Bkgd5'] );
        Input_SFiso  = TFile( cfg['Wplusmunu5_IsoSF'] );    Input_SFreco = TFile( cfg['Wplusmunu5_recoSF'] );  Input_SFTrig    = TFile( cfg['Wplusmunu5_TrigSF'] );


# Get The Migration Matrix
MigrationMatrixs = GetTheMigrationMatrix(fInput_MC)

# calculate the Total Background
Background_Total = SumBackground( Input_Bkgd1, Input_Bkgd2, Input_Bkgd3, Input_Bkgd5, Input_Bkgd4, cfg['Channel'], cfg['Variable'])

# read the migration Matrix: 
mig_hist   = MigrationMatrix2d(MigrationMatrixs)

# read the truth histograms:: 
truth_hist = TruthDistribution2d( fInput_MC)

# Get data distribution
data_hist  = DataDistribution2d( fInput_Data) 
reco_hist  = DataDistribution2d( fInput_MC)

Acceptance_hist = GetAcceptance(mig_hist, truth_hist)
Efficiency_hist = GetEfficieny(mig_hist, reco_hist)

dataCorrected = CorrectData( data_hist, reco_hist, Background_Total, Efficiency_hist)
responseM = RooUnfoldResponse(0,0,mig_hist,"UNFOLD","UNFOLD");

unfolded_data   = []
Covarinace_data = []
for i in range(1, 1+cfg['Niterations']):
    unfoldDATA = RooUnfoldBayes (responseM, dataCorrected, i)
    unfolded_data.append( unfoldDATA.Hreco())
    Covarinace_data.append( unfoldDATA.Ereco(2) )

# define the bias for Unfolding
VarMin = 0
VarMax = 132

GetTheBias(responseM, dataCorrected, mig_hist, cfg['Niterations'], VarMin, VarMax, cfg['Channel'], cfg['Energy'], cfg['Variable'])


'''

# define the bias for Unfolding
VarMin = 25
VarMax = 60

GetTheBias(responseM, dataCorrected, mig_hist, cfg['Niterations'], VarMin, VarMax, cfg['Channel'], cfg['Energy'], cfg['Variable'])

ToysOfData = GetToysofData(fInput_Data_BS, cfg['Channel'], cfg['Variable'], cfg['Energy'])

print(len(ToysOfData))

for i in range(0, len(ToysOfData) ):
    ToysOfData[i].Add(data_hist)
    ToysOfData[i] =  CorrectData( ToysOfData[i], reco_hist, Background_Total, Efficiency_hist)
    print(ToysOfData[i].GetMean())

# Get The Covariance Matrix:
CovarianceMatrix = []
for i in range(1, 1+cfg['Niterations']):
    print(" Iteration %d"%(i))
    unfoldDATA  = RooUnfoldBayes (responseM, dataCorrected, i)
    dataNominal = unfoldDATA.Hreco()
    UnfoldToys  = GetUnfoldToys(responseM, ToysOfData, i)
    Covariance  = GetCovarianceMatrix(dataNominal, UnfoldToys, VarMin, VarMax, cfg['Variable'], mig_hist)
    CovarianceMatrix.append(Covariance)
# Calculate the Sf Systematics:
if (cfg['Channel'].find("enu") != -1):
	print("Id systematics ")
	Id_Systematics   = GetSFSystematic( Input_SFid,   reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "ElIDSys",  cfg['Niterations'], VarMin, VarMax, "Muon") 
Iso_Systematics  = GetSFSystematic( Input_SFiso,  reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "MuIsoSys",   cfg['Niterations'], VarMin, VarMax, "Muon")
Reco_Systematics = GetSFSystematic( Input_SFreco, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "MuRecoSys",  cfg['Niterations'], VarMin, VarMax, "Muon")
Trig_Systematics = GetSFSystematic( Input_SFTrig, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "MuTrigSys",  cfg['Niterations'], VarMin, VarMax, "Muon")

#Calculate the Calib Systematics:
if  (cfg['Channel'].find("enu") != -1):
	CalibCovarianceItera  = []
	CalibVariation        = GetTheCalibVariation(cfg['Charge'], cfg['Energy'])
	GetPrinSystematic( CalibVariation, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], cfg['Niterations'], VarMin, VarMax, 1, "Calib")
'''
'''
#Calculate the Recoil Systematics:
RecoilCovarianceItera  = []
RecoilVariation        = GetTheRecoilVariation(cfg['Charge'], cfg['Energy'])
GetPrinSystematic( RecoilVariation, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], cfg['Niterations'], VarMin, VarMax, 1, "Recoil")
'''

# Save Output File
OutputFile = TFile("output_"+cfg['Channel']+str(cfg['Energy'])+"/"+cfg['Variable']+"_2d/Summarize_"+cfg['Channel']+str(cfg['Energy'])+".root",'RECREATE')
#OutputFile = TFile("output_wminusenu_5TeV_2d.root",'RECREATE')
Background_Total.Write("Background_Total")
mig_hist.Write("mig_hist")
truth_hist.Write("truth_hist")
data_hist.Write("data_hist")
reco_hist.Write("reco_hist")
Efficiency_hist.Write("Efficiency_hist")
Acceptance_hist.Write("Acceptance_hist")
dataCorrected.Write("dataCorrected")
for i in range(0, cfg['Niterations']):
    unfolded_data[i].Write("unfolded_data"+str(i+1))
#for i in range(0, len(ToysOfData) ):
#    ToysOfData[i].Write("Toys_data"+str(i+1))
for i in range(0, len(Covarinace_data) ):
    Covarinace_data[i].Write("CovarianceMatrix_Iter"+str(i+1))       

print("Fin")
