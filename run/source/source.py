#!/usr/bin/env python
# -*-coding:Latin-1 -* 

import ROOT
import ROOT as root
from   math import *

from ROOT import TFile, TH1F, TH2F, TCanvas, TPad, TLegend, gStyle, gROOT, gPad, gDirectory, TVector2, TPaveStats, TStyle, TLatex
from ROOT import TColor, kBlack, kRed, kBlue, kMagenta, kYellow, kCyan, kGreen, kOrange, kTeal, kPink, kGray
from ROOT import TArrayD, TAxis, TMath, TVectorF, TMatrixF, TF1, TH2D, TH1D
from ROOT import kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from ROOT import RooUnfoldSvd
from root_numpy import *


def GetTheRecoilVariation(Charge, Energy):

        RecoilSystVariation = []
    
	RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varSET_SYSbin1.root'))
        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_SYS_DOWNbin1.root'))
        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
        RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))
	
	for i in range(1, 20):
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))
	
        for i in range(1, 12):
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
            RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

        return RecoilSystVariation



def GetTheCalibVariation(Charge, Energy):

	CalibSystVariation = []

	for i in range(1, 25):
            CalibSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/ElCalibVar/Merge/mc16_'+str(Energy)+'TeV.varscaleDownbin'+str(i)+'.root'))

        for i in range(1, 25):
            CalibSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/5TeVInputs/Processing/pTW_Input/pTWanalysis_ptw'+ Charge+'_MC_'+str(Energy)+'TeV/ElCalibVar/Merge/mc16_'+str(Energy)+'TeV.varcDownbin'+str(i)+'.root'))
	
	return CalibSystVariation

def GetDevSystematic(reco_hist, reco_Varied, mig_hist, responseM, itera):

        reco_hist_Eff    = GetEfficieny(mig_hist, reco_hist) 
	reco_Varied_Eff  = GetEfficieny(mig_hist, reco_Varied)

	responseM        = RooUnfoldResponse(0,0,mig_hist,"UNFOLD","UNFOLD");
	
        unfoldMC         = RooUnfoldBayes (responseM, reco_hist_Eff,   itera)
	HistNominal      = unfoldMC.Hreco()

	unfoldMC_Var     = RooUnfoldBayes (responseM, reco_Varied_Eff, itera)	
	HistVaried	 = unfoldMC_Var.Hreco()

	CovarianceMatrix = SysCovarianc( HistNominal, HistVaried)

	return CovarianceMatrix

def SysCovarianc( HistoNominal, unfoldedSys_down):

        ntbins   = HistoNominal.GetNbinsX()
        xaxis    = HistoNominal.GetXaxis()

        Covariance = TH2D("CovarianceMatrix", "CovarianceMatrix", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())

        for j in range(1, 1 + HistoNominal.GetNbinsX()):
            for k in range(1, 1 + HistoNominal.GetNbinsX()):
                Covariance.SetBinContent(j, k, (unfoldedSys_down.GetBinContent(j)-HistoNominal.GetBinContent(j))*(unfoldedSys_down.GetBinContent(k)-HistoNominal.GetBinContent(k)))	

	return Covariance
	
def SumCovarianceMatrix( CalibCovarianceMatrix ):
	
	CovarianceTotal = (CalibCovarianceMatrix[0]).Clone("CovarianceTotal")

	print("nomber of event",len(CalibCovarianceMatrix))
        for j in range(1, 1 + CovarianceTotal.GetNbinsX()):
            for k in range(1, 1 + CovarianceTotal.GetNbinsX()):
		CovarianceTotal.SetBinContent(j, k, 0)
		
        for i in range(1, 1 + CovarianceTotal.GetNbinsX()):
            for j in range(1, 1 + CovarianceTotal.GetNbinsX()):
		covsum = 0
		for k in range(0, len(CalibCovarianceMatrix) ):
	    	    covsum = covsum + CalibCovarianceMatrix[k].GetBinContent(i,j)
		CovarianceTotal.SetBinContent(i, j, covsum)
		
	return CovarianceTotal		

def GetPrinSystematic( CalibVariationFiles, reco_hist, mig_hist, Channel, Energy, Variable, Niter, VarMin, VarMax, Muon, Syst):

	CalibVariation = []
        CalibVariation_Eff = []

	FileName = Variable
        if( Variable == "WpT" ):
                Variable = Variable + "_Reco"

	for i in range(0, len( CalibVariationFiles )):
	    CalibVariation.append( CalibVariationFiles[i].Get( Channel + "Selection/"+Variable+"_cut7"))
	
        # Add variation to Nominal and apply efficiency corrections:
        for i in range(0, len( CalibVariation )):
            CalibVariation_Eff.append(ApplyEffecciency( CalibVariation[i], reco_hist, mig_hist))
	    print(CalibVariationFiles[i].GetName(),  CalibVariation[i].Integral() - reco_hist.Integral())
	
        # correct the reco distribution:
        reco_hist_Eff = (mig_hist.ProjectionX()).Clone("reco_hist_Eff")

        # define the response matrix for Syst unfo
        response_Syst = RooUnfoldResponse(0, 0, mig_hist, "UNFOLD", "UNFOLD");

        # Calculate the Syst:
        Systematics    = []
        CovarianceIter = []

        for i in range(1, 1 + Niter ):

            unfoldMCNominal  = RooUnfoldBayes (response_Syst, reco_hist_Eff, i)
            HistoNominal     = unfoldMCNominal.Hreco()

            unfoldedSys_down = GetUnfoldToys(response_Syst, CalibVariation_Eff, i)
            Systematic_down  = GetSystematics(HistoNominal, unfoldedSys_down)
            Covariance       = GetSystCovarianceMatrix(HistoNominal, unfoldedSys_down, mig_hist, Variable)

            Systematic_down.GetXaxis().SetRangeUser(VarMin, VarMax)
            Covariance.GetXaxis().SetRangeUser(VarMin, VarMax)
            Covariance.GetYaxis().SetRangeUser(VarMin, VarMax)
            CovarianceIter.append(Covariance)
            Systematics.append(Systematic_down)


        OutputFile = TFile("output_"+Channel+str(Energy)+"/"+FileName+"/"+Syst+"_Syst.root",'RECREATE')
        for i in range(1, Niter):
                Systematics[i].Write( Syst + "_Systematics_Iter"+str(i))
                CovarianceIter[i].Write( Syst + "_Covariance_Iter"+str(i))

        return Systematics
	
def GetSFSystematic(InputSyst, reco_hist, mig_hist, Channel, Energy, Variable, Syst, Niter, VarMin, VarMax, Muon):

	# read the variation from the input files:
	Variation_1D_down     = []
	Variation_1D_down_Eff = []
        Variation_2D_down     = []

	DireName       = Channel + "Selection_WeightVariations"
	Hist1DName     = "WpT_Reco_v_Truth_" + str(Energy) + "TeV_cut7"
	Hist2DName     = "WpT_Reco_cut7"
	
 	directory 	= InputSyst.GetDirectory( DireName )

        for key in directory.GetListOfKeys():
            hist = key.ReadObj()
	    if ((hist.GetName()).find("sumEt") == -1 and (hist.GetName()).find("coarseHigh") == -1 and (hist.GetName()).find("SF") == -1 and (hist.GetName()).find("eta") == -1 and (hist.GetName()).find('_down') != -1 ):
               if ( hist.ClassName() == 'TH1F' and (hist.GetName()).find(Variable) != -1 and (hist.GetName()).find(Syst) != -1 ):
		  print(hist.GetName())
		  Variation_1D_down.append(hist)
	
	# Add variation to Nominal and apply efficiency corrections:
	for i in range(0, len( Variation_1D_down )):
            Variation_1D_down[i].Add(reco_hist)
	    Variation_1D_down_Eff.append(ApplyEffecciency(Variation_1D_down[i], reco_hist, mig_hist))
	        	
	# Get reco, migration, data with Syst File
	reco_Syst     = RecoDistribution( InputSyst, Channel, Variable, 0)
	mig_hist_Syst = MigrationMatrix(  InputSyst, Channel, str(Energy), Variable, mig_hist)

	# correct the reco distribution:
	reco_hist_Eff = (mig_hist.ProjectionX()).Clone("reco_hist_Eff")

	# define the response matrix for Syst unfo
	response_Syst = RooUnfoldResponse(0, 0, mig_hist, "UNFOLD", "UNFOLD");	

	# Calculate the Syst:
	Systematics    = []
	CovarianceIter = []

	for i in range(1, 1 + Niter ):	

	    unfoldMCNominal  = RooUnfoldBayes (response_Syst, reco_hist_Eff, i)	
	    HistoNominal     = unfoldMCNominal.Hreco()
		
	    unfoldedSys_down = GetUnfoldToys(response_Syst, Variation_1D_down_Eff, i)
	    Systematic_down  = GetSystematics(HistoNominal, unfoldedSys_down)	
	    print(" difference ", HistoNominal.GetName(), unfoldedSys_down[0].GetName() )
            Covariance	     = GetSystCovarianceMatrix(HistoNominal, unfoldedSys_down, mig_hist, Variable)
	
            Systematic_down.GetXaxis().SetRangeUser(VarMin, VarMax)
	    Covariance.GetXaxis().SetRangeUser(VarMin, VarMax)
            Covariance.GetYaxis().SetRangeUser(VarMin, VarMax)
	    CovarianceIter.append(Covariance)
	    Systematics.append(Systematic_down)


	
	OutputFile = TFile("output_"+Channel+str(Energy)+"/"+Variable+"/Syst_" + Syst + ".root",'RECREATE')
	for i in range(1, Niter):
    		Systematics[i].Write( Syst + "_Systematics_Iter"+str(i))
		CovarianceIter[i].Write( Syst + "_Covariance_Iter"+str(i))
	
	return Systematics
	

def GetSystCovarianceMatrix( HistoNominal, unfoldedSys_down, mig_hist, Variable):

	CovarianceTot    = []

        ntbins   = HistoNominal.GetNbinsX()
        xaxis    = HistoNominal.GetXaxis()
      
        if(Variable != "WpT"):
	    CovarianceMatrix = mig_hist.Clone("CovarianceMatrix")
	    CovarianceSumme  = mig_hist.Clone("CovarianceSumme")
            CovMatrix = mig_hist.Clone("CovMatrix")
        if(Variable == "WpT"):
            CovarianceMatrix = TH2D("CovarianceMatrix", "CovarianceMatrix", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
            CovarianceSumme  = TH2D("CovarianceSumme", "CovarianceSumme", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())

	for i in range(0, len(unfoldedSys_down) ):		
	    Covariance = 0
	    CovarianceMatIter = CovarianceMatrix.Clone("CovarianceMatIter")
	    for j in range(1, 1 + HistoNominal.GetNbinsX()):
		for k in range(1, 1 + HistoNominal.GetNbinsX()):
		    Covariance = ( unfoldedSys_down[i].GetBinContent(j) - HistoNominal.GetBinContent(j) )*( unfoldedSys_down[i].GetBinContent(k) - HistoNominal.GetBinContent(k) )
		    CovarianceMatIter.SetBinContent(j, k, Covariance)	
	    CovarianceTot.append(CovarianceMatIter)
	    
	for i in range(1, 1 + HistoNominal.GetNbinsX()):
            for j in range(1, 1 + HistoNominal.GetNbinsX()):	    
		Covariance = 0
        	for k in range(0, len(CovarianceTot) ):
		    Covariance = Covariance + CovarianceTot[k].GetBinContent(i,j)
	        CovarianceSumme.SetBinContent(i, j, Covariance)
		print("Covariance element %f"%Covariance)
	return CovarianceSumme

def GetSystematics( HistoNominal, unfoldedSys_down):
		
	HistSyst = HistoNominal.Clone("HistSyst")
	
	for i in range(1, 1 + HistoNominal.GetNbinsX()):
	    difference = 0
	    for j in range(0, len(unfoldedSys_down) ):
		if( HistoNominal.GetBinContent(i) != 0):
	            difference = difference + pow( (( unfoldedSys_down[j].GetBinContent(i) - HistoNominal.GetBinContent(i)) / HistoNominal.GetBinContent(i)), 2)
	    HistSyst.SetBinContent(i, 100*sqrt(difference))
	    HistSyst.SetBinError(i, 0)
	return HistSyst

def ApplyEffecciency( data_hist, reco_hist, mig_hist):

	data_hist_Corr = data_hist.Clone("data_hist_Corr")

        Efficiency_hist = (mig_hist.ProjectionX()).Clone("Efficiency_hist")
        Efficiency_hist.Divide(reco_hist)

        for i in range(1, 1 + reco_hist.GetNbinsX()):
	    data_hist_Corr.SetBinContent(i, data_hist.GetBinContent(i)*Efficiency_hist.GetBinContent(i) )	
        return data_hist_Corr
	

def GetCovarianceMatrix(unfoldDATA, UnfoldToys, VarMin, VarMax, Variable, mig_hist):

	ntbins   = unfoldDATA.GetNbinsX()
	xaxis    = unfoldDATA.GetXaxis()

        if(Variable != "WpT"):
            CovMatrix = mig_hist.Clone("CovMatrix")
        if(Variable == "WpT"):
            CovMatrix = TH2D("Covariance", "Covariance" , ntbins,  xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
	
	for i in range(1, 1 + ntbins ):
	    for j in range(1, 1 + ntbins ):
		MatrixValue = 0
		for k in range(0, len( UnfoldToys )):
		    MatrixValue = MatrixValue + ( (UnfoldToys[k].GetBinContent(i) - unfoldDATA.GetBinContent(i)) * (UnfoldToys[k].GetBinContent(j) - unfoldDATA.GetBinContent(j)) )
		CovMatrix.SetBinContent(i, j, MatrixValue/len(UnfoldToys))
		CovMatrix.GetXaxis().SetRangeUser(VarMin, VarMax)
                CovMatrix.GetYaxis().SetRangeUser(VarMin, VarMax)

	return CovMatrix		


def GetUnfoldToys(responseM, ToysOfData, Niter):
	UnfoldToys = []

	for i in range(0, len(ToysOfData)):
	    unfoldToy = RooUnfoldBayes (responseM, ToysOfData[i], Niter)
            UnfoldToys.append( (unfoldToy.Hreco()).Clone() )


	return UnfoldToys

def GetToysofData(fInput_Data_BS, Channel, Variable, Energy):
	ToysOfData = []
	director =  fInput_Data_BS.GetDirectory( Channel+"Selection_WeightVariations" )

	if(Variable == "WpT"): Variable = Variable + "_Reco"

        if(Variable == "MuPt" and Channel.find("munu") != -1 ):
                Variable = "muPt"

        for key in director.GetListOfKeys():
            hist = key.ReadObj()
            if hist.ClassName() == 'TH1F' :
                if not ((hist.GetName()).find( Variable + "_cut7_toy")):
		       #print(hist.GetName())
                       ToysOfData.append(hist)
	return ToysOfData

def GetTheBias(responseM, dataCorrected, mig_hist, Niteration, VarMin, VarMax, Channel, Energy, Variable):

	# clone the nominal plots
	Migration	    = mig_hist.Clone("Response")
	truth_hist 	    = (mig_hist.ProjectionY()).Clone("truth_hist")
        truth_hist_Weighted = (mig_hist.ProjectionY()).Clone("truth_hist_Weighted")
	reco_hist	    = (mig_hist.ProjectionX()).Clone("reco_hist")
        reco_hist_Weighted  = (mig_hist.ProjectionX()).Clone("reco_hist_Weighted")
  	Response     	    = mig_hist.Clone("Response")

	RatioData  	    = dataCorrected.Clone("RatioData")
	RatioMC	   	    = (mig_hist.ProjectionX()).Clone("RatioMC")
	Bias       	    = (mig_hist.ProjectionY()).Clone("Bias")
	
	# fit the ratio data/MC
	RatioData.Divide(RatioMC)
	f1 = TF1("f1","pol7", VarMin, VarMax)
	RatioData.Fit("f1")

	# reweight the truth distributions:
	for i in range(1, 1 + truth_hist.GetNbinsX()):
	      binC = truth_hist.GetXaxis().GetBinCenter(i)
	      print((f1.Eval( binC ) ))
	      truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f1.Eval( binC ) ) )
	      truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
	      #print("Bin i: %d,  truth_Weighted: %f"%(i, truth_hist_Weighted.GetBinContent(i)))
	
	# calculate the response matrix:
	for i in range(1, 1 + reco_hist.GetNbinsX()):
	    for j in range(1, 1 + truth_hist.GetNbinsX()):
		if( truth_hist.GetBinContent(j) != 0): Response.SetBinContent(i, j, mig_hist.GetBinContent(i,j) / truth_hist.GetBinContent(j) )
                if( truth_hist.GetBinContent(j) == 0): Response.SetBinContent(i, j, mig_hist.GetBinContent(i,j) )
	
	# calculte the reco_weighted
        for i in range(1, 1 + reco_hist.GetNbinsX()):
	    ElemV = 0
	    for j in range(1, 1 + truth_hist.GetNbinsX()):
	  	ElemV = ElemV + Response.GetBinContent(i, j) * truth_hist_Weighted.GetBinContent(j)
	
	    reco_hist_Weighted.SetBinContent(i, ElemV)		
            reco_hist_Weighted.SetBinError(i,   reco_hist.GetBinError(i)) 
	
	# define the covariance matrix:
	ntbins = truth_hist_Weighted.GetNbinsX()
	xaxis  = truth_hist_Weighted.GetXaxis()
        print(truth_hist.Integral(), ntbins)
	print(ntbins, xaxis, xaxis.GetXbins().GetArray())
	if(Variable != "WpT"):
	    CovMatrix = mig_hist.Clone("CovMatrix")
	if(Variable == "WpT"):
	    CovMatrix = TH2D("Covariance", "Covariance" , ntbins,  xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
        print(" ligne 2 ")

	# define the response matrix:
	responseMN = RooUnfoldResponse(0, 0, Migration, "UNFOLD", "UNFOLD");

	# define the output:
	OutputFile = TFile("output_"+Channel+str(Energy)+"/"+Variable+"/Bias_"+Channel+str(Energy)+".root",'RECREATE')
	truth_hist.Write("truth_hist")
	truth_hist_Weighted.Write("truth_hist_Weighted")
	reco_hist.Write("reco_hist")
	reco_hist_Weighted.Write("reco_hist_Weighted")
	
	reco_Weighted = reco_hist_Weighted.Clone("reco_Weighted")

	# Calculate the Bias
	for i in range(1, 1 + Niteration):

	    unfoldMC = RooUnfoldBayes (responseMN, reco_Weighted, i)
    	    #unfoldMC = RooUnfoldSvd  (responseMN, reco_Weighted, i);

	    UnfoldHisto = unfoldMC.Hreco()

	    Bias.Add( UnfoldHisto, truth_hist_Weighted, 1, -1)

            for j in range(1, 1 + truth_hist.GetNbinsX()):
                for k in range(1, 1 + truth_hist.GetNbinsX()):
                    CovMatrix.SetBinContent(j, k, Bias.GetBinContent(j)*Bias.GetBinContent(k))

            for j in range(1, 1 + truth_hist.GetNbinsX()):
                if( truth_hist_Weighted.GetBinContent(j) != 0 ):
                    Bias.SetBinContent( j,100*Bias.GetBinContent(j) / truth_hist_Weighted.GetBinContent(j) )
                    Bias.SetBinError(j,0)

            Bias.GetXaxis().SetRangeUser(VarMin, VarMax)
            CovMatrix.GetXaxis().SetRangeUser(VarMin, VarMax)
            CovMatrix.GetYaxis().SetRangeUser(VarMin, VarMax)
            Bias.Write("Bias_Iter_"+str(i))
            CovMatrix.Write("CovMatrix_Iter_"+str(i))
	
def SumBackground(Input_Bkgd1, Input_Bkgd2, Input_Bkgd3, Input_Bkgd5, Input_Bkgd4, Channel, Var ):

	Background_W        = Input_Bkgd1.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Z        = Input_Bkgd2.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Dilepton = Input_Bkgd3.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Top      = Input_Bkgd5.Get(  Channel + "Selection/" +  Var + "_cut7" )

	if( Var == "WpT_Reco" ): Var = Var + "_cut7";
	if( Var == "MuPt"     ): Var = "muPt"

	Background_Mj       = Input_Bkgd4.Get(  "hist/" + Var )

	print(Background_W.GetNbinsX())
	print(Background_Z.GetNbinsX())
	print(Background_Dilepton.GetNbinsX())
	print(Background_Top.GetNbinsX())
	print(Background_Mj.GetNbinsX())

	Background_Total    = Background_W.Clone("Background_Total")
	Background_Total.Add(Background_Z)
	Background_Total.Add(Background_Dilepton)
	Background_Total.Add(Background_Top)
	Background_Total.Add(Background_Mj)

	print("Sum the background ditributions: Done")
	return Background_Total


def MigrationMatrix( fInput_MC, Channel, Energy, Var, truth):
	if( Var == "elEta" ):
        	Migration = fInput_MC.Get( Channel + "Selection/el_Eta_Reco_v_Truth_cut7")
		
        	ntbins   = truth.GetNbinsX()
        	xaxis    = truth.GetXaxis()

            	mig_hist = TH2D("mig_hist", "mig_hist" , ntbins,  xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
	
		for i in range(1, 1+mig_hist.GetNbinsX() ):
                    for j in range(1, 1+mig_hist.GetNbinsX() ):
		    	mig_hist.SetBinContent(i, j, Migration.GetBinContent(i, j))

	elif ( Var == "WpT" ):
        	mig_hist      = fInput_MC.Get( Channel + "Selection/WpT_Reco_v_Truth_"+ str(Energy)  +"TeV_cut7")
	else :
		mig_hist      = fInput_MC.Get( Channel + "Selection/"+Var+"_Reco_v_Truth_cut7")

        print("Get the migration Matrix: Done")

        return mig_hist


def TruthDistribution( fInput_MC, Var, Energy):
	if( Var == "WpT" ):
        	truth_hist    = fInput_MC.Get( "TruthSelection/"+ Var +"_Truth_" + str(Energy) + "TeV_cut4" )
	else:
        	truth_hist    = fInput_MC.Get( "TruthSelection/"+ Var +"_Truth_cut4" )
        print("Get the Truth Distribution: Done")
	return truth_hist


def RecoDistribution( fInput_MC, Channel, Var, indice):
        if( Var == "WpT" ): 
		Var = Var + "_Reco"	
	if(indice == 1 and Channel.find("munu") != -1 ): 
		Var = "muPt"

        reco_hist     = fInput_MC.Get( Channel + "Selection/"+ Var + "_cut7" )

        print("Get the Reco Distribution: Done")
	return reco_hist

def GetAcceptance( mig_hist, truth_hist):
	Acceptance_hist = (mig_hist.ProjectionY()).Clone("Acceptance_hist")
	Acceptance_hist.Divide(truth_hist)
	print("Get the Acceptance Corrections: Done")
	return Acceptance_hist

def GetEfficieny( mig_hist, reco_hist):
        Efficiency_hist = (mig_hist.ProjectionX()).Clone("Efficiency_hist")
        Efficiency_hist.Divide(reco_hist)
        print("Get the Efficiency Corrections: Done")
        return Efficiency_hist

def CorrectData( data_hist, reco_hist, Background_Total, Efficiency_hist):

	dataCorrected = data_hist.Clone("dataCorrected")

	for i in range(1, 1 + reco_hist.GetNbinsX()):
	    if(reco_hist.GetBinContent(i) != 0):
	   	rapportBGMC = (Background_Total.GetBinContent(i) / (reco_hist.GetBinContent(i)+Background_Total.GetBinContent(i)))
		dataCorrected.SetBinContent(i, data_hist.GetBinContent(i)*(1-rapportBGMC))

	for i in range(1, 1 + dataCorrected.GetNbinsX()):
	    dataCorrected.SetBinContent(i, dataCorrected.GetBinContent(i)*Efficiency_hist.GetBinContent(i) )

        print("Correct data and subtract background: Done")

	return dataCorrected
