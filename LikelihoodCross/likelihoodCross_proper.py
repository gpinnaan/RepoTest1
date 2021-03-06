#! /usr/bin/env python

import ROOT
from ROOT import RooStats


## to time the macro
t = ROOT.TStopwatch()
t.Start()

wspace = ROOT.RooWorkspace("w")

nobs_4m = ROOT.Double(27)        
b_4m = 0.09        
sigmab_4m = 0.16
			   
nobs_2e2m = ROOT.Double(30) 
b_2e2m = 0.47
sigmab_2e2m = 0.26 
			   			   
nobs_4e = ROOT.Double(8) 
b_4e = 0.44
sigmab_4e = 0.35


#  make Poisson model * Gaussian constraint
wspace.factory("prod:s_4m(mu[1.,0.,1000],xs_4m[8.57,0,100],Acc_4m[0.5,0.,1.],Lumi[2.568,0.,10000])")  
wspace.factory("prod:s_2e2m(mu[1.,0.,1000],xs_2e2m[17.25,0,100],Acc_2e2m[0.5,0.,1.],Lumi[2.568,0.,10000])")  
wspace.factory("prod:s_4e(mu[1.,0.,1000],xs_4e[8.57,0,100],Acc_4e[0.5,0.,1.],Lumi[2.568,0.,10000])")  

wspace.factory("sum:nexp_4m(s_4m,b_4m[1,0,10])")
wspace.factory("sum:nexp_2e2m(s_2e2m,b_2e2m[1,0,10])")
wspace.factory("sum:nexp_4e(s_4e,b_4e[1,0,10])")

wspace.Print()

wspace.var("b_4m").setVal(b_4m);
wspace.var("b_2e2m").setVal(b_2e2m);
wspace.var("b_4e").setVal(b_4e);

#Poisson of (n | s+b)
wspace.factory("Poisson:pdf_4m(nobs_4m[27,0,50],nexp_4m)")
wspace.factory("Poisson:pdf_2e2m(nobs_2e2m[30,0,50],nexp_2e2m)")
wspace.factory("Poisson:pdf_4e(nobs_4e[8,0,50],nexp_4e)")

wspace.factory("Gaussian:constraint_4m(b0_4m[0,10],b_4m,sigmab_4m[1])")
wspace.factory("Gaussian:constraint_2e2m(b0_2e2m[0,10],b_2e2m,sigmab_2e2m[1])")
wspace.factory("Gaussian:constraint_4e(b0_4e[0,10],b_4e,sigmab_4e[1])")

wspace.factory("Gaussian:constraintAcc_4m(Acc0_4m[0,1],Acc_4m,sigmaAcc_4m[1])")
wspace.factory("Gaussian:constraintAcc_2e2m(Acc0_2e2m[0,1],Acc_2e2m,sigmaAcc_2e2m[1])")
wspace.factory("Gaussian:constraintAcc_4e(Acc0_4e[0,1],Acc_4e,sigmaAcc_4e[1])")


wspace.factory("PROD:model_4m(pdf_4m,constraint_4m,constraintAcc_4m)")
wspace.factory("PROD:model_2e2m(pdf_2e2m,constraint_2e2m,constraintAcc_2e2m)")
wspace.factory("PROD:model_4e(pdf_4e,constraint_4e,constraintAcc_4e)")

wspace.factory("PROD:model(model_4m,model_2e2m,model_4e)")

wspace.var("b0_4m").setVal(b_4m)
wspace.var("b0_2e2m").setVal(b_2e2m)
wspace.var("b0_4e").setVal(b_4e)

wspace.var("b_4m").setConstant(True)
wspace.var("b_2e2m").setConstant(True) 
wspace.var("b_4e").setConstant(True) 


 #  Acc_4m = 0.844*0.5388;
 #  Acc_2e2m = 0.694*0.5388;
 #  Acc_4e = 0.60*0.5388;

Acc_4m = 0.844
Acc_2e2m = 0.694
Acc_4e = 0.60

wspace.var("Acc_4m").setVal(Acc_4m)
wspace.var("Acc_2e2m").setVal(Acc_2e2m)
wspace.var("Acc_4e").setVal(Acc_4e)

wspace.var("Acc0_4m").setVal(Acc_4m)
wspace.var("Acc0_2e2m").setVal(Acc_2e2m)
wspace.var("Acc0_4e").setVal(Acc_4e)

wspace.var("Acc_4m").setConstant(True) # needed for being treated as global observables
wspace.var("Acc_2e2m").setConstant(True) # needed for being treated as global observables
wspace.var("Acc_4e").setConstant(True) # needed for being treated as global observables

sigmaAcc_4m = 0.0097 
sigmaAcc_2e2m = 0.0097 
sigmaAcc_4e = 0.0097 

BRele = 0.03363
BRmu  = 0.03366  

BR_4m = BRmu*BRmu
BR_2e2m = 2*BRmu*BRele
BR_4e = BRele*BRele

BR = BR_4m+BR_2e2m+BR_4e

print "BR sum",BR," BRmean ",(BR_4m + BR_4e + BR_2e2m)/3.," BR_4m ",BR_4m," BR_2e2m ",BR_2e2m," BR_4e ",BR_4e

# wspace.var("BR_4m").setVal(BR_4m)
# wspace.var("BR_2e2m").setVal(BR_2e2m)
# wspace.var("BR_4e").setVal(BR_4e)

wspace.var("xs_4m").setConstant(True) # needed for being treated as global observables
wspace.var("xs_2e2m").setConstant(True) # needed for being treated as global observables
wspace.var("xs_4e").setConstant(True) # needed for being treated as global observables

wspace.var("Lumi").setVal(2.568)
wspace.var("Lumi").setConstant(True) 

wspace.var("sigmab_4m").setVal(sigmab_4m)  
wspace.var("sigmab_2e2m").setVal(sigmab_2e2m)  
wspace.var("sigmab_4e").setVal(sigmab_4e)  

wspace.var("sigmaAcc_4m").setVal(sigmaAcc_4m)  
wspace.var("sigmaAcc_2e2m").setVal(sigmaAcc_2e2m)  
wspace.var("sigmaAcc_4e").setVal(sigmaAcc_4e)  

wspace.defineSet("obs","nobs_4m,nobs_4e,nobs_2e2m")  #observables
wspace.defineSet("poi","mu"); #parameters of interest
wspace.defineSet("np","b_4m,b_4e,b_2e2m,Acc_4m,Acc_4e,Acc_2e2m") #nuisance_lumi


wspace.var("nobs_4m").setVal(nobs_4m);
wspace.var("nobs_2e2m").setVal(nobs_2e2m);
wspace.var("nobs_4e").setVal(nobs_4e);

wspace.Print()

CloseVar=input("digit anything you want to end the script \n")        

# # make data set with the namber of observed events
data = ROOT.RooDataSet("data","", ROOT.RooArgSet(wspace.var("nobs_4m"),wspace.var("nobs_2e2m"),wspace.var("nobs_4e")));


data.add(ROOT.RooArgSet(wspace.var("nobs_4m") ))
data.add(ROOT.RooArgSet(wspace.var("nobs_2e2m") ))
data.add(ROOT.RooArgSet(wspace.var("nobs_4e") ))


frame = wspace.var("mu").frame(0.95,1.1);

nll = wspace.pdf("model").createNLL(data)
nll.plotOn(frame,ROOT.RooFit.ShiftToZero()); #the ShiftToZero option puts the minimum at 0 on the y-axis

mini = ROOT.RooMinuit(nll);
mini.minos(wspace.set("poi"));


pll = nll.createProfile(wspace.set("poi"))
pll.plotOn(frame,ROOT.RooFit.LineColor(ROOT.kRed))

frame.SetMaximum(1.) 
frame.Draw()



mu = wspace.var("mu").getValV()
mu_hi = wspace.var("mu").getErrorHi()
mu_lo = wspace.var("mu").getErrorLo()
print "mu",mu,"cross",mu*34.34,"+",(mu+mu_hi)*34.34,"-",(mu+mu_lo)*34.34
print "Total Cross ",(mu*34.34)/(0.5338*BR)

CloseVar=input("digit anything you want to end the script \n")        


# import data set in workspace and save it in a file

#fit = wspace.pdf("model").fitTo(data, ROOT.RooFit.Save(True))

#wspace.Print("t")


#pl = ROOT.RooStats.ProfileLikelihoodCalculator(data, mc);
#pl.SetConfidenceLevel(0.68); # 95% interval
#interval = pl.GetInterval();


# # print out the iterval on the first Parameter of Interest
#RooRealVar firstPOI = (RooRealVar) mc.GetParametersOfInterest().first();
# cout << "\n68% interval on " <<firstPOI.GetName()<<" is : ["<<
# interval.LowerLimit(firstPOI) << ", "<<
# interval.UpperLimit(firstPOI) <<"] "<<endl;


#wspace.Print()

#Mc = ROOT.RooStats.MCMCCalculator(data, wspace.pdf("model"))

#mc.SetPdf(wspace.pdf("model"))

# print mc.GetParametersOfInterest().getRealValue("mu")
# print "Cross ",mc.GetParametersOfInterest().getRealValue("mu")*34.34
# print "Total Cross ",(mc.GetParametersOfInterest().getRealValue("mu")*34.34)/(0.5338*BR)

# wspace.import(data);

# wspace.Print();

# TString fileName = "CountingModel.root"; 

# # write workspace in the file (recreate file if already existing)
# wspace.writeToFile(fileName, true);


#wspace.Print()

### print timing info
t.Stop()
t.Print()
