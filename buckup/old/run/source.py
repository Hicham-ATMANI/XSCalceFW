#!/usr/bin/env python
# -*-coding:Latin-1 -* 

import ROOT
import ROOT as root

def SumBackground(Input_Bkgd1, Input_Bkgd2, Input_Bkgd3, Input_Bkgd5, Input_Bkgd4, Channel, Var ):

	print("      Sum the background ditributions    ")

	Background_W        = Input_Bkgd1.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Z        = Input_Bkgd2.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Dilepton = Input_Bkgd3.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Top      = Input_Bkgd5.Get(  Channel + "Selection/" +  Var + "_cut7" )
	Background_Mj       = Input_Bkgd4.Get(  "hist/" +  Var + "_cut7" )

	Background_Total    = Background_W.Clone("Background_Total")
	Background_Total.Add(Background_Z)
	Background_Total.Add(Background_Dilepton)
	Background_Total.Add(Background_Top)
	Background_Total.Add(Background_Mj)

	return Background_Total

def GetSelectionsPlots():
	print("fffff")
