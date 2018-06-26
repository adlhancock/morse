# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:33:52 2018

@author: dhancock
"""

from winsound import Beep as beep
from time import sleep as wait
import code

codesourcestring =  code.readlines()

codesource = [x.strip().split(",") for x in codesourcestring]
textdict = {a:b for a,b in source}
codedict = {b:a for a,b in source}

freq = 660
ditlength = 100


def ditsound():
    print(".", end="")
    wait(ditlength*1e-3)
    beep(frequency=freq,duration=ditlength)

def dahsound():
    wait(ditlength*1e-3)
    beep(frequency=freq,duration=3*ditlength)
    print("-", end="")

def letterpause():
    wait(2e-3*ditlength)
    print(" ", end="")

def wordpause():
    wait(6e-3*ditlength)
    print("/", end="")

def code2sound(codestring):
    for x in codestring.lower():
        if x is ".":
            ditsound()
        elif x is "-":
            dahsound()
        elif x is "/":
            wordpause()
        elif x is " ":
            letterpause()
        else:
            raise ValueError("Unrecognised symbol ({})".format(x))

def code2text(codestring):
    codeletter = ""
    textstring = ""
    for x in "["+codestring+"]":
        #print(x,end="")
        if x in [".","-"]:
            codeletter+=x
        elif x in [" ","/","\n","[","]"]:
            if codeletter in codedict:
                textletter = codedict[codeletter]
                textstring+=textletter
                codeletter = ""
            elif codeletter is "":
                pass
            else:
                raise ValueError("Unrecognised code ({})".format(codeletter))
            if x is "/":
                #print(x, end="")
                textstring+=" "
                codeletter = ""
        else:
            raise ValueError("Unrecognised symbol ({})".format(x))
    print()        
    return textstring

def text2code(textstring):
    codestring = ""
    for x in textstring:
        if x in textdict:
            codestring+=textdict[x]+" "
        elif x is " ":
            codestring+="/"
        else:
            raise ValueError("Unrecognised symbol ({})".format(x))
    return codestring
        

def main():
    with open("samplecode.txt") as f:
        codein = f.read()
    
    print(codein)
    
    textout  = code2text(codein)
    print(textout)
    
    codeout = text2code(textout)
    
    print(codeout)
    
    textoutagain = code2text(codeout)
    print(textoutagain)
    #code2sound(codestring)
