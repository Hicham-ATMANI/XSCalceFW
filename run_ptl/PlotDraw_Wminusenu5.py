#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1


from source.Test                        import *
from source.PlotClass2D                 import Plot2D
from source.PlotClass1D              	import Plot1D
from source.SystVariations              import SystVariations
from source.OpitmisationStudy           import OpitmisationStudy
from source.OpitmisationStudy1B         import OpitmisationStudy1B
from source.BackgroundClass             import BackgroundClass
from source.CrossSection                import CrossSection
from source.CrossSectionDev             import CrossSectionDev
from source.ComparisonUnfoldedMC        import ComparisonUnfoldedMC

#import matplotlib.pyplot as plt
import numpy as np
###Define all the Objects needed for next part """

CrossSectionDeter    =  CrossSection()
MatrixPlots          =  Plot2D()
NominalPlots         =  Plot1D()
SystematicsStudy     =  SystVariations()
Optimisation         =  OpitmisationStudy()
Optimisation1B       =  OpitmisationStudy1B()
BackgroundPlot       =  BackgroundClass()
CrossSectionDeterDev =  CrossSectionDev()
#TestPlot             =  Test()
Unfolded_MC          =  ComparisonUnfoldedMC()

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# minus enu 5 TeV
MCsamples_minusenu5  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wminusenu_MC_5TeV/Nominal/mc16_5TeV.361103.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusenu.e4916_s3238_r10243_r10210_p3665.root")
Summarize_minusenu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Summarize_Wminusenu5.root")
Bias_minusenu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Bias_Wminusenu5.root")

IdSF_minusenu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Syst_ElIDSys.root")
IsoSF_minusenu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Syst_ElIsoSys.root")
RecoSF_minusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Syst_ElRecoSys.root")
TrigSF_minusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Syst_ElTrigSys.root")
Recoil_minusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusenu5/elPt/Recoil_Syst.root")
Calib_minusenu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusenu5/elPt/Calib_Syst.root")

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusenu 5TeV '''

#NominalPlots.GetEpsilonFactors(Summarize_minusenu5,               "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#NominalPlots.GetAcceptanceFactors(Summarize_minusenu5,            "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#NominalPlots.MigrationMatrix(Summarize_minusenu5,                 "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#NominalPlots.ShowNominalDistribution(Summarize_minusenu5,         "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_minusenu5, 1,  9,                  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_minusenu5, 1,  9,        "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#NominalPlots.BiasProcedure( Summarize_minusenu5, Bias_minusenu5,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV" )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusenu 5TeV '''

#SystematicsStudy.CompareSystId(   IdSF_minusenu5,  1, 9, "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystIso(  IsoSF_minusenu5,  1, 9, "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystReco( RecoSF_minusenu5, 1, 9, "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystTrig( TrigSF_minusenu5, 1, 9, "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")

#SystematicsStudy.CompareSystRecoil( Summarize_minusenu5, Recoil_minusenu5, 1, 9, "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystCalib( Summarize_minusenu5,  Calib_minusenu5,  1, 9, "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu,   5TeV")
#SystematicsStudy.CompareSyst( Summarize_minusenu5, IdSF_minusenu5, IsoSF_minusenu5, RecoSF_minusenu5, TrigSF_minusenu5, Recoil_minusenu5, Calib_minusenu5, "Wminusenu5", "W^{-}#rightarrow e^{-}#nu,   5TeV")


""" ********************************************************************************************************************************************************* """
""" ************************************************************** Optimisation Study 1 bin ***************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  35, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  36, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  37, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  38, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  39, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  40, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  41, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  42, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  43, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  44, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  45, "Wminusenu5", "$p^{T}_{W}$")    # define the number of iterations for the study

#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")
#


#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  35, "Wminusenu5", "$p^{T}_{l}$", "ptl")    # define the number of iterations for the study
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  45,  "Wminusenu5", "W^{-}#rightarrow e^{-}#nu, 5TeV", "$p^{T}_{W}$")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 25, 60,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 30, 55,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 30, 50,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 35, 45,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 25, 60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 30, 55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 30, 50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 35, 45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 25,  60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 30,  55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 30,  50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 35,  45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 25,   60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 30,   55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 30,   50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 35,   45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 25,   60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 30,   55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 30,   50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 35,   45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 25,   60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 30,   55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 30,   50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 35,   45,  "Wminusenu5", "$p^{T}_{l}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_minusenu5, 2,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_minusenu5,      2,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu, 5TeV", "5TeV")
#MatrixPlots.SystCovarianceMatrix(RecoSF_minusenu5, 2,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#DiffernetialXsPlot(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-}#rightarrow e^{-}#nu, 5TeV", "Wminusenu5", 256.827)
#CrossSectionDeter.GetDiffernetialXs(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W$^{-}$ $\\rightarrow$ e$^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusenu5", 256.827, 2)
#CrossSectionDeter.GetDiffernetialXsPlot(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-}#rightarrow e^{-}#nu, 5TeV", "Wminusenu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-}#rightarrow e^{-}#nu, 5TeV", "Wminusenu5", 256.827)

""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-} \\rightarrow e^{-} \\nu, 5TeV", "Wminusenu5", 256.827)
#CrossSectionDeter.GetSummaringTable(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W$^{-}$ $\\rightarrow$ e$^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusenu5", 256.827, 0.460)

""" ********************************************************************************************************************************************************* """
""" ******************************************************************** Background Plot ******************************************************************** """
""" ********************************************************************************************************************************************************* """
'''
channel              = "Wminusenu"
Energy               = "5TeV"
Indice               = "W^{-}#rightarrow e^{-}#nu, 5TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/pTWanalysis_ptwminusenu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/pTWanalysis_ptwminusenu_MC_5TeV/Nominal/mc16_5TeV.361103.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusenu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/Background/Wminusenu5/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/Background/Wminusenu5/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/Background/Wminusenu5/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/Background/Wminusenu5/Background_Z.root")
Background_MiltiJetN = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/Background/Wminusenu5/Background_MiltiJet_new.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/Old5TeV/DataSets_5TeV/Background/Wminusenu5/Background_MiltiJet.root")
Uncertainties        = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wminusenu_MC_5TeV/Uncertainties/SystematicsptW.root")
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
'''
'''
channel              = "Wplusenu"
Energy               = "5TeV"
Indice               = "W^{+}#rightarrow e^{+}#nu, 5TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wplusenu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wplusenu_MC_5TeV/Nominal/mc16_5TeV.361100.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusenu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusenu5/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusenu5/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusenu5/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusenu5/Background_Z.root")
Background_MiltiJetN = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusenu5/Background_MiltiJet_new.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusenu5/Background_MiltiJet.root")
Uncertainties        = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wplusenu_MC_5TeV/Uncertainties/SystematicsptW.root")
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
'''
'''
channel              = "Wminusmunu"
Energy               = "5TeV"
Indice               = "W^{-}#rightarrow #mu^{-}#nu, 5TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wminusmunu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wminusmunu_MC_5TeV/Nominal/mc16_5TeV.361104.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusmunu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wminusmunu5/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wminusmunu5/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wminusmunu5/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wminusmunu5/Background_Z.root")
Background_MiltiJetN = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wminusmunu5/Background_MiltiJet_new.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wminusmunu5/Background_MiltiJet.root")
Uncertainties        = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wminusmunu_MC_5TeV/Uncertainties/SystematicsptW.root")
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
'''

channel             = "Wplusmunu"
Energy              = "5TeV"
Indice              = "W^{+}#rightarrow #mu^{+}#nu, 5TeV"
data                = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wplusmunu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Signal              = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wplusmunu_MC_5TeV/Nominal/mc16_5TeV.361101.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusmunu.e4916_s3238_r10243_r10210_p3665.root")
Background_Top      = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusmunu5/Background_Top.root")
Background_diboson  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusmunu5/Background_dilepton.root")
Background_W        = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusmunu5/Background_W.root")
Background_Z        = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusmunu5/Background_Z.root")
Background_MiltiJetN= ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusmunu5/Background_MiltiJet_new.root")
Background_MiltiJet = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/Background/Wplusmunu5/Background_MiltiJet.root")
Uncertainties       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_wplusmunu_MC_5TeV/Uncertainties/SystematicsptW.root")
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTlepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJetN, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotsmTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
#BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy)
BackgroundPlot.BackgroundPlotspTW(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Uncertainties, Indice, channel, Energy)

