#!/usr/bin/env python
# -*-coding:Latin-1 -*
#import atlasplots
#from   atlasplots import atlas_style as astyle
#from   atlasplots import utils
#from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TAttFill
from ROOT import gStyle

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend


class Plot2D:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""


    def StatCovarianceMatrix(self, inputFile, Iter, channel, Indice, Energy):
        hists = []

        StatCovMatrix   = inputFile.Get("CovarianceMatrix_Iter"+str(Iter))
        StatCovMatrixN  = inputFile.Get("CovarianceMatrix_Iter"+str(Iter))
        StatCorrMatrix  = StatCovMatrix.Clone("StatCorrMatrix")

        for i in range(0,StatCovMatrix.GetNbinsX()):
            for j in range(0,StatCovMatrix.GetNbinsX()):
                StatCovMatrixN.SetBinContent(i+1, j+1, StatCovMatrix.GetBinContent(i+1,j+1))
                StatCovMatrixN.SetBinError(i+1, j+1, StatCovMatrix.GetBinError(i+1, j+1))
                if(StatCovMatrix.GetBinContent(i+1,i+1) != 0 and StatCovMatrix.GetBinContent(j+1,j+1) != 0):
                     StatCorrMatrix.SetBinContent(i+1, j+1, StatCovMatrix.GetBinContent(i+1,j+1) / (sqrt(StatCovMatrix.GetBinContent(i+1,i+1)*StatCovMatrix.GetBinContent(j+1,j+1))) )
                     StatCorrMatrix.SetBinError(i+1, j+1, StatCovMatrix.GetBinError(i+1))
                else:
                    StatCorrMatrix.SetBinContent(i, j, 0 )
                    StatCorrMatrix.SetBinError(i, j, 0 )

        StatCorrMatrix.SetName('Correlation Matrix')
        StatCorrMatrix.SetStats(0)
        StatCorrMatrix.SetTitle("")
        StatCorrMatrix.GetXaxis().SetTitle("p^{l}_{T} [GeV]")
        StatCorrMatrix.GetYaxis().SetTitle("p^{l}_{T} [GeV]")
        StatCorrMatrix.GetXaxis().SetRangeUser(25,60)
        StatCorrMatrix.GetYaxis().SetRangeUser(25,60)

        StatCorrMatrix.GetYaxis().SetTitleOffset(1)


        StatCorrMatrix.GetXaxis().SetLabelSize(0.045)
        StatCorrMatrix.GetXaxis().SetTitleSize(0.045)
        StatCorrMatrix.GetYaxis().SetLabelSize(0.045)
        StatCorrMatrix.GetYaxis().SetTitleSize(0.045)
        StatCorrMatrix.SetName('Covariance Matrix')
        StatCorrMatrix.SetStats(0)
        StatCorrMatrix.SetTitle("")
 
	#gROOT.SetStyle("ATLAS")
        c1 = root.TCanvas("c1", "CorrelationMatrix", 0, 0, 800, 600)
        gStyle.SetPaintTextFormat("4.2f")
        StatCorrMatrix.Draw("colz")
        gStyle.SetPaintTextFormat("4.2f")

	l = root.TLatex()
    	l.SetNDC()
    	l.SetTextColor(1)
    	l.DrawLatex(0.15, 0.92, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.55, 0.92, r"#bf{#it{ATLAS}} " + Indice)

        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_Stat_CorrMatrix_Iter_"+str(Iter)+"_"+Energy+".pdf")

    def BiasCovarianceMatrix(self, Bias, Iter, channel, Indice, Energy):
        hists = []

        BiasCovMatrix   = Bias.Get("CovMatrix_Iter_"+str(Iter))
        BiasCorrMatrix  = BiasCovMatrix.Clone("BiasCorrMatrix")

        for i in range(0,BiasCovMatrix.GetNbinsX()):
            for j in range(0,BiasCovMatrix.GetNbinsX()):
                if(BiasCovMatrix.GetBinContent(i+1,i+1) != 0 and BiasCovMatrix.GetBinContent(j+1,j+1) != 0):
                     BiasCorrMatrix.SetBinContent(i+1, j+1, BiasCovMatrix.GetBinContent(i+1,j+1) / (sqrt(BiasCovMatrix.GetBinContent(i+1,i+1)*BiasCovMatrix.GetBinContent(j+1,j+1))) )
                     BiasCorrMatrix.SetBinError(i+1, j+1,   BiasCovMatrix.GetBinError(i+1))
                else:
                    BiasCorrMatrix.SetBinContent(i+1, j+1, 0 )
                    BiasCorrMatrix.SetBinError(i+1, j+1, 0 )


        BiasCorrMatrix.SetName('Covariance_Matrix1')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")
        BiasCorrMatrix.GetXaxis().SetTitle("p^{l}_{T} [GeV]")
        BiasCorrMatrix.GetYaxis().SetTitle("p^{l}_{T} [GeV]")
        BiasCorrMatrix.GetXaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetYaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetXaxis().SetLabelSize(0.045) 
        BiasCorrMatrix.GetXaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetLabelSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleOffset(1)
        BiasCorrMatrix.SetName('Covariance Matrix')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")

        #BiasCorrMatrix.GetZaxis().SetRangeUser(0.1,1)
        #gROOT.SetStyle("ATLAS")

        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")


        l = root.TLatex()
        l.SetNDC()
        l.SetTextColor(1)
        l.DrawLatex(0.15, 0.92, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.55, 0.92, r"#bf{#it{ATLAS}} " + Indice)

        c1.Print("Output/"+channel+"/"+channel+"_Bias_CorrMatrix_Iter_"+str(Iter)+"_"+Energy+".pdf")


    def SystCovarianceMatrix(self, Bias, Iter, channel, Indice, Energy):
        hists = []

        BiasCovMatrix   = Bias.Get("ElRecoSys_Covariance_Iter"+str(Iter))
        BiasCorrMatrix  = BiasCovMatrix.Clone("BiasCorrMatrix")

        for i in range(0,BiasCovMatrix.GetNbinsX()):
            for j in range(0,BiasCovMatrix.GetNbinsX()):
                if(BiasCovMatrix.GetBinContent(i+1,i+1) != 0 and BiasCovMatrix.GetBinContent(j+1,j+1) != 0):
                     BiasCorrMatrix.SetBinContent(i+1, j+1, BiasCovMatrix.GetBinContent(i+1,j+1) / (sqrt(BiasCovMatrix.GetBinContent(i+1,i+1)*BiasCovMatrix.GetBinContent(j+1,j+1))) )
                     BiasCorrMatrix.SetBinError(i+1, j+1,   BiasCovMatrix.GetBinError(i+1))
                else:
                    BiasCorrMatrix.SetBinContent(i+1, j+1, 0 )
                    BiasCorrMatrix.SetBinError(i+1, j+1, 0 )


        BiasCorrMatrix.SetName('Covariance_Matrix1')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")
        BiasCorrMatrix.GetXaxis().SetTitle("p^{l}_{T} [GeV]")
        BiasCorrMatrix.GetYaxis().SetTitle("p^{l}_{T} [GeV]")
        BiasCorrMatrix.GetXaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetYaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetXaxis().SetLabelSize(0.045)
        BiasCorrMatrix.GetXaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetLabelSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleOffset(1)
        BiasCorrMatrix.SetName('Covariance Matrix')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")

        #BiasCorrMatrix.GetZaxis().SetRangeUser(0.1,1)
        #gROOT.SetStyle("ATLAS")

        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")


        l = root.TLatex()
        l.SetNDC()
        l.SetTextColor(1)
        l.DrawLatex(0.15, 0.92, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.55, 0.92, r"#bf{#it{ATLAS}} " + Indice)

        c1.Print("Output/"+channel+"/"+channel+"_Syst_CorrMatrix_Iter_"+str(Iter)+"_"+Energy+".pdf")


