#!/usr/bin/env python
# -*-coding:Latin-1 -*

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from   ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TAttFill, TF1, gStyle, gPad, TStyle

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend


class Plot1D:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""

    def GetSelectionsPlots(self, inputFile, channel, Indice, SelectionCode):

        TruthSelections = inputFile.Get("TruthSelectionCutFlow")
        RecoSelections  = inputFile.Get(SelectionCode+"SelectionCutFlow")

        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        TruthSelections.SetStats(0)
        TruthSelections.SetTitle("")
        TruthSelections.SetLineWidth(2)
        TruthSelections.SetLineColor(2)
        TruthSelections.Draw()
        astyle.ATLASLabel(0.15, 0.82, "Internal")
        utils.DrawText(0.15, 0.76, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_TruthSelections.pdf")

        c2 = root.TCanvas("c2", "The FillRandom example", 0, 0, 800, 600)
        RecoSelections.SetStats(0)
        RecoSelections.SetTitle("")
        RecoSelections.SetLineWidth(2)
        RecoSelections.SetLineColor(2)
        RecoSelections.Draw()
        astyle.ATLASLabel(0.15, 0.82, "Internal")
        utils.DrawText(0.15, 0.76, Indice)
        c2.Print("Output/"+channel+"/"+channel+"_RecoSelections.pdf")


    def BiasProcedure(self, inputFile, Bias, channel, Indice):

	reco	= Bias.Get("reco_hist")
	reco_W  = Bias.Get("reco_hist_Weighted")
	data    = inputFile.Get("dataCorrected")
	
	reco.Divide(data)
	reco_W.Divide(data)

	        
	f1 = TF1("f1","pol7", 50, 100)
        reco.Fit("f1")

        reco.SetStats(0)
        reco.SetTitle("")
        reco.SetLineWidth(2)
        reco.SetLineColor(2)
        reco.SetMarkerStyle(10)
        reco.SetMarkerSize(1)
        reco.SetMarkerColor(2)

        reco_W.SetLineWidth(2)
        reco_W.SetLineColor(4)
        reco_W.SetMarkerStyle(10)
        reco_W.SetMarkerSize(1)
        reco_W.SetMarkerColor(4)

        reco.GetYaxis().SetRangeUser(0.8,1.24)
        reco.GetXaxis().SetRangeUser(50,100)
        reco.GetYaxis().SetTitle("ratio")
        reco.GetXaxis().SetTitle("m^{W}_{T}[GeV]")
        reco.GetXaxis().SetTitleOffset(1.5)
        reco.GetYaxis().SetTitleSize(0.05)

	hists = []
	hists.append(reco)
	hists.append(reco_W)
	
        legend = makeLegend(hists,0.26, 0.25,0.4,0.4)
	
        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        reco.Draw("P")
	reco_W.Draw("same")
	legend.Draw("same")
        astyle.ATLASLabel(0.25, 0.87, "Internal")
        utils.DrawText(0.25, 0.81, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_BiasPro.pdf")

    def GetEpsilonFactors(self, inputFile, channel, Indice):

        hreco_noFakes   = inputFile.Get("Efficiency_hist")

        hreco_noFakes.SetStats(0)
        hreco_noFakes.SetTitle("")
        hreco_noFakes.SetLineWidth(2)
        hreco_noFakes.SetLineColor(2)
        hreco_noFakes.SetMarkerStyle(10)
        hreco_noFakes.SetMarkerSize(1)
        hreco_noFakes.SetMarkerColor(2)
        hreco_noFakes.GetXaxis().SetRangeUser(50,100)
        hreco_noFakes.GetYaxis().SetRangeUser(0.2,1.2)
        hreco_noFakes.GetYaxis().SetTitle("reconstruction efficiency")
        hreco_noFakes.GetXaxis().SetTitle("m^{W}_{T}[GeV]")
        hreco_noFakes.GetXaxis().SetTitleOffset(1.2)
        hreco_noFakes.GetYaxis().SetTitleSize(0.05)
        hreco_noFakes.GetXaxis().SetTitleSize(0.05)
        hreco_noFakes.GetXaxis().SetLabelSize(0.043)
        hreco_noFakes.GetYaxis().SetLabelSize(0.043)

	print(         hreco_noFakes.GetXaxis().GetLabelSize() )

        #hreco_noFakes.GetXaxis().SetLabelSize(0.05)

        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        hreco_noFakes.Draw("P")
        astyle.ATLASLabel(0.65, 0.87, "Internal")
        utils.DrawText(0.65, 0.81, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_Epsilons.pdf")

    def GetAcceptanceFactors(self, inputFile, channel, Indice):

        hreco_noFakes   = inputFile.Get("Acceptance_hist")

        hreco_noFakes.SetStats(0)
        hreco_noFakes.SetTitle("")
        hreco_noFakes.SetLineWidth(2)
        hreco_noFakes.SetLineColor(2)
        hreco_noFakes.SetMarkerStyle(10)
        hreco_noFakes.SetMarkerSize(1)
        hreco_noFakes.SetMarkerColor(2)
        hreco_noFakes.GetYaxis().SetRangeUser(0.2,1.2)
        hreco_noFakes.GetXaxis().SetRangeUser(50,100)
        hreco_noFakes.GetYaxis().SetTitle("Acceptance efficiency")
        hreco_noFakes.GetXaxis().SetTitle("m^{W}_{T}[GeV]")
        hreco_noFakes.GetXaxis().SetTitleOffset(1.2)
        hreco_noFakes.GetYaxis().SetTitleSize(0.05)
        hreco_noFakes.GetXaxis().SetTitleSize(0.05)
        hreco_noFakes.GetXaxis().SetLabelSize(0.043)
        hreco_noFakes.GetYaxis().SetLabelSize(0.043)

        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        hreco_noFakes.Draw("P")
        astyle.ATLASLabel(0.65, 0.87, "Internal")
        utils.DrawText(0.65, 0.81, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_Acceptance.pdf")

    def MigrationMatrix(self, inputFile, channel, Indice):

        hists = []
        Migration_Matrix = inputFile.Get("mig_hist")

        c2 = root.TCanvas("c2", "The FillRandom example", 0, 0, 800, 600)
        Migration_Matrix.SetStats(0)
        Migration_Matrix.SetTitle("")
        Migration_Matrix.GetXaxis().SetTitle("m^{W}_{T} Detector level [GeV]")
        Migration_Matrix.GetYaxis().SetTitle("m^{W}_{T} Particle level [GeV]")
        Migration_Matrix.GetXaxis().SetRangeUser(50,100)
        Migration_Matrix.GetYaxis().SetRangeUser(50,100)
        Migration_Matrix.GetXaxis().SetTitleOffset(1.3)
	Migration_Matrix.GetZaxis().SetLabelSize(0.04)
	print( Migration_Matrix.GetZaxis().GetLabelSize() )

        Migration_Matrix.Draw("COLZ")
        astyle.ATLASLabel(0.15, 0.92, "Internal")
        utils.DrawText(0.65, 0.92, Indice)
        c2.Update()
        c2.Print("Output/"+channel+"/"+channel+"_MigrationMatrix.pdf")

    def ShowNominalDistribution(self, inputFile, channel, Indice):
        hists = []

        data             = inputFile.Get("dataCorrected")
        data_Unfolded    = inputFile.Get("unfolded_data1")
        Migration_Matrix = inputFile.Get("mig_hist")

	truth_MC         = Migration_Matrix.ProjectionY("truth_MC")
	reco_MC		 = Migration_Matrix.ProjectionX("reco_MC")

        data_Unfolded.SetName('data unfolded')
        truth_MC.SetName('Particle level - MC')
        reco_MC.SetName('Detector level - MC')

        hists.append(data_Unfolded)
        hists.append(truth_MC)
        hists.append(reco_MC)

        reco_MC.SetLineColor(4)
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        compteur = 1
        for hist in hists:
            hist.SetStats(0)
            hist.SetTitle("")
	    if(compteur == 3): compteur = 4
            utils.SetHistogramLine(hist, compteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
	    hist.SetMarkerSize(1)
            hist.SetMarkerColor(hist.GetLineColor())
            hist.GetXaxis().SetTitle("m^{W}_{T} [GeV]")
            hist.GetXaxis().SetRangeUser(50,100)
            hist.GetYaxis().SetRangeUser(4,hist.GetMaximum())
            hist.Draw("HIST same")
            compteur +=1
        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2, 0.76, Indice)
        legend = makeLegend(hists,0.64, 0.65,0.85,0.8)
        legend.Draw("same")
        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_NominalPlots.pdf")

        #define the rapport data/MC

    def CompareBias(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice):
        hists = []
        compteur = NumberOfIterationMinimal
        Colorcompteur = 1
        while compteur < NumberOfIterationMaximal:
            hist = inputFile.Get('Bias_Iter_' + str(compteur))
	    print(hist.GetTitle())
            hist.GetXaxis().SetRangeUser(50,100)
            hist.GetYaxis().SetRangeUser(-6,3)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Bias Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetXaxis().SetTitle("m^{W}_{T} [GeV]")
            hist.GetYaxis().SetTitle("Bias [%]")
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1
        # Draw
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        for hist in hists:
            hist.Draw("same")
        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2, 0.76, Indice)
        legend = makeLegend(hists,0.4, 0.2,0.7,0.6)
        legend.Draw("same")
        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_Bias_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")

    def CompareStatError(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice):
        hists = []
        compteur  = NumberOfIterationMinimal
        Colorcompteur = 1
        while compteur < NumberOfIterationMaximal:
            CovarianceMatrix = inputFile.Get('CovarianceMatrix_Iter' + str(compteur))
            data_Unfolded    = inputFile.Get("unfolded_data"+ str(compteur))
            StatErrorHist    = data_Unfolded.Clone("StatErrorHist")
            j=0
            while j < StatErrorHist.GetNbinsX():
                if(data_Unfolded.GetBinContent(j+1)!=0):
                    #StatErrorHist.SetBinContent(j+1, 100*sqrt(CovarianceMatrix.GetBinContent(j+1,j+1))/data_Unfolded.GetBinContent(j+1))
                    StatErrorHist.SetBinContent(j+1, 100*sqrt(CovarianceMatrix.GetBinContent(j+1,j+1))/data_Unfolded.GetBinContent(j+1))
                    StatErrorHist.SetBinError(j+1, 0)
                j=j+1
            StatErrorHist.GetXaxis().SetRangeUser(50,100)
            StatErrorHist.GetYaxis().SetRangeUser(0,6)
            StatErrorHist.SetStats(0)
            StatErrorHist.SetTitle("")
            StatErrorHist.SetName('Stat Iteration ' +str(compteur))
            StatErrorHist.SetTitle('Stat Iteration ' +str(compteur))
            StatErrorHist.SetMarkerColor(compteur)
            print(compteur)
            StatErrorHist.GetXaxis().SetTitle("m^{W}_{T} [GeV]")
            StatErrorHist.GetYaxis().SetTitle("Stat [%]")
            utils.SetHistogramLine(StatErrorHist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(StatErrorHist)
            Colorcompteur +=1
            compteur +=1
        # Draw
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        for hist in hists:
            hist.SetTitle("")
            hist.Draw("same")
        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2, 0.76, Indice)
        legend = makeLegend(hists,0.25, 0.35,0.75,0.7)
        legend.Draw("same")
        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_StatError_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")
