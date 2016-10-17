using namespace RooFit;
using namespace RooStats;


void LikeLihood(           int nobs_4m = 27,           // number of observed events
			   double b_4m = 0.09,           // number of background events
			   double sigmab_4m = 0.16,     // relative uncertainty in b 1

			   Float_t Eff_4m = 0.844,
			   Float_t Acc_4m = 0.538,
			   
			   int nobs_2e2m = 30,           // number of observed events
			   double b_2e2m = 0.47,           // number of background events
			   double sigmab_2e2m = 0.26,    // relative uncertainty in b 2

			   Float_t Eff_2e2m = 0.694,
			   Float_t Acc_2e2m = 0.538,
			   			   
			   int nobs_4e = 8,           // number of observed events
			   double b_4e = 0.44,           // number of background events
			   double sigmab_4e = 0.35,    // relative uncertainty in b 2


			   Float_t Eff_4e = 0.60,
			   Float_t Acc_4e = 0.538,
			   float Lumi = 2.56 )
{
  RooWorkspace w("w");
  
  // make Poisson model * Gaussian constraint
  w.factory("prod:s_4m(mu[1,0.,1000],xs_4m[8.57,0,100],Eff_4m[0.5,0.,1.],Lumi[2.56,0.,10000])");  
  w.factory("prod:s_2e2m(mu[1,0.,1000],xs_2e2m[17.25,0,100],Eff_2e2m[0.5,0.,1.],Lumi[2.56,0.,10000])");  
  w.factory("prod:s_4e(mu[1,0.,1000],xs_4e[8.57,0,100],Eff_4e[0.5,0.,1.],Lumi[2.56,0.,10000])");  

  w.factory("sum:nexp_4m(s_4m,b_4m[1,0,10])");
  w.factory("sum:nexp_2e2m(s_2e2m,b_2e2m[1,0,10])");
  w.factory("sum:nexp_4e(s_4e,b_4e[1,0,10])");
  
  w.var("b_4m")->setVal(b_4m);
  w.var("b_2e2m")->setVal(b_2e2m);
  w.var("b_4e")->setVal(b_4e);

  // Poisson of (n | s+b)
  w.factory("Poisson:pdf_4m(nobs_4m[0,50],nexp_4m)");
  w.factory("Poisson:pdf_2e2m(nobs_2e2m[0,50],nexp_2e2m)");
  w.factory("Poisson:pdf_4e(nobs_4e[0,50],nexp_4e)");

  w.factory("Gaussian:constraint_4m(b0_4m[0,10],b_4m,sigmab_4m[1])");
  w.factory("Gaussian:constraint_2e2m(b0_2e2m[0,10],b_2e2m,sigmab_2e2m[1])");
  w.factory("Gaussian:constraint_4e(b0_4e[0,10],b_4e,sigmab_4e[1])");

  w.factory("Gaussian:constraintEff_4m(Eff0_4m[0,1],Eff_4m,sigmaEff_4m[1])");
  w.factory("Gaussian:constraintEff_2e2m(Eff0_2e2m[0,1],Eff_2e2m,sigmaEff_2e2m[1])");
  w.factory("Gaussian:constraintEff_4e(Eff0_4e[0,1],Eff_4e,sigmaEff_4e[1])");


  w.factory("PROD:model_4m(pdf_4m,constraint_4m,constraintEff_4m)");
  w.factory("PROD:model_2e2m(pdf_2e2m,constraint_2e2m,constraintEff_2e2m)");
  w.factory("PROD:model_4e(pdf_4e,constraint_4e,constraintEff_4e)");

  w.factory("PROD:model(model_4m,model_2e2m,model_4e)");

  w.var("b0_4m")->setVal(b_4m);
  w.var("b0_2e2m")->setVal(b_2e2m);
  w.var("b0_4e")->setVal(b_4e);

  w.var("b0_4m")->setConstant(true); // needed for being treated as global observables
  w.var("b0_2e2m")->setConstant(true); // needed for being treated as global observables
  w.var("b0_4e")->setConstant(true); // needed for being treated as global observables


  // w.var("Eff_4m")->setVal(0.844);
  // w.var("Eff_2e2m")->setVal(0.694);
  // w.var("Eff_4e")->setVal(0.60);
  
  // Float_t Eff_4m = 0.844*0.5388;
  // Float_t Eff_2e2m = 0.694*0.5388;
  // Float_t Eff_4e = 0.60*0.5388;
  
  w.var("Eff_4m")->setVal(Eff_4m);
  w.var("Eff_2e2m")->setVal(Eff_2e2m);
  w.var("Eff_4e")->setVal(Eff_4e);

  w.var("Eff0_4m")->setVal(Eff_4m);
  w.var("Eff0_2e2m")->setVal(Eff_2e2m);
  w.var("Eff0_4e")->setVal(Eff_4e);

  w.var("Eff0_4m")->setConstant(true); // needed for being treated as global observables
  w.var("Eff0_2e2m")->setConstant(true); // needed for being treated as global observables
  w.var("Eff0_4e")->setConstant(true); // needed for being treated as global observables

  Float_t  sigmaEff_4m = 0.0097 ;
  Float_t  sigmaEff_2e2m = 0.0097 ;
  Float_t  sigmaEff_4e = 0.0097 ;

  Float_t BRele = 0.03363;
  Float_t BRmu  = 0.03366;  

  Float_t BR_4m = BRmu*BRmu;
  Float_t BR_2e2m = 2*BRmu*BRele;
  Float_t BR_4e = BRele*BRele;

  Float_t BR = BR_4m+BR_2e2m+BR_4e;
  //  Float_t Lumi  = 2.56;

  Float_t xs_4m   = (nobs_4m - b_4m)/(Eff_4m*Lumi);
  Float_t xs_2e2m = (nobs_2e2m - b_2e2m)/(Eff_2e2m*Lumi);
  Float_t xs_4e   = (nobs_4e - b_4e)/(Eff_4e*Lumi);

  cout<<"xs 4m "<<xs_4m<<" xs 2e2m "<<xs_2e2m<<" xs 4e "<<xs_4e<<" Tot "<<(xs_4m+xs_2e2m+xs_4e)<<endl;  

  // cout<<"BR sum"<<BR<<" BRmean "<<(BR_4m + BR_4e + BR_2e2m)/3.<<" BR_4m "<<BR_4m<<" BR_2e2m "<<BR_2e2m<<" BR_4e "<<BR_4e<<endl;

  // w.var("BR_4m")->setVal(BR_4m);
  // w.var("BR_2e2m")->setVal(BR_2e2m);
  // w.var("BR_4e")->setVal(BR_4e);

  w.var("xs_4m")->setConstant(true); // needed for being treated as global observables
  w.var("xs_2e2m")->setConstant(true); // needed for being treated as global observables
  w.var("xs_4e")->setConstant(true); // needed for being treated as global observables

  w.var("Lumi")->setVal(2.560);
  w.var("Lumi")->setConstant(true); 

  w.var("sigmab_4m")->setVal(sigmab_4m*b_4m);  
  w.var("sigmab_2e2m")->setVal(sigmab_2e2m*b_2e2m);  
  w.var("sigmab_4e")->setVal(sigmab_4e*b_4e);  

  w.var("sigmaEff_4m")->setVal(sigmaEff_4m*Eff_4m);  
  w.var("sigmaEff_2e2m")->setVal(sigmaEff_2e2m*Eff_2e2m);  
  w.var("sigmaEff_4e")->setVal(sigmaEff_4e*Eff_4e);  
  
  ModelConfig mc("ModelConfig",&w);
  
   mc.SetPdf(*w.pdf("model"));
   mc.SetParametersOfInterest(*w.var("mu"));
  
   mc.SetObservables(RooArgSet(*w.var("nobs_4m"),*w.var("nobs_2e2m"),*w.var("nobs_4e")));  


  // mc.SetNuisanceParameters(RooArgSet(*w.var("b_4m"),*w.var("b_2e2m"),*w.var("b_4e")));

   //mc.SetObservables(RooArgSet(*w.var("nobs_4m"),*w.var("nobs_2e2m")));  
   //   mc.SetNuisanceParameters(RooArgSet(*w.var("b_4m"),*w.var("b_2e2m"),*w.var("Eff_4m"),*w.var("Eff_2e2m")));
   mc.SetNuisanceParameters(RooArgSet(*w.var("b_4m"),*w.var("b_2e2m"),*w.var("b_4e"),*w.var("Eff_4m"),*w.var("Eff_2e2m"),*w.var("Eff_4e")));

  // these are needed for the hypothesis tests
  mc.SetSnapshot(*w.var("mu"));
  mc.SetGlobalObservables(RooArgSet(*w.var("b0_4m"),*w.var("b0_2e2m"),*w.var("b0_4e")));


  //mc.Print();
  // import model in the workspace 

  w.import(mc);

  // make data set with the namber of observed events
  RooDataSet data("data","", RooArgSet(*w.var("nobs_4m"),*w.var("nobs_2e2m"),*w.var("nobs_4e")));
  //RooDataSet data("data","", RooArgSet(*w.var("nobs_4m"),*w.var("nobs_2e2m")));


  w.var("nobs_4m")->setVal(nobs_4m);
  data.add(*w.var("nobs_4m") );

  w.var("nobs_2e2m")->setVal(nobs_2e2m);
  data.add(*w.var("nobs_2e2m") );

  w.var("nobs_4e")->setVal(nobs_4e);
  data.add(*w.var("nobs_4e") );

  // import data set in workspace and save it in a file

  ProfileLikelihoodCalculator pl(data, mc);
  pl.SetConfidenceLevel(0.68); // 95% interval
  LikelihoodInterval* interval = pl.GetInterval();

  // print out the iterval on the first Parameter of Interest
  RooRealVar* firstPOI = (RooRealVar*) mc.GetParametersOfInterest()->first();
  cout << "\n68% interval on " <<firstPOI->GetName()<<" is : ["<<
    interval->LowerLimit(*firstPOI) << ", "<<
    interval->UpperLimit(*firstPOI) <<"] "<<endl;

  std::cout<<"Cross "<<mc.GetParametersOfInterest()->getRealValue("mu")*34.34<<std::endl;
  std::cout<<"Total Cross "<<(mc.GetParametersOfInterest()->getRealValue("mu")*34.34)/(Acc_4m*BR)<<std::endl;

  w.import(data);

  w.Print();

  TString fileName = "CountingModel.root"; 

  // write workspace in the file (recreate file if already existing)
  w.writeToFile(fileName, true);

}
