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

# plus enu 5 TeV
MCsamples_plusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker/Processing/pTW_Input/pTWanalysis_ptwplusmunu_MC_5TeV/Nominal/mc16_5TeV.361101.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusmunu.e4916_s3238_r10243_r10210_p3665.root")
Summarize_plusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/mT/Summarize_Wplusmunu5.root")
Bias_plusmunu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/mT/Bias_Wplusmunu5.root")

IsoSF_plusmunu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/mT/Syst_MuIsoSys.root")
RecoSF_plusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/mT/Syst_MuRecoSys.root")
TrigSF_plusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/mT/Syst_MuTrigSys.root")
Recoil_plusmunu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold/output_Wplusmunu5/mT/Recoil_Syst.root")

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wplusmunu 5TeV '''

NominalPlots.GetEpsilonFactors(Summarize_plusmunu5,                "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.GetAcceptanceFactors(Summarize_plusmunu5,             "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.MigrationMatrix(Summarize_plusmunu5,                  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.ShowNominalDistribution(Summarize_plusmunu5,          "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_plusmunu5, 1,  10,                   "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.CompareBias(Bias_plusmunu5, 10, 19,                   "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_plusmunu5, 1,  10,         "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.CompareStatError(Summarize_plusmunu5, 10, 19,         "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#NominalPlots.BiasProcedure( Summarize_plusmunu5, Bias_plusmunu5,  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV" )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wplusmunu 5TeV '''

#SystematicsStudy.CompareSystIso(  IsoSF_plusmunu5,  1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystReco( RecoSF_plusmunu5, 1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystTrig( TrigSF_plusmunu5, 1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")
#SystematicsStudy.CompareSystRecoil(  Summarize_plusmunu5, Recoil_plusmunu5, 1, 10, "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu,   5TeV")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 50, 100,  "Wplusmunu5", "$m^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 60,  90,  "Wplusmunu5", "$m^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 70,  90,  "Wplusmunu5", "$m^{T}_{W}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_plusmunu5, 1, 20, 75,  85,  "Wplusmunu5", "$m^{T}_{W}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 50, 100,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 60,  90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 70,  90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.BiasStudy(Summarize_plusmunu5, Bias_plusmunu5, 1, 20, 75,  85,  "Wplusmunu5", "$m^{T}_{W}$")

#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 50, 100,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 60,  90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 70,  90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.EffSystematicStudy(Summarize_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, 1, 19, 75,  85,  "Wplusmunu5", "$m^{T}_{W}$")

#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 50,  100,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 60,   90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 70,   90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.RecoilSystematicStudy(Summarize_plusmunu5, Recoil_plusmunu5, 1, 19, 75,   85,  "Wplusmunu5", "$m^{T}_{W}$")

#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 50,  100,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 60,   90,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 70,   80,  "Wplusmunu5", "$m^{T}_{W}$")
#Optimisation.TotalSystematicStudy(Summarize_plusmunu5, Bias_plusmunu5,  TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, Recoil_plusmunu5, 1, 19, 75,   85,  "Wplusmunu5", "$m^{T}_{W}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_plusmunu5, 3,  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_plusmunu5,      3,  "Wplusmunu5",   "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetDiffernetialXs(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W$^{+}$ $\\rightarrow$ $\\mu^{+} \\nu $, 5TeV, Uncertainties in (\%)", "Wplusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlot(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "Wplusmunu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_plusmunu5, Bias_plusmunu5, TrigSF_plusmunu5, RecoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, IsoSF_plusmunu5, Recoil_plusmunu5, "5TeV", "W^{+}#rightarrow #mu^{+}#nu, 5TeV", "Wplusmunu5", 256.827)


""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_plusmunu5, Bias_plusmunu5, "5TeV", "W^{+} \\rightarrow e^{+} \\nu, 5TeV", "Wplusmunu5")

