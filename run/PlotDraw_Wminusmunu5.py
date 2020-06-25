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
BackgroundPlot       =  BackgroundClass()
CrossSectionDeter    =  CrossSection()
CrossSectionDeterDev =  CrossSectionDev()
TestPlot             =  Test()
Unfolded_MC          =  ComparisonUnfoldedMC()

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# minus enu 5 TeV
Summarize_minusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/WpT/Summarize_Wminusmunu5.root")
Bias_minusmunu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/WpT/Bias_Wminusmunu5.root")

IsoSF_minusmunu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/WpT/Syst_MuIsoSys.root")
RecoSF_minusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/WpT/Syst_MuRecoSys.root")
TrigSF_minusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/WpT/Syst_MuTrigSys.root")
Recoil_minusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/buckup/old/output_Wminusmunu5/WpT/Recoil_Syst.root")

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusmunu 5TeV '''

#NominalPlots.GetEpsilonFactors(Summarize_minusmunu5,                "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.GetAcceptanceFactors(Summarize_minusmunu5,             "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.MigrationMatrix(Summarize_minusmunu5,                  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.ShowNominalDistribution(Summarize_minusmunu5,          "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_minusmunu5, 1,  10,                   "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_minusmunu5, 10, 19,                   "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_minusmunu5, 1,  10,         "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_minusmunu5, 10, 19,         "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#NominalPlots.BiasProcedure( Summarize_minusmunu5, Bias_minusmunu5,  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV" )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusmunu 5TeV '''

#SystematicsStudy.CompareSystIso(  IsoSF_minusmunu5,  1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystReco( RecoSF_minusmunu5, 1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystTrig( TrigSF_minusmunu5, 1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")
#SystematicsStudy.CompareSystRecoil(  Summarize_minusmunu5, Recoil_minusmunu5, 1, 10, "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu,   5TeV")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 0, 600, "Wminusmunu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 0, 60,  "Wminusmunu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 0, 40,  "Wminusmunu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 0, 20,  "Wminusmunu5", "$p^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusmunu5, 1, 20, 0, 10,  "Wminusmunu5", "$p^{T}_{W}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 0, 600, "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 0, 60,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 0, 40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 0, 20,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_minusmunu5, Bias_minusmunu5, 1, 20, 0, 10,  "Wminusmunu5", "$p^{T}_{W}$")

#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 0, 600,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 0,  60,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 0,  40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 0,  20,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, 1, 19, 0,  10,  "Wminusmunu5", "$p^{T}_{W}$")

#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 0,  600,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   60,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   20,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   10,  "Wminusmunu5", "$p^{T}_{W}$")

#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 0,  600,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   60,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   40,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   20,  "Wminusmunu5", "$p^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_minusmunu5, Bias_minusmunu5,  TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, 1, 19, 0,   10,  "Wminusmunu5", "$p^{T}_{W}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_minusmunu5, 4,  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_minusmunu5,      4,  "Wminusmunu5",   "W^{-}#rightarrow #mu^{-}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """
CrossSectionDeter.GetptwTables(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W$^{-}$ $\\rightarrow$ $\\mu ^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusmunu5", 256.827, 2)


#CrossSectionDeter.GetDiffernetialXs(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W$^{-}$ $\\rightarrow$ $\\mu ^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlot(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-}#rightarrow \\mu^{-}#nu, 5TeV", "Wminusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-}#rightarrow \\mu^{-}#nu, 5TeV", "Wminusmunu5", 256.827)

""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, "5TeV", "W^{-} \\rightarrow \\mu ^{-} \\nu, 5TeV", "Wminusmunu5", 256.827)
#CrossSectionDeter.GetSummaringTable(Summarize_minusmunu5, Bias_minusmunu5, TrigSF_minusmunu5, RecoSF_minusmunu5, IsoSF_minusmunu5, IsoSF_minusmunu5, Recoil_minusmunu5, Recoil_minusmunu5, "5TeV", "W$^{-}$ $\\rightarrow$ $\\mu$ $^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusmunu5", 256.827, 0.397)

