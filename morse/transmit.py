# -*- coding: utf-8 -*-
"""transmit.py
Created on Tue Oct 24 17:17:46 2017

@author: David
"""

import os
import platform
import winsound
import time
from time import sleep as wait


wpm = 15
ditlength = int(2.4 / wpm * 1000)
frequency = 1000
codefile = './code.txt'

def import_morse(codefile=codefile):
    with open(codefile) as f:
        rawcode = [x.strip().split(' ') for x in f.readlines()]
    morse = {letter:sequence for letter,sequence in rawcode}
    return morse

def beep(t = ditlength, f = frequency):
    if platform.system() is 'Windows':
        winsound.Beep(f,t)
    elif platform.system() is 'Linux':
        os.system("beep -f {}, -l {}".format(f,t))

def dit():
    beep(ditlength)
    wait(ditlength/1000)
    
def dah():
    beep(3*ditlength)
    wait(ditlength/1000)

def endletter():
    wait(2*ditlength/1000)
    
def endword():
    wait(6*ditlength/1000)

def fromfile(filename):
    with open(filename) as f:
        filestring = f.read().strip()
    return filestring

def sendchar(plainchar,morse):
    if plainchar in (' ','\n','\r'): endword() 
    elif plainchar.lower() in morse.keys():
        morsechar = morse[plainchar.lower()]
        for x in morsechar:
            if x is '.': dit()
            elif x is '-':dah()
            else: raise Exception("error in morse code file")
        endletter()
    else:  
        print("*",end='')
        endletter()
        
def sendstring(string,morse,verbose=True):
    #morse = import_morse('./code.txt')
    tic = time.time()
    for char in string:
        if verbose is True: print(char,end='')
        sendchar(char,morse)

    if verbose is True:
        print('\nTime to send: {:.1f} seconds'.format(time.time()-tic))

if __name__ is '__main__':
    morse = import_morse()
    #signal = "Paris"
    signal = fromfile('./testsignal.txt')
    sendstring(signal,morse)
    