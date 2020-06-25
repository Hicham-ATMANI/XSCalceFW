#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1


from source.PlotClass1D              import Plot1D
from source.SystVariations              import SystVariations
from source.PlotClass2D                 import Plot2D
from source.OpitmisationStudy           import OpitmisationStudy
from source.OpitmisationStudy1B         import OpitmisationStudy1B
from source.BackgroundClass             import BackgroundClass
from source.CrossSection                import CrossSection
from source.CrossSectionDev             import CrossSectionDev
from source.ComparisonUnfoldedMC        import ComparisonUnfoldedMC

from source.Test                import Test

import matplotlib.pyplot as plt
import numpy as np

""" Define all the Objects needed for next part """
NominalPlots         =  Plot1D()
SystematicsStudy     =  SystVariations()
MatrixPlots          =  Plot2D()
Optimisation         =  OpitmisationStudy()
Optimisation1B       =  OpitmisationStudy1B()
BackgroundPlot       =  BackgroundClass()
CrossSectionDeter    =  CrossSection()
CrossSectionDeterDev =  CrossSectionDev()
TestPlot             =  Test()
Unfolded_MC          =  ComparisonUnfoldedMC()

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# plus enu 5 TeV
MCsamples_plusenu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker/Processing/pTW_Input/pTWanalysis_ptwplusenu_MC_5TeV/Nominal/mc16_5TeV.361100.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusenu.e4916_s3238_r10243_r10210_p3665.root")
Summarize_plusenu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Summarize_Wplusenu5.root")
Bias_plusenu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Bias_Wplusenu5.root")

IdSF_plusenu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Syst_ElIDSys.root")
IsoSF_plusenu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Syst_ElIsoSys.root")
RecoSF_plusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Syst_ElRecoSys.root")
TrigSF_plusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Syst_ElTrigSys.root")
Recoil_plusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Recoil_Syst.root")
Calib_plusenu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusenu5/mT/Calib_Syst.root")

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wplusenu 5TeV '''

#NominalPlots.GetEpsilonFactors(Summarize_plusenu5,                "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.GetAcceptanceFactors(Summarize_plusenu5,             "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.MigrationMatrix(Summarize_plusenu5,                  "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
NominalPlots.ShowNominalDistribution(Summarize_plusenu5,          "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_plusenu5, 1,  10,                   "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_plusenu5, 10, 19,                   "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_plusenu5, 1,  10,         "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_plusenu5, 10, 19,         "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#NominalPlots.BiasProcedure( Summarize_plusenu5, Bias_plusenu5,  "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV" )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wplusenu 5TeV '''

#SystematicsStudy.CompareSystId(   IdSF_plusenu5,   1, 10, "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystIso(  IsoSF_plusenu5,  1, 10, "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystReco( RecoSF_plusenu5, 1, 10, "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystTrig( TrigSF_plusenu5, 1, 10, "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")

#SystematicsStudy.CompareSystRecoil(  Summarize_plusenu5, Recoil_plusenu5, 1, 10, "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystCalib(  Summarize_plusenu5,  Calib_plusenu5,  1, 10, "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu,   5TeV")
#SystematicsStudy.CompareSyst( Summarize_plusenu5, IdSF_plusenu5, IsoSF_plusenu5, RecoSF_plusenu5, TrigSF_plusenu5, Recoil_plusenu5, Calib_plusenu5, "Wplusenu5", "W^{+}#rightarrow e^{+}#nu,   5TeV")


""" ********************************************************************************************************************************************************* """
""" ************************************************************** Optimisation Study 1 bin ***************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  38, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  39, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  40, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  41, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  42, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  43, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  44, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_plusenu5, 1, 20,  45, "Wplusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study

#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  38,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  39,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  40,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  41,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  42,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  43,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  44,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20,  45,  "Wplusenu5", "$p^{T}_{W}$")

#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  38,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  39,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  40,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  41,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  42,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  43,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  44,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19,  45,  "Wplusenu5", "$p^{T}_{W}$")

#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  38,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  39,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  40,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  41,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  42,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  43,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  44,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19,  45,  "Wplusenu5", "$p^{T}_{W}$")

#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  38,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  39,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  40,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  41,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  42,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  43,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  44,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19,  45,  "Wplusenu5", "$p^{T}_{W}$")

#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  38,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  39,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  40,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  41,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  42,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  43,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  44,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  45,  "Wplusenu5", "$p^{T}_{W}$")

#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  38,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  39,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  40,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  41,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  42,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  43,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  44,  "Wplusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19,  45,  "Wplusenu5", "$p^{T}_{W}$")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation.StatStudy(Summarize_plusenu5, 1, 20, 50, 100, "Wplusenu5", "$m^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusenu5, 1, 20, 60, 90,  "Wplusenu5", "$m^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusenu5, 1, 20, 70, 90,  "Wplusenu5", "$m^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusenu5, 1, 20, 75, 85,  "Wplusenu5", "$m^{T}_{W}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20, 50, 100, "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20, 60, 90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20, 70, 90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_plusenu5, Bias_plusenu5, 1, 20, 75, 85,  "Wplusenu5", "$m^{T}_{W}$")

#Optimisation.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19, 50, 100,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19, 60,  90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19, 70,  90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, 1, 19, 75,  85,  "Wplusenu5", "$m^{T}_{W}$")

#Optimisation.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19, 50,  100,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19, 60,   90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19, 70,   90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.CalibSystematicStudy(Summarize_plusenu5, Calib_plusenu5, 1, 19, 75,   85,  "Wplusenu5", "$m^{T}_{W}$")

#Optimisation.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19, 50,  100,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19, 60,   90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19, 70,   90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusenu5, Recoil_plusenu5, 1, 19, 75,   85,  "Wplusenu5", "$m^{T}_{W}$")

#Optimisation.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19, 50,  100,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19, 60,   90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19, 70,   90,  "Wplusenu5", "$m^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, 1, 19, 75,   85,  "Wplusenu5", "$m^{T}_{W}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_plusenu5, 4,  "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_plusenu5,      4,  "Wplusenu5",   "W^{+}#rightarrow e^{+}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetDiffernetialXs(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, "5TeV", "W$^{+}$ $\\rightarrow$ e$^{+} \\nu $, 5TeV, Uncertainties in (\%)", "Wplusenu5", 256.827, 2)
#CrossSectionDeter.GetDiffernetialXsPlot(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, "5TeV", "W^{+}#rightarrow e^{+}#nu, 5TeV", "Wplusenu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, "5TeV", "W^{+}#rightarrow e^{+}#nu, 5TeV", "Wplusenu5", 256.827)


""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-} \\rightarrow e^{-} \\nu, 5TeV", "Wminusenu5", 256.827)
#CrossSectionDeter.GetSummaringTable(Summarize_plusenu5, Bias_plusenu5, TrigSF_plusenu5, RecoSF_plusenu5, IsoSF_plusenu5, IdSF_plusenu5, Calib_plusenu5, Recoil_plusenu5, "5TeV", "W$^{+}$ $\\rightarrow$ e$^{+} \\nu $, 5TeV, Uncertainties in (\%)", "Wplusenu5", 256.827, 0.460)

""" ********************************************************************************************************************************************************* """
""" ******************************************************************** Background Plot ******************************************************************** """
""" ********************************************************************************************************************************************************* """
'''
channel             = "Wminusenu"
Energy              = "5TeV"
Indice              = "W^{-}#rightarrow e^{-}#nu, 5TeV"
data                = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/data17_minusenu_5TeV.root")
Signal              = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/mc16_5TeV.361103.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusenu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top      = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusenu5/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusenu5/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusenu5/Background_W.root")
Background_Z        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusenu5/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusenu5/Background_MiltiJet.root")
BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)

channel             = "Wplusenu"
Energy              = "5TeV"
Indice              = "W^{+}#rightarrow e^{+}#nu, 5TeV"
data                = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/data17_plusenu_5TeV.root")
Signal              = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/mc16_5TeV.361100.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusenu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top      = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusenu5/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusenu5/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusenu5/Background_W.root")
Background_Z        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusenu5/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusenu5/Background_MiltiJet.root")
BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)

channel             = "Wminusmunu"
Energy              = "5TeV"
Indice              = "W^{-}#rightarrow #mu^{-}#nu, 5TeV"
data                = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/data17_minusmunu_5TeV.root")
Signal              = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/mc16_5TeV.361104.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusmunu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top      = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusmunu5/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusmunu5/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusmunu5/Background_W.root")
Background_Z        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusmunu5/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wminusmunu5/Background_MiltiJet.root")
BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)

channel             = "Wplusmunu"
Energy              = "5TeV"
Indice              = "W^{+}#rightarrow #mu^{+}#nu, 5TeV"
data                = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/data17_plusmunu_5TeV.root")
Signal              = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/pT_Input/mc16_5TeV.361101.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusmunu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top      = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusmunu5/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusmunu5/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusmunu5/Background_W.root")
Background_Z        = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusmunu5/Background_Z.root")
Background_MiltiJet = ROOT.TFile.Open("/Users/hatmani/pTw_Unfolding/Inputs/Background/Wplusmunu5/Background_MiltiJet.root")
BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
'''
