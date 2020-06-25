#!/usr/bin/env python
# -*-coding:Latin-1 -* 

import ROOT
import ROOT as root
from   math import *

from ROOT import TFile, TH1F, TH2F, TCanvas, TPad, TLegend, gStyle, gROOT, gPad, gDirectory, TVector2, TPaveStats, TStyle, TLatex
from ROOT import TColor, kBlack, kRed, kBlue, kMagenta, kYellow, kCyan, kGreen, kOrange, kTeal, kPink, kGray
from ROOT import TArrayD, TGaxis, TAxis, TMath, TVectorF, TMatrixF, TF1, TH2D, TH1D
from ROOT import kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal, TLine

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from root_numpy import *
from array import array

    
def BackgroundPlotsetalepton(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy):

        if(channel == "Wplusmunu" or channel == "Wminusmunu" ):
            lepton = "muEtaSF"
        else:
            lepton = "elEta"

        Nsignal                 = Signal.Get(channel+'Selection/'+lepton+'_cut7')                # Signal
        Ndata                   = data.Get(channel+'Selection/'+lepton+'_cut7')                  # Data

        print("Nombre de bins de MC : ",Nsignal.GetNbinsX())
        print("Nombre de bins de data : ",Ndata.GetNbinsX())

        NBackgroundW            = Background_W.Get(channel+'Selection/'+lepton+'_cut7')          # background "W"
        NBackgroundZ            = Background_Z.Get(channel+'Selection/'+lepton+'_cut7')          # background "Z"
        NBackgroundDiboson      = Background_diboson.Get(channel+'Selection/'+lepton+'_cut7')    # background "diboson"
        NBackgroundTop          = Background_Top.Get(channel+'Selection/'+lepton+'_cut7')        # background "Top"
        NBackgroundMultijet     = Background_MiltiJet.Get('eTaLepton')                           # background "Miltijet"

        if(lepton == "elEta"):
                RecoBin = [-2.5, -2.18, -1.95, -1.74, -1.52, -1.37, -1.05, -0.84, -0.63, -0.42, -0.21, 0.0, 0.21, 0.42, 0.63, 0.84, 1.05, 1.37, 1.52, 1.74, 1.95, 2.18, 2.5]
        if(lepton == "muEtaSF"):
                RecoBin = [-2.4, -1.918, -1.348, -1.1479, -1.05,  -0.908, -0.476, 0, 0.476, 0.908, 1.05, 1.1479, 1.348, 1.918, 2.4]

        # Make a Clone of hists
        Hdata               = TH1F("Hdata",                 "data",                 len(RecoBin)-1, array('d',RecoBin))     # data
        Hsignal             = TH1F("Hsignal1",              "signal",               len(RecoBin)-1, array('d',RecoBin))   # Signal
        HBackgroundW        = TH1F("NBackgroundW",          "Background_W",         len(RecoBin)-1, array('d',RecoBin))    # W+-
        HBackgroundZ        = TH1F("HBackgroundZ",          "Background_Z",         len(RecoBin)-1, array('d',RecoBin))    # Z+-
        HBackgroundDiboson  = TH1F("HBackgroundDiboson",    "Background_Diboson",   len(RecoBin)-1, array('d',RecoBin))   # diboson
        HBackgroundMultijet = TH1F("HBackgroundMultijet",   "Background_Multijet",  len(RecoBin)-1, array('d',RecoBin))     # MJ
        HBackgroundTop      = TH1F("HBackgroundTop",        "Background_Top",       len(RecoBin)-1, array('d',RecoBin))     # Top
        Hratio1             = TH1F("Hratio1",               "ratio",                len(RecoBin)-1, array('d',RecoBin))     # ratio



        for i in range(1, len(RecoBin)):


            Hdata.SetBinContent(i,                  Ndata.GetBinContent(i))

            Hsignal.SetBinContent(i,                Nsignal.GetBinContent(i))
            Hsignal.SetBinError(i,                  Nsignal.GetBinError(i))

            HBackgroundW.SetBinContent(i,           NBackgroundW.GetBinContent(i))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ.GetBinContent(i))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson.GetBinContent(i))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop.GetBinContent(i))
            HBackgroundMultijet.SetBinContent(i, NBackgroundMultijet.GetBinContent(i))

            Hratio1.SetBinContent(i,                Ndata.GetBinContent(i))
            Hratio1.SetBinError(i,                  Ndata.GetBinError(i))
            i=i+1

        # MC Total
        Hsignal.SetLineColor(2)
        Hsignal.SetLineWidth(2)
        Hsignal.SetLineStyle(2)

        MCTotal = Hsignal.Clone("MCTotal")
        MCTotal.Add(HBackgroundDiboson)
        MCTotal.Add(HBackgroundTop)
        MCTotal.Add(HBackgroundMultijet)
        MCTotal.Add(HBackgroundW)
        MCTotal.Add(HBackgroundZ)
        MCTotal.SetMarkerSize(0)

        # Ratio Plot
        Nratio1 =  Hdata.Clone("Nratio1")

        print("Nombre de bins de data : ",Nratio1.GetNbinsX())
        print("Nombre de bins de MC : ",Hsignal.GetNbinsX())

        # Hist Syle
        ColorParameter(HBackgroundW, 1001, 2, 1, 1)
        ColorParameter(HBackgroundZ, 1001, 4, 1, 1)
        ColorParameter(HBackgroundDiboson, 1001, 209, 1, 1)
        ColorParameter(HBackgroundMultijet, 1001, 93, 1, 1)
        ColorParameter(HBackgroundTop, 1001, 53, 1, 1)


        Legend = ROOT.TLegend(0.4,0.75,0.7,0.85)
        Legend.AddEntry(Hdata,"Data");
        Legend.AddEntry(MCTotal,"Signal + Background");

        Legend2 = ROOT.TLegend(0.72,0.7,0.93,0.9)
        Legend2.AddEntry(HBackgroundW,"W^{+-} #rightarrow l^{+-}v","f");
        Legend2.AddEntry(HBackgroundZ,"Z #rightarrow ll","f");
        Legend2.AddEntry(HBackgroundDiboson,"Diboson","f");
        Legend2.AddEntry(HBackgroundMultijet,"Multijet","f");
        Legend2.AddEntry(HBackgroundTop,"Top","f");

        Legend.SetBorderSize(0)
        Legend2.SetBorderSize(0)


        # Tline
        line1 = ROOT.TLine(-2.4,0.95,2.4,0.95)
        line2 = ROOT.TLine(-2.4,1.05,2.4,1.05)
        line3 = ROOT.TLine(-2.4,1.,2.4,1.)

        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(2)

        # TStack
        BackgroundPlot = ROOT.THStack("ss","")
        BackgroundPlot.Add(HBackgroundDiboson)
        BackgroundPlot.Add(HBackgroundTop)
        BackgroundPlot.Add(HBackgroundMultijet)
        BackgroundPlot.Add(HBackgroundZ)
        BackgroundPlot.Add(HBackgroundW)
        BackgroundPlot.Add(Hsignal)

        # Draw
        astyle.SetAtlasStyle()
        c = TCanvas("c", "canvas", 800, 700)
        pad1 = TPad("pad1", "pad1", 0, 0.32, 1, 1.0)
        pad1.SetBottomMargin(0);
        pad1.Draw();
        pad1.SetLogy()
        pad1.cd();
        Hdata.SetStats(0)
        Hdata.SetName("")
        Hdata.SetTitle("")
        Hdata.SetLineWidth(0)

        Hdata.SetMarkerSize(1)
        Hdata.SetMarkerStyle(20)
        Hdata.SetMarkerColor(1)
        Hdata.GetYaxis().SetTitle("Events")
        Hdata.GetYaxis().SetTitleOffset(0.8)
        Hdata.GetYaxis().SetTitleSize(0.06)
        Hdata.GetYaxis().SetLabelSize(0.05)
        Hdata.SetMinimum(1.4)
        Hdata.SetMaximum(1000000)
        Hdata.Draw("same P")
        MCTotal.SetLineStyle(1)
        MCTotal.SetLineWidth(2)
        MCTotal.Draw("same HIST")
        BackgroundPlot.Draw("same")
        Legend.Draw("same")
        Legend2.Draw("same")
        astyle.ATLASLabel(0.2, 0.87, "Internal")
        utils.DrawText(0.2, 0.82, Indice)

        c.Update()

        c.cd();
        pad2 = TPad("pad2", "pad2", 0, 0., 1, 0.3)
        pad2.SetTopMargin(0);
        pad2.SetBottomMargin(0.4);
        pad2.SetFrameBorderSize(2);
        pad2.Draw();
        pad2.cd();
        #Nratio1.GetXaxis().SetRangeUser(0,200)
        Nratio1.GetYaxis().SetRangeUser(0.892,1.108)
        Nratio1.GetXaxis().SetLabelSize(0.12)
        Nratio1.GetYaxis().SetLabelSize(0.12)
        Nratio1.GetXaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().CenterTitle()
        Nratio1.GetYaxis().SetTitleOffset(0.5)
        Nratio1.GetYaxis().SetTitleSize(0.12)
        Nratio1.GetXaxis().SetTitleSize(0.14)
        Nratio1.GetXaxis().SetLabelOffset(0.04)
        Nratio1.GetXaxis().SetTitleOffset(1.3)
        Nratio1.SetTitle("")
        Nratio1.Divide(MCTotal)
        Nratio1.SetLineColor(1)
        Nratio1.SetMarkerStyle(20)
        Nratio1.SetMarkerSize(1.2)
        Nratio1.SetLineWidth(2)
        Nratio1.SetStats(0)
        Nratio1.GetXaxis().SetTitle("#eta^{lepton}")
        Nratio1.GetYaxis().SetTitle("Data/MC")
        Nratio1.Draw("P")
        line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")
        c.Print("Migration_2D_"+Channel+".pdf")


def PlotMigrationMatrix(Matrixs, Channel):
	

	Migration = TH2F("Migration", "Migration", 132, 0, 132, 132, 0, 132)
	
	Nbin =  Matrixs[0].GetNbinsX()

        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]


	
	print(Nbin)
	print(Matrixs[3].GetName())


	for k in range(0, 6):
	    for i in range(0, Nbin):
            	for j in range(k*Nbin, (k+1)*Nbin):
		    Migration.SetBinContent(i,j, Matrixs[k].GetBinContent(i,j-k*Nbin))
	
        for k in range(0, 6):
            for i in range(Nbin, 2*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
	            Migration.SetBinContent(i,j, Matrixs[6+k].GetBinContent(i-Nbin,j-k*Nbin))
	
        for k in range(0, 6):
            for i in range(2*Nbin, 3*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[12+k].GetBinContent(i-2*Nbin,j-k*Nbin))

        for k in range(0, 6):
            for i in range(3*Nbin, 4*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[18+k].GetBinContent(i-3*Nbin,j-k*Nbin))

        for k in range(0, 6):
            for i in range(4*Nbin, 5*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[24+k].GetBinContent(i-4*Nbin,j-k*Nbin))

        for k in range(0, 6):
            for i in range(5*Nbin, 6*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[30+k].GetBinContent(i-5*Nbin,j-k*Nbin))

	Xaxis = Migration.GetXaxis()
        Yaxis = Migration.GetYaxis()

	gROOT.SetStyle("ATLAS")
        c1 = TCanvas("C","canvas",1024,640)
	c1.cd()
	Migration.SetName("")        
	Migration.SetTitle("")
        Migration.GetXaxis().SetLabelSize(0.04)
	Migration.GetYaxis().SetLabelSize(0.04)
	Migration.GetZaxis().SetRangeUser(0.5,4600)
	Migration.SetStats(0)
	Migration.Draw("colz") 

        line1 = TLine(0, 22,  132, 22);
        line2 = TLine(0, 44,  132, 44);
        line3 = TLine(0, 66,  132, 66);
        line4 = TLine(0, 88,  132, 88);
        line5 = TLine(0, 110, 132, 110);


        line11 = TLine(22,  0,  22, 132);
        line22 = TLine(44,  0,  44, 132);
        line33 = TLine(66,  0,  66, 132);
        line44 = TLine(88,  0,  88, 132);
        line55 = TLine(110, 0, 110, 132);

        line1.SetLineWidth(1)
        line2.SetLineWidth(1)
        line3.SetLineWidth(1)
        line4.SetLineWidth(1)
        line5.SetLineWidth(1)

        line11.SetLineWidth(1)
        line22.SetLineWidth(1)
        line33.SetLineWidth(1)
        line44.SetLineWidth(1)
        line55.SetLineWidth(1)

        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(2)
        line4.SetLineStyle(2)
        line5.SetLineStyle(2)

        line11.SetLineStyle(2)
        line22.SetLineStyle(2)
        line33.SetLineStyle(2)
        line44.SetLineStyle(2)
        line55.SetLineStyle(2)

        line11.Draw("same")
        line22.Draw("same")
        line33.Draw("same")
        line44.Draw("same")
        line55.Draw("same")

	line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")
        line4.Draw("same")
        line5.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);
        latex.DrawLatex(4,  -15,"25<p^{l}_{reco}<30");
        latex.DrawLatex(26, -15,"30<p^{l}_{reco}<35");
        latex.DrawLatex(49, -15,"35<p^{l}_{reco}<40");
        latex.DrawLatex(71, -15,"40<p^{l}_{reco}<45");
        latex.DrawLatex(93, -15,"45<p^{l}_{reco}<50");
        latex.DrawLatex(115,-15,"50<p^{l}_{reco}<100");

        latex.DrawLatex(-23, 10,   "25<p^{l}_{truth}<30");
        latex.DrawLatex(-23, 30,  "30<p^{l}_{truth}<35");
        latex.DrawLatex(-23, 53,  "35<p^{l}_{truth}<40");
        latex.DrawLatex(-23, 76,  "40<p^{l}_{truth}<45");
        latex.DrawLatex(-23, 96,  "45<p^{l}_{truth}<50");
        latex.DrawLatex(-23, 115, "50<p^{l}_{truth}<100");

	Migration.GetXaxis().SetTitle("#eta_{reco} ")
        Migration.GetYaxis().SetTitle("#eta_{truth} ")
	print(Migration.GetXaxis().GetTitleOffset())
	Migration.GetXaxis().SetTitleOffset(2.4)

        for i in range(0, Migration.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))                    
             Yaxis.SetBinLabel(i,str(Binning[i]))


	c1.Print("Migration_2D_"+Channel+".pdf")

def DataDistribution2d(fInput_MC):

        truth  = TH1F("truth", "data", 132, 0, 132)
	truth1 = []

        truth1.append(fInput_MC.Get("WminusenuSelection/el_Eta_pt1_cut7"))
        truth1.append(fInput_MC.Get("WminusenuSelection/el_Eta_pt2_cut7"))
        truth1.append(fInput_MC.Get("WminusenuSelection/el_Eta_pt3_cut7"))
        truth1.append(fInput_MC.Get("WminusenuSelection/el_Eta_pt4_cut7"))
        truth1.append(fInput_MC.Get("WminusenuSelection/el_Eta_pt5_cut7"))
        truth1.append(fInput_MC.Get("WminusenuSelection/el_Eta_pt6_cut7"))
        Nbin =  truth1[0].GetNbinsX()

        RecoBin = [-2.5, -2.18, -1.95, -1.74, -1.52, -1.37, -1.05, -0.84, -0.63, -0.42, -0.21, 0.0, 0.21, 0.42, 0.63, 0.84, 1.05, 1.37, 1.52, 1.74, 1.95, 2.18, 2.5]


        for i in range(0 , Nbin):
                truth.SetBinContent(i+1,  truth1[0].GetBinContent(i+1 - 0*Nbin))
                truth.SetBinError(i+1,    truth1[0].GetBinError(i+1   - 0*Nbin))

        for i in range(1*Nbin , 2*Nbin):
                truth.SetBinContent(i+1,  truth1[1].GetBinContent(i+1 - 1*Nbin))
                truth.SetBinError(i+1,    truth1[1].GetBinError(i+1   - 1*Nbin))

        for i in range(2*Nbin , 3*Nbin):
                truth.SetBinContent(i+1,  truth1[2].GetBinContent(i+1 - 2*Nbin))
                truth.SetBinError(i+1,    truth1[2].GetBinError(i+1   - 2*Nbin))

        for i in range(3*Nbin , 4*Nbin):
                truth.SetBinContent(i+1,  truth1[3].GetBinContent(i+1 - 3*Nbin))
                truth.SetBinError(i+1,    truth1[3].GetBinError(i+1   - 3*Nbin))

        for i in range(4*Nbin , 5*Nbin):
                truth.SetBinContent(i+1,  truth1[4].GetBinContent(i+1 - 4*Nbin))
                truth.SetBinError(i+1,    truth1[4].GetBinError(i+1   - 4*Nbin))

        for i in range(5*Nbin , 6*Nbin):
                truth.SetBinContent(i+1,  truth1[5].GetBinContent(i+1 - 5*Nbin))
                truth.SetBinError(i+1,    truth1[5].GetBinError(i+1   - 5*Nbin))

        return truth


def TruthDistribution2d(fInput_MC):
		        
	truth  = TH1F("truth", "truth", 132, 0, 132)    
	truth1 = []

	truth1.append(fInput_MC.Get("TruthSelection/EleTa_Truth_pt1_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/EleTa_Truth_pt2_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/EleTa_Truth_pt3_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/EleTa_Truth_pt4_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/EleTa_Truth_pt5_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/EleTa_Truth_pt6_cut4"))        
	Nbin =  truth1[0].GetNbinsX()

	        
	RecoBin = [-2.5, -2.18, -1.95, -1.74, -1.52, -1.37, -1.05, -0.84, -0.63, -0.42, -0.21, 0.0, 0.21, 0.42, 0.63, 0.84, 1.05, 1.37, 1.52, 1.74, 1.95, 2.18, 2.5]
	
	for i in range(0 , Nbin):
	    	truth.SetBinContent(i+1,  truth1[0].GetBinContent(i+1 - 0*Nbin))
	    	truth.SetBinError(i+1,    truth1[0].GetBinError(i+1   - 0*Nbin))

        for i in range(1*Nbin , 2*Nbin):
                truth.SetBinContent(i+1,  truth1[1].GetBinContent(i+1 - 1*Nbin))
                truth.SetBinError(i+1,    truth1[1].GetBinError(i+1   - 1*Nbin))

        for i in range(2*Nbin , 3*Nbin):
                truth.SetBinContent(i+1,  truth1[2].GetBinContent(i+1 - 2*Nbin))
                truth.SetBinError(i+1,    truth1[2].GetBinError(i+1   - 2*Nbin))

        for i in range(3*Nbin , 4*Nbin):
                truth.SetBinContent(i+1,  truth1[3].GetBinContent(i+1 - 3*Nbin))
                truth.SetBinError(i+1,    truth1[3].GetBinError(i+1   - 3*Nbin))

        for i in range(4*Nbin , 5*Nbin):
                truth.SetBinContent(i+1,  truth1[4].GetBinContent(i+1 - 4*Nbin))
                truth.SetBinError(i+1,    truth1[4].GetBinError(i+1   - 4*Nbin))

        for i in range(5*Nbin , 6*Nbin):
                truth.SetBinContent(i+1,  truth1[5].GetBinContent(i+1 - 5*Nbin))
                truth.SetBinError(i+1,    truth1[5].GetBinError(i+1   - 5*Nbin))

	return truth


def MigrationMatrix2d(Matrixs):

        Migration = TH2F("Migration", "Migration", 132, 0, 132, 132, 0, 132)
        Nbin =  Matrixs[0].GetNbinsX()
	print("Matrix binini :",Nbin)
        for k in range(0, 6):
            for i in range(0, Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k].GetBinContent(i+1,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(Nbin, 2*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[6+k].GetBinContent(i+1-Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(2*Nbin, 3*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[12+k].GetBinContent(i+1-2*Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(3*Nbin, 4*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[18+k].GetBinContent(i+1-3*Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(4*Nbin, 5*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[24+k].GetBinContent(i+1-4*Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(5*Nbin, 6*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[30+k].GetBinContent(i+1-5*Nbin,j+1-k*Nbin))

	return Migration

def GetTheMigrationMatrix(Inputs):
	
        Tpad = []

        for i in range(1, 7):
            Tpad.append(Inputs.Get("WminusenuSelection/el_Eta_Reco_v_Truth_pt1pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get("WminusenuSelection/el_Eta_Reco_v_Truth_pt2pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get("WminusenuSelection/el_Eta_Reco_v_Truth_pt3pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get("WminusenuSelection/el_Eta_Reco_v_Truth_pt4pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get("WminusenuSelection/el_Eta_Reco_v_Truth_pt5pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get("WminusenuSelection/el_Eta_Reco_v_Truth_pt6pt"+str(i)+"_cut7"))

	for i in range(0, len(Tpad)):
		print(i, Tpad[i].GetName())
	
        print(" return the 2d migration matrix ")

	return Tpad

