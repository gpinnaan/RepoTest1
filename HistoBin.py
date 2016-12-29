#! /usr/bin/env python

# bin = 0;       underflow bin
# bin = 1;       first bin with low-edge xlow INCLUDED
# bin = nbins;   last bin with upper-edge xup EXCLUDED
# bin = nbins+1; overflow bin

import ROOT, copy
from ROOT import TH1F

h1 = ROOT.TH1F("","",10,0,10)

Nbins=h1.GetNbinsX()

for i in range(0,Nbins+2):
    h1.SetBinContent(i,i)
    print i

h1.Fill(-10)
h1.Fill(-12)
h1.Fill(0)
h1.Fill(100,2)
h1.Fill(120,3)
print "under flow             ",h1.GetBinContent(0)
print "over flow (bin -1)     ",h1.GetBinContent(-1)
print "over flow (bin xbins+1)",h1.GetBinContent(11)
print "integral               ",h1.Integral()
print "integral 0,10          ",h1.Integral(0,10)
print "integral 0,-1          ",h1.Integral(0,-1)
print "integral 0,xbins+1     ",h1.Integral(0,11)


# boh
#h1.Draw("hist")
#CloseVar=input("digit anything you want to end the script \n")        
#for i in range(0,10):
 #   print i
