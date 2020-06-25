#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1

from source.Test                	import *

from source.PlotClass2D                 import Plot2D
from source.PlotClass1D              	import Plot1D
from source.SystVariations              import SystVariations
from source.OpitmisationStudy1B         import OpitmisationStudy1B
from source.OpitmisationStudy           import OpitmisationStudy
from source.BackgroundClass             import BackgroundClass
from source.CrossSection                import CrossSection
from source.CrossSectionDev             import CrossSectionDev
from source.ComparisonUnfoldedMC        import ComparisonUnfoldedMC

import matplotlib.pyplot as plt
import numpy as np

""" Define all the Objects needed for next part """
MatrixPlots          =  Plot2D()
NominalPlots         =  Plot1D()
SystematicsStudy     =  SystVariations()
Optimisation         =  OpitmisationStudy()
Optimisation1B       =  OpitmisationStudy1B()
BackgroundPlot       =  BackgroundClass()
CrossSectionDeter    =  CrossSection()
CrossSectionDeterDev =  CrossSectionDev()
Unfolded_MC          =  ComparisonUnfoldedMC()

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# minus enu 5 TeV
MCsamples_minusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker/Processing/pTW_Input/pTWanalysis_ptwminusmunu_MC_5TeV/Nominal/mc16_5TeV.361101.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusmunu.e4916_s3238_r10243_r10210_p3665.root")
Summarize_minusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusmunu5/MuPt/Summarize_Wminusmunu5.root")
Bias_minusmunu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusmunu5/MuPt/Bias_Wminusmunu5.root")

IsoSF_minusmunu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusmunu5/MuPt/Syst_MuIsoSys.root")
RecoSF_minusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusmunu5/MuPt/Syst_MuRecoSys.root")
TrigSF_minusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wminusmunu5/MuPt/Syst_MuTrigSys.root")
Recoil_minusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/MuPt/Recoil_Syst.root")


""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusmunu 5TeV '''

#NominalPlots.GetEpsilonFactors(Summarize_minusmunu5,                "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.GetAcceptanceFactors(Summarize_minusmunu5,             "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.MigrationMatrix(Summarize_minusmunu5,                  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.ShowNominalDistribution(Summarize_minusmunu5,          "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_minusmunu5, 1,  9,                   "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_minusmunu5, 1,  9,         "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.BiasProcedure( Summarize_minusmunu5, Bias_minusmunu5,  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV" )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusmunu 5TeV '''

#SystematicsStudy.CompareSystIso(  IsoSF_minusmunu5,  1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystReco( RecoSF_minusmunu5, 1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystTrig( TrigSF_minusmunu5, 1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystRecoil(  Summarize_minusmunu5, Recoil_minusmunu5, 1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSyst( Summarize_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, RecoSF_minusmunu5, TrigSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, "Wminusmunu5", "W^{-}#rightarrow #mu^{-}#nu,   5TeV")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  35,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  36,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  37,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  38,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  39,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  41,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  42,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  43,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  44,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 10,  45,  "Wminusmunu5", "$p^{T}_{W}$")

#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  35,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  36,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  37,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  38,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  39,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  41,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  42,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  43,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  44,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  45,  "Wminusmunu5", "$p^{T}_{W}$")

#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  35,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  36,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  37,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  38,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  39,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  41,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  42,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  43,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  44,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 9,  45,  "Wminusmunu5", "$p^{T}_{W}$")

#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 25, 60,  "Wminusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 30, 55,  "Wminusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 30, 50,  "Wminusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 35, 45,  "Wminusmunu5", "$p^{T}_{l}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 25, 60,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 30, 55,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 30, 50,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 35, 45,  "Wminusmunu5", "$p^{T}_{l}$")

#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 25,  60,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 30,  55,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 30,  50,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 35,  45,  "Wminusmunu5", "$p^{T}_{l}$")

#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 25,   60,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 30,   55,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 30,   50,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 35,   45,  "Wminusmunu5", "$p^{T}_{l}$")

#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 25,   60,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 30,   55,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 30,   50,  "Wminusmunu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 35,   45,  "Wminusmunu5", "$p^{T}_{l}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_minusmunu5, 2,  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_minusmunu5,      2,  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """
#DiffernetialXsPlot(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "Wminusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXs(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W$^{-}$ $\\rightarrow$ $\\mu^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusmunu5", 256.827, 2)
CrossSectionDeter.GetDiffernetialXsPlot(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "Wminusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "Wminusmunu5", 256.827)

""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-} \\rightarrow \\mu ^{-} \\nu, 5TeV", "Wminusmunu5", 256.827)
#CrossSectionDeter.GetSummaringTable(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, "5TeV", "W$^{-}$ $\\rightarrow$ $\\mu$ $^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusmunu5", 256.827, 0.397)

