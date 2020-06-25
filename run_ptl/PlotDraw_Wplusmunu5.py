#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1


from source.Test                	import *
'''
from source.PlotClass2D                 import Plot2D
from source.OpitmisationStudy1B         import OpitmisationStudy1B
from source.PlotClass1D              	import Plot1D
from source.SystVariations              import SystVariations
from source.OpitmisationStudy           import OpitmisationStudy
from source.BackgroundClass             import BackgroundClass
from source.CrossSection                import CrossSection
from source.CrossSectionDev             import CrossSectionDev
from source.ComparisonUnfoldedMC        import ComparisonUnfoldedMC
from source.Test                import Test
'''
import matplotlib.pyplot as plt
import numpy as np

""" Define all the Objects needed for next part """
'''
MatrixPlots          =  Plot2D()
NominalPlots         =  Plot1D()
SystematicsStudy     =  SystVariations()
Optimisation         =  OpitmisationStudy()
Optimisation1B       =  OpitmisationStudy1B()
BackgroundPlot       =  BackgroundClass()
CrossSectionDeter    =  CrossSection()
CrossSectionDeterDev =  CrossSectionDev()
TestPlot             =  Test()
Unfolded_MC          =  ComparisonUnfoldedMC()
'''
""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# plus enu 5 TeV
MCsamples_plusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker/Processing/pTW_Input/pTWanalysis_ptwplusmunu_MC_5TeV/Nominal/mc16_5TeV.361101.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusmunu.e4916_s3238_r10243_r10210_p3665.root")
Summarize_plusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/MuPt/Summarize_Wplusmunu5.root")
Bias_plusmunu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/MuPt/Bias_Wplusmunu5.root")

IsoSF_plusmunu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/MuPt/Syst_MuIsoSys.root")
RecoSF_plusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/MuPt/Syst_MuRecoSys.root")
TrigSF_plusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/MuPt/Syst_MuTrigSys.root")
Recoil_plusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wplusmunu5/MuPt/Recoil_Syst.root")

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wplusmunu 5TeV '''

#NominalPlots.GetEpsilonFactors(Summarize_plusmunu5,                "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.GetAcceptanceFactors(Summarize_plusmunu5,             "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.MigrationMatrix(Summarize_plusmunu5,                  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.ShowNominalDistribution(Summarize_plusmunu5,          "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_plusmunu5, 1,  9,                   "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_plusmunu5, 1,  9,         "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.BiasProcedure( Summarize_plusmunu5, Bias_plusmunu5,   "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV" )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wplusmunu 5TeV '''

#SystematicsStudy.CompareSystIso(  IsoSF_plusmunu5,  1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystReco( RecoSF_plusmunu5, 1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystTrig( TrigSF_plusmunu5, 1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystRecoil(  Summarize_plusmunu5, Recoil_plusmunu5, 1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSyst( Summarize_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, RecoSF_plusmunu5, TrigSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, "Wplusmunu5", "W^{+}#rightarrow #mu^{+}#nu,   5TeV")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  35,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  36,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  37,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  38,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  39,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  40,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  41,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  42,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  43,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  44,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 10,  45,  "Wplusmunu5", "$p^{T}_{W}$")

#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  35,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  36,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  37,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  38,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  39,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  40,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  41,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  42,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  43,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  44,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  45,  "Wplusmunu5", "$p^{T}_{W}$")

#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  35,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  36,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  37,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  38,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  39,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  40,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  41,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  42,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  43,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  44,  "Wplusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 9,  45,  "Wplusmunu5", "$p^{T}_{W}$")

#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 25,  60,  "Wplusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 30,  55,  "Wplusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 30,  50,  "Wplusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 35,  45,  "Wplusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 25,  60,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 30,  55,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 30,  50,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 35,  45,  "Wplusmunu5", "$p^{T}_{l}$")

#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 25,  60,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 30,  55,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 30,  50,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 35,  45,  "Wplusmunu5", "$p^{T}_{l}$")

#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 25,   60,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 30,   55,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 30,   50,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 35,   45,  "Wplusmunu5", "$p^{T}_{l}$")

#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 35,   60,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 30,   55,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 30,   50,  "Wplusmunu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 35,   45,  "Wplusmunu5", "$p^{T}_{l}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_plusmunu5, 3,  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_plusmunu5,      3,  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """
DiffernetialXsPlot(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "Wplusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXs(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W$^{+}$ $\\rightarrow$ $\\mu^{+} \\nu $, 5TeV, Uncertainties in (\%)", "Wplusmunu5", 256.827, 2)
#CrossSectionDeter.GetDiffernetialXsPlot(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "Wplusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "Wplusmunu5", 256.827)


""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_plusmunu5, Bias_plusmunu5, "5TeV", "W^{+} \\rightarrow e^{+} \\nu, 5TeV", "Wplusmunu5")

