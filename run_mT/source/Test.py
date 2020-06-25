#!/usr/bin/env python
# -*-coding:Latin-1 -*

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TAttFill

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend


class Test:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""

    def Test(self, inputFile, channel, Indice):

        Reco_MC         = inputFile.Get("Reco_MC")
        hreco_noFakes   = inputFile.Get("hreco_noFakes")

        hreco_noFakes.Divide(Reco_MC)

        hreco_noFakes.SetStats(0)
        hreco_noFakes.SetTitle("")
        hreco_noFakes.SetLineWidth(2)
        hreco_noFakes.SetLineColor(2)
        hreco_noFakes.SetMarkerStyle(1)
        hreco_noFakes.SetMarkerSize(20)
        hreco_noFakes.SetMarkerColor(1)
        hreco_noFakes.GetXaxis().SetRangeUser(0,100)
        hreco_noFakes.GetYaxis().SetTitle("reconstruction efficiency")
        hreco_noFakes.GetXaxis().SetTitle("p^{W}_{T}[GeV]")
        hreco_noFakes.GetXaxis().SetTitleOffset(1.5)







        HCrossSection1N.SetMarkerSize(1)
        HCrossSection1N.SetName("Unfolded data")
        HCrossSection1N.SetMarkerStyle(20)
        HCrossSection1N.SetMarkerColor(2)
        HCrossSection1N.SetFillStyle(3001)
        HCrossSection1N.SetFillColor(2)

        TruthPowheg.SetLineWidth(2)
        TruthPowheg.SetLineColor(1)
        TruthPowheg.SetMarkerStyle(1)
        TruthPowheg.SetMarkerColor(1)
        TruthPowheg.SetMarkerSize(1)
        TruthPowheg.SetName("PowhegPythia")

        histsN = []
        histsN.append(HCrossSection1N)
        histsN.append(TruthPowheg)
        legendN = makeLegend(histsN,0.6, 0.6,0.84,0.78)

        astyle.SetAtlasStyle()
        c1N = root.TCanvas("c1N", "The FillRandom example", 0, 0, 800, 600)
        c1N.cd(1)
        c1N.SetLogy()
        HCrossSection1N.GetXaxis().SetRangeUser(0,100)
        HCrossSection1N.SetStats(0)
        HCrossSection1N.SetTitle("")
        HCrossSection1N.GetXaxis().SetTitle("p_{w}^{T}[GeV]")
        HCrossSection1N.GetYaxis().SetTitle("1/#sigma d#sigma / dp_{w}^{T} ")
        HCrossSection1N.GetXaxis().SetTitleOffset(1.5)
        HCrossSection1N.Draw("same E1E5")










        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        hreco_noFakes.Draw("E12")
        astyle.ATLASLabel(0.65, 0.87, "Internal")
        utils.DrawText(0.65, 0.81, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_Test.pdf")
