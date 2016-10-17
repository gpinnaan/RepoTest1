#! /usr/bin/env python

import ROOT
from ROOT import RooStats


## to time the macro
t = ROOT.TStopwatch()
t.Start()

def LikeCross(wspace):
#wspace = ROOT.RooWorkspace("w")


    # b_4m = 0.09        
    sigmaBkg_4m = 0.16
    

    # b_2e2m = 0.47
    sigmaBkg_2e2m = 0.26 
    

    # b_4e = 0.44
    sigmaBkg_4e = 0.35

    
    #  Poisson model * Gaussian constraint
    wspace.factory("prod:s_4m(mu[1.,0.,1000],xs_4m[8.57,0,100],eff_4m[0.5,0.,1.],Lumi)")  
    wspace.factory("prod:s_2e2m(mu[1.,0.,1000],xs_2e2m[17.25,0,100],eff_2e2m[0.5,0.,1.],Lumi)")  
    wspace.factory("prod:s_4e(mu[1.,0.,1000],xs_4e[8.57,0,100],eff_4e[0.5,0.,1.],Lumi)")  
    
    wspace.factory("sum:nexp_4m(s_4m,bkg_4m)")
    wspace.factory("sum:nexp_2e2m(s_2e2m,bkg_2e2m)")
    wspace.factory("sum:nexp_4e(s_4e,bkg_4e)")
        
    wspace.Print()
    
    # wspace.var("bkg_4m").setVal(bkg_4m); DEL
    # Wspace.var("bkg_2e2m").setVal(bkg_2e2m);
    # wspace.var("bkg_4e").setVal(bkg_4e);
    
    # Poisson of (n | s+b)
    wspace.factory("Poisson:pdf_4m(nobs_4m,nexp_4m)")
    wspace.factory("Poisson:pdf_2e2m(nobs_2e2m,nexp_2e2m)")
    wspace.factory("Poisson:pdf_4e(nobs_4e,nexp_4e)")

    wspace.factory("Gaussian:constraint_4m(b0_4m[0,10],bkg_4m,sigmaBkg_4m[1])")
    wspace.factory("Gaussian:constraint_2e2m(b0_2e2m[0,10],bkg_2e2m,sigmaBkg_2e2m[1])")
    wspace.factory("Gaussian:constraint_4e(b0_4e[0,10],bkg_4e,sigmaBkg_4e[1])")
    
    wspace.factory("Gaussian:constraintEff_4m(eff0_4m[0,1],eff_4m,sigmaEff_4m[1])")
    wspace.factory("Gaussian:constraintEff_2e2m(eff0_2e2m[0,1],eff_2e2m,sigmaEff_2e2m[1])")
    wspace.factory("Gaussian:constraintEff_4e(eff0_4e[0,1],eff_4e,sigmaEff_4e[1])")
    
    
    wspace.factory("PROD:model_4m(pdf_4m,constraint_4m,constraintEff_4m)")
    wspace.factory("PROD:model_2e2m(pdf_2e2m,constraint_2e2m,constraintEff_2e2m)")
    wspace.factory("PROD:model_4e(pdf_4e,constraint_4e,constraintEff_4e)")
    
    wspace.factory("PROD:model(model_4m,model_2e2m,model_4e)")
    
    # wspace.var("b0_4m").setVal(bkg_4m)
    # wspace.var("b0_2e2m").setVal(bkg_2e2m)
    # wspace.var("b0_4e").setVal(bkg_4e)
    
    wspace.var("bkg0_4m").setConstant(True)
    wspace.var("bkg0_2e2m").setConstant(True) 
    wspace.var("bkg0_4e").setConstant(True) 
    
    
    #  eff_4m = 0.844*0.5388;
    #  eff_2e2m = 0.694*0.5388;
    #  eff_4e = 0.60*0.5388;
    
    eff_4m = 0.844
    eff_2e2m = 0.694
    eff_4e = 0.60
    
    wspace.var("eff_4m").setVal(eff_4m)
    wspace.var("eff_2e2m").setVal(eff_2e2m)
    wspace.var("eff_4e").setVal(eff_4e)
    
    wspace.var("eff0_4m").setVal(eff_4m)
    wspace.var("eff0_2e2m").setVal(eff_2e2m)
    wspace.var("eff0_4e").setVal(eff_4e)
    
    wspace.var("eff0_4m").setConstant(True) # needed for being treated as global observabls
    wspace.var("eff0_2e2m").setConstant(True) # needed for being treated as global observab
    wspace.var("eff0_4e").setConstant(True) # needed for being treated as global observables
    
    sigmaEff_4m = 0.0097 
    sigmaEff_2e2m = 0.0097 
    sigmaEff_4e = 0.0097 
    
    BRele = 0.03363
    BRmu  = 0.03366  
    
    BR_4m = BRmu*BRmu
    BR_2e2m = 2*BRmu*BRele
    BR_4e = BRele*BRele
    
    BR = BR_4m+BR_2e2m+BR_4e
    
# cout<<"BR sum"<<BR<<" BRmean "<<(BR_4m + BR_4e + BR_2e2m)/3.<<" BR_4m "<<BR_4m<<" BR_2e2m "<<BR_2e2m<<" BR_4e "<<BR_4e<<endl
    
    # wspace.var("BR_4m").setVal(BR_4m)
    # wspace.var("BR_2e2m").setVal(BR_2e2m)
    # wspace.var("BR_4e").setVal(BR_4e)
    
    wspace.var("xs_4m").setConstant(True) # needed for being treated as global observables
    wspace.var("xs_2e2m").setConstant(True) # needed for being treated as global observables
    wspace.var("xs_4e").setConstant(True) # needed for being treated as global observables
    
#    wspace.var("Lumi").setVal(2.568)
    wspace.var("Lumi").setConstant(True) 
    
    wspace.var("sigmaBkg_4m").setVal(sigmaBkg_4m*bkg_4m)  
    wspace.var("sigmaBkg_2e2m").setVal(sigmaBkg_2e2m*bkg_2e2m)  
    wspace.var("sigmaBkg_4e").setVal(sigmaBkg_4e*bkg_4e)  
    
    wspace.var("sigmaEff_4m").setVal(sigmaEff_4m*eff_4m)  
    wspace.var("sigmaEff_2e2m").setVal(sigmaEff_2e2m*eff_2e2m)  
    wspace.var("sigmaEff_4e").setVal(sigmaEff_4e*eff_4e)  
    
    mc = ROOT.RooStats.ModelConfig(ROOT.RooWorkspace())
    mc.SetPdf(wspace.pdf("model"))
    
    mc.SetParametersOfInterest(ROOT.RooArgSet(wspace.var("mu")))
    
    mc.SetObservables(ROOT.RooArgSet(wspace.var("nobs_4m"),wspace.var("nobs_2e2m"),wspace.var("nobs_4e")));  
    
    
    mc.SetNuisanceParameters(ROOT.RooArgSet(wspace.var("bkg_4m"),wspace.var("bkg_2e2m"),wspace.var("bkg_4e"),wspace.var("eff_4m"),wspace.var("eff_2e2m"),wspace.var("eff_4e")))
    
    mc.SetSnapshot(ROOT.RooArgSet(wspace.var("mu")))
    mc.SetGlobalObservables(ROOT.RooArgSet(wspace.var("bkg0_4m"),wspace.var("bkg0_2e2m"),wspace.var("bkg0_4e")))
    
    
  #mc.Print();
  # import model in the workspace 
    getattr(wspace, 'import')(mc)
    
    
# # make data set with the namber of observed events
    data = ROOT.RooDataSet("data","", ROOT.RooArgSet(wspace.var("nobs_4m"),wspace.var("nobs_2e2m"),wspace.var("nobs_4e")));
#   #RooDataSet data("data","", ROOT.RooArgSet(wspace.var("nobs_4m"),wspace.var("nobs_2e2m")));
    
    
#    wspace.var("nobs_4m").setVal(nobs_4m);
    data.add(ROOT.RooArgSet(wspace.var("nobs_4m") ))
    
 #   wspace.var("nobs_2e2m").setVal(nobs_2e2m);
    data.add(ROOT.RooArgSet(wspace.var("nobs_2e2m") ))
    
  #  wspace.var("nobs_4e").setVal(nobs_4e);
    data.add(ROOT.RooArgSet(wspace.var("nobs_4e") ))
    
# # import data set in workspace and save it in a file
    
#fit = wspace.pdf("model").fitTo(data, ROOT.RooFit.Save(True))

    print "Valv",wspace.var("nobs_4m").getValV();
    wspace.Print("t")
    
    pl = ROOT.RooStats.ProfileLikelihoodCalculator(data, mc);
    pl.SetConfidenceLevel(0.68); # 95% interval
    interval = pl.GetInterval();
    
    
    # # print out the iterval on the first Parameter of Interest
#RooRealVar firstPOI = (RooRealVar) mc.GetParametersOfInterest().first();
# cout << "\n68% interval on " <<firstPOI.GetName()<<" is : ["<<
# interval.LowerLimit(firstPOI) << ", "<<
# interval.UpperLimit(firstPOI) <<"] "<<endl;
    
    
#wspace.Print()
    
#Mc = ROOT.RooStats.MCMCCalculator(data, wspace.pdf("model"))
    
    mc.SetPdf(wspace.pdf("model"))
    
    print mc.GetParametersOfInterest().getRealValue("mu")
    print "Cross ",mc.GetParametersOfInterest().getRealValue("mu")*34.34
    print "Total Cross ",(mc.GetParametersOfInterest().getRealValue("mu")*34.34)/(0.5338*BR)

    return mc.GetParametersOfInterest().getRealValue("mu")*34.34
# wspace.import(data);

# wspace.Print();

# TString fileName = "CountingModel.root"; 

# # write workspace in the file (recreate file if already existing)
# wspace.writeToFile(fileName, true);


#wspace.Print()

### print timing info
t.Stop()
t.Print()
