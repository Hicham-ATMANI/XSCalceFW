#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1

import matplotlib.pyplot as plt
import numpy as np

dataminusenu5  = TFile("/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptwminusenu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Hdataminusenu5 = dataminusenu5.Get("WminusenuSelectionCutFlow")
dataplusenu5  = TFile("/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptwplusenu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Hdataplusenu5 = dataplusenu5.Get("WplusenuSelectionCutFlow")

dataminusmunu5  = TFile("/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptwminusmunu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Hdataminusmunu5 = dataminusmunu5.Get("WminusmunuSelectionCutFlow")
dataplusmunu5  = TFile("/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptwplusmunu_DATA_5TeV/Nominal/data17_WZ_lowMu_repro_5TeV.root")
Hdataplusmunu5 = dataplusmunu5.Get("WplusmunuSelectionCutFlow")


latexFile = open("Selection_5TeV.tex","w+")
latexFile.write("\\documentclass[12pt]{article} \n")
latexFile.write("\\usepackage{amsmath}\n")
latexFile.write("\\usepackage{graphicx}\n")
latexFile.write("\\usepackage{hyperref}\n")
latexFile.write("\\usepackage{hyperref}\n")
latexFile.write("\\usepackage[latin1]{inputenc}\n")
latexFile.write("\\begin{document}\n")
        

latexFile.write("\\begin{table}[]\n")
latexFile.write("\\begin{tabular}{|c|c|l|l|c|c|c|}\n")
latexFile.write("\\hline\n")
latexFile.write("            & \multicolumn{6}{c|}{Channels}                                                                       \\\ \\hline \n")
latexFile.write("Selections  & \multicolumn{3}{c|}{W^{-} \\rightarrow e^{-} \\nu} & W^{+} \\rightarrow e^{+} \\nu & W^{-} \\rightarrow \\mu^{-} \\nu                   & W^{+} \\rightarrow \\mu^{+} \\nu                  \\\ \\hline \n")

latexFile.write(" No cut     & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(1), Hdataplusenu5.GetBinContent(1), Hdataminusmunu5.GetBinContent(1), Hdataplusmunu5.GetBinContent(1)) )
latexFile.write(" Charge     & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(2), Hdataplusenu5.GetBinContent(2), Hdataminusmunu5.GetBinContent(2), Hdataplusmunu5.GetBinContent(2)) )
latexFile.write(" One lepton & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(3), Hdataplusenu5.GetBinContent(3), Hdataminusmunu5.GetBinContent(3), Hdataplusmunu5.GetBinContent(3)) )
latexFile.write(" trigger    & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(4), Hdataplusenu5.GetBinContent(4), Hdataminusmunu5.GetBinContent(4), Hdataplusmunu5.GetBinContent(4)) )
latexFile.write(" Isolation  & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(5), Hdataplusenu5.GetBinContent(5), Hdataminusmunu5.GetBinContent(5), Hdataplusmunu5.GetBinContent(5)) )
latexFile.write(" $p^{T}_{l}>25GeV$      & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(6), Hdataplusenu5.GetBinContent(6), Hdataminusmunu5.GetBinContent(6), Hdataplusmunu5.GetBinContent(6)) )
latexFile.write(" $E^{T}_{miss}>25GeV$   & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(7), Hdataplusenu5.GetBinContent(7), Hdataminusmunu5.GetBinContent(7), Hdataplusmunu5.GetBinContent(7)) )
latexFile.write(" $m^{T}>25GeV$         & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu5.GetBinContent(8), Hdataplusenu5.GetBinContent(8), Hdataminusmunu5.GetBinContent(8), Hdataplusmunu5.GetBinContent(8)) )

latexFile.write("\end{tabular}\n")
latexFile.write("\caption{ Selections table for 5TeV }\n")
latexFile.write("\end{table}\n")
latexFile.write("\\end{document}\n")        
latexFile.close()


dataminusenu13  = TFile("/eos/user/h/hatmani/13TeVInputs/Processing/pTW_Input/pTWanalysis_ptwminusenu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Hdataminusenu13 = dataminusenu13.Get("WminusenuSelectionCutFlow")
dataplusenu13  = TFile("/eos/user/h/hatmani/13TeVInputs/Processing/pTW_Input/pTWanalysis_ptwplusenu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Hdataplusenu13 = dataplusenu13.Get("WplusenuSelectionCutFlow")

dataminusmunu13  = TFile("/eos/user/h/hatmani/13TeVInputs/Processing/pTW_Input/pTWanalysis_ptwminusmunu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Hdataminusmunu13 = dataminusmunu13.Get("WminusmunuSelectionCutFlow")
dataplusmunu13  = TFile("/eos/user/h/hatmani/13TeVInputs/Processing/pTW_Input/pTWanalysis_ptwplusmunu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Hdataplusmunu13 = dataplusmunu13.Get("WplusmunuSelectionCutFlow")



latexFile = open("Selection_13TeV.tex","w+")
latexFile.write("\\documentclass[12pt]{article} \n")
latexFile.write("\\usepackage{amsmath}\n")
latexFile.write("\\usepackage{graphicx}\n")
latexFile.write("\\usepackage{hyperref}\n")
latexFile.write("\\usepackage{hyperref}\n")
latexFile.write("\\usepackage[latin1]{inputenc}\n")
latexFile.write("\\begin{document}\n")


latexFile.write("\\begin{table}[]\n")
latexFile.write("\\begin{tabular}{|c|c|l|l|c|c|c|}\n")
latexFile.write("\\hline\n")
latexFile.write("            & \multicolumn{6}{c|}{Channels}                                                                       \\\ \\hline \n")
latexFile.write("Selections  & \multicolumn{3}{c|}{W^{-} \\rightarrow e^{-} \\nu} & W^{+} \\rightarrow e^{+} \\nu & W^{-} \\rightarrow \\mu^{-} \\nu                   & W^{+} \\rightarrow \\mu^{+} \\nu                  \\\ \\hline \n")

latexFile.write(" No cut     & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(1), Hdataplusenu13.GetBinContent(1), Hdataminusmunu13.GetBinContent(1), Hdataplusmunu13.GetBinContent(1)) )
latexFile.write(" Charge     & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(2), Hdataplusenu13.GetBinContent(2), Hdataminusmunu13.GetBinContent(2), Hdataplusmunu13.GetBinContent(2)) )
latexFile.write(" One lepton & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(3), Hdataplusenu13.GetBinContent(3), Hdataminusmunu13.GetBinContent(3), Hdataplusmunu13.GetBinContent(3)) )
latexFile.write(" trigger    & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(4), Hdataplusenu13.GetBinContent(4), Hdataminusmunu13.GetBinContent(4), Hdataplusmunu13.GetBinContent(4)) )
latexFile.write(" Isolation  & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(5), Hdataplusenu13.GetBinContent(5), Hdataminusmunu13.GetBinContent(5), Hdataplusmunu13.GetBinContent(5)) )
latexFile.write(" $p^{T}_{l}>25GeV$      & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(6), Hdataplusenu13.GetBinContent(6), Hdataminusmunu13.GetBinContent(6), Hdataplusmunu13.GetBinContent(6)) )
latexFile.write(" $E^{T}_{miss}>25GeV$   & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(7), Hdataplusenu13.GetBinContent(7), Hdataminusmunu13.GetBinContent(7), Hdataplusmunu13.GetBinContent(7)) )
latexFile.write(" $m^{T}>25GeV$         & \multicolumn{3}{c|}{ %d}   &  %d   &   %d   &  %d   \\\ \\hline \n" %(Hdataminusenu13.GetBinContent(8), Hdataplusenu13.GetBinContent(8), Hdataminusmunu13.GetBinContent(8), Hdataplusmunu13.GetBinContent(8)) )

latexFile.write("\end{tabular}\n")
latexFile.write("\caption{ Selections table for 13TeV }\n")
latexFile.write("\end{table}\n")


latexFile.write("\\end{document}\n")        
latexFile.close()

