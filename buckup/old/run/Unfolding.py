#!/usr/bin/env python
# -*-coding:Latin-1 -*

# ==============================================================================
#  Description:
#       Unfolding using for pT(W), mT(W), pT(lepton) and eta(lepton)
#  Author:  ATMANI Hicham
# ==============================================================================

from ROOT import gRandom, TH1, TH1D, cout
from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from ROOT import TFile
from source import *

import yaml

# ==============================================================================
#  				Read the config file
# ==============================================================================

with open("config.yml", 'r') as ymlfile:
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

# define the output file:
OutputFile = TFile("output_" + cfg['Channel'] + str(cfg['Energy']) +"/"+ cfg['Variable'] + "/" + "Summarize_" + cfg['Channel'] + str(cfg['Energy']) +"TeV.root","RECREATE")

# read the Input files:
if( cfg['Channel'] == "Wminusenu" and cfg['Energy'] == 5):
	fInput_MC    = TFile( cfg['Wminusenu5_MC'] );       fInput_Data  = TFile( cfg['Wminusenu5_data'] );    fInput_Data_BS  = TFile( cfg['Wminusenu5_BSdata']);  Input_Bkgd1  = TFile( cfg['Wminusenu5_Bkgd1'] );
	Input_Bkgd2  = TFile( cfg['Wminusenu5_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wminusenu5_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wminusenu5_Bkgd4']);   Input_Bkgd5  = TFile( cfg['Wminusenu5_Bkgd5'] );

if( cfg['Channel'] == "Wplusenu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wplusenu5_MC'] );        fInput_Data  = TFile( cfg['Wplusenu5_data'] );     fInput_Data_BS  = TFile( cfg['Wplusenu5_BSdata']);   Input_Bkgd1  = TFile( cfg['Wplusenu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusenu5_Bkgd2'] );     Input_Bkgd3  = TFile( cfg['Wplusenu5_Bkgd3'] );    Input_Bkgd4     = TFile( cfg['Wplusenu5_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wplusenu5_Bkgd5'] );

if( cfg['Channel'] == "Wminusmunu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wminusmunu5_MC'] );      fInput_Data  = TFile( cfg['Wminusmunu5_data'] );   fInput_Data_BS  = TFile( cfg['Wminusmunu5_BSdata']); Input_Bkgd1  = TFile( cfg['Wminusmunu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wminusmunu5_Bkgd2'] );   Input_Bkgd3  = TFile( cfg['Wminusmunu5_Bkgd3'] );  Input_Bkgd4     = TFile( cfg['Wminusmunu5_Bkgd4']);  Input_Bkgd5  = TFile( cfg['Wminusmunu5_Bkgd5'] );

if( cfg['Channel'] == "Wplusmunu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wplusmunu5_MC'] );       fInput_Data  = TFile( cfg['Wplusmunu5_data'] );    fInput_Data_BS  = TFile( cfg['Wplusmunu5_BSdata']);  Input_Bkgd1  = TFile( cfg['Wplusmunu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusmunu5_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wplusmunu5_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wplusmunu5_Bkgd4']);   Input_Bkgd5  = TFile( cfg['Wplusmunu5_Bkgd5'] );



# calculate the Total Background

Var = cfg['Variable'] 
if( Var == "WpT" ):Var = Var + "_Reco"; 

Background_Total = SumBackground(Input_Bkgd1, Input_Bkgd2, Input_Bkgd3, Input_Bkgd5, Input_Bkgd4, cfg['Channel'], Var )

#Background_W        = Input_Bkgd1.Get(  cfg['Channel'] +"Selection/" +  Var +"_cut7" )
#Background_Z        = Input_Bkgd2.Get(  cfg['Channel'] +"Selection/" +  Var +"_cut7" )
#Background_Dilepton = Input_Bkgd3.Get(  cfg['Channel'] +"Selection/" +  Var +"_cut7" )
#Background_Top 	    = Input_Bkgd5.Get(  cfg['Channel'] +"Selection/" +  Var +"_cut7" )
#Background_Mj       = Input_Bkgd4.Get(  "hist/" +  Var +"_cut7" )

#Background_Total    = Background_W.Clone("Background_Total")
#Background_Total.Add(Background_Z)
#Background_Total.Add(Background_Dilepton)
#Background_Total.Add(Background_Top)
#Background_Total.Add(Background_Mj)

# read the migration Matrix: 
if( cfg['Variable'] == "elEta" ):
	mig_hist       = fInput_MC.Get( cfg['Channel'] + "Selection/el_Eta_Reco_v_Truth_"+ str(cfg['Energy'])  +"TeV_cut7") 
else:
        mig_hist       = fInput_MC.Get( cfg['Channel'] + "Selection/"+ cfg['Variable'] +"_Reco_v_Truth_"+ str(cfg['Energy'])  +"TeV_cut7") 

# read the truth histograms:: 
if( cfg['Variable'] == "WpT" ):
	truth_hist     = fInput_MC.Get( "TruthSelection/"+ cfg['Variable']  +"_Truth_" + str(cfg['Energy']) + "TeV_cut4" )
else:
	truth_hist     = fInput_MC.Get( "TruthSelection/"+ cfg['Variable']  +"_Truth_cut4" )
 
# read the reco histograms:: 
GetSelectionsPlots()



print("djznfej")

