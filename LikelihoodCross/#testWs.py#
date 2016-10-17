#! /usr/bin/env python

import ROOT
from ROOT import RooStats
#import LikeLihoodCross
#from LikeLihoodCross import* 

import likelihoodCross_proper_class
from likelihoodCross_proper_class import*
## to time the macro
t = ROOT.TStopwatch()
t.Start()

wspace = ROOT.RooWorkspace("w")

#nobs_4m = ROOT.Double(27)        
nobs_4m = 27        
bkg_4m = 0.09        
sigmaBkg_4m = 0.16
			   
nobs_2e2m = 30 
bkg_2e2m = 0.47
sigmaBkg_2e2m = 0.26 
			   			   
nobs_4e = 8 
bkg_4e = 0.44
sigmaBkg_4e = 0.35

eff_4m = 0.844
eff_2e2m = 0.694
eff_4e = 0.60

sigmaEff_4m = 0.0097 
sigmaEff_2e2m = 0.0097 
sigmaEff_4e = 0.0097 

xs_4m =  8.57
xs_2e2m = 17
xs_4e = 8.57
Lumi = 2.568

sigmaEff_4m = 0.0097   
sigmaEff_4e = 0.0097  
sigmaEff_2e2m = 0.0097

wspace.factory("nobs_4m["+str(nobs_4m)+",0,50]")
wspace.factory("nobs_4e["+str(nobs_4e)+",0,50]")
wspace.factory("nobs_2e2m["+str(nobs_2e2m)+",0,50]")


wspace.factory("bkg_4m["+str(bkg_4m)+"]")
wspace.factory("bkg_4e["+str(bkg_4e)+"]")
wspace.factory("bkg_2e2m["+str(bkg_2e2m)+"]")

wspace.factory("bkg0_4m["+str(bkg_4m)+",0,10]")
wspace.factory("bkg0_4e["+str(bkg_4e)+",0,10]")
wspace.factory("bkg0_2e2m["+str(bkg_2e2m)+",0,10]")

wspace.factory("sigmaBkg_4m["+str(sigmaBkg_4m)+"]")
wspace.factory("sigmaBkg_4e["+str(sigmaBkg_4e)+"]")
wspace.factory("sigmaBkg_2e2m["+str(sigmaBkg_2e2m)+"]")

wspace.factory("eff_4m["+str(eff_4m)+"]")
wspace.factory("eff_4e["+str(eff_4e)+"]")
wspace.factory("eff_2e2m["+str(eff_2e2m)+"]")

wspace.factory("eff0_4m["+str(eff_4m)+",0,1]")
wspace.factory("eff0_4e["+str(eff_4e)+",0,1]")
wspace.factory("eff0_2e2m["+str(eff_2e2m)+",0,1]")

wspace.factory("sigmaEff_4m["+  str( sigmaEff_4m )   + "]")
wspace.factory("sigmaEff_2e2m["+ str( sigmaEff_4e )  + "]")
wspace.factory("sigmaEff_4e["+ str( sigmaEff_2e2m )  + "]")

wspace.factory("xs_4m["+str(xs_4m)+",0,30]")
wspace.factory("xs_4e["+str(xs_4e)+",0,30]")
wspace.factory("xs_2e2m["+str(xs_2e2m)+",0,30]")

wspace.factory("Lumi["+str(Lumi)+",0,100]")
#wspace.Print()

cross  = LikeCross(wspace)
print "CROSS",cross
