# -*- coding: utf-8 -*-
"""
morse v3

Created on Wed Jun 27 15:39:45 2018

@author: dhancock
"""

morsecode = """
a,.-
b,-...
c,-.-.
d,-..
e,.
f,..-.
g,--.
h,....
i,..
j,.---
k,-.-
l,.-..
m,--
n,-.
o,---
p,.--.
q,--.-
r,.-.
s,...
t,-
u,..-
v,...-
w,.--
x,-..-
y,-.--
z,--..
0,-----
1,.----
2,..---
3,...--
4,....-
5,.....
6,-....
7,--...
8,---..
9,----.
.,.-.-.-
?,..--..
!,-.-.--
:,---...
',.---.
-,-....-
"""

import numpy as np
import wave
import struct
#%%
def translate(sourcestring,mode="plain"):

    code = [x.strip().split(",") for x in morsecode.strip().split("\n")]
    dictionary               = {}
    dictionary["plain"]      = {plain.upper():morse+" " for plain,morse in code}
    dictionary["plain"][" "] ="/ "
    dictionary["plain"]["\n"] =".-.- "
    dictionary["plain"][","] ="--..-- "
    dictionary["morse"]      = {morse:plain.upper() for plain,morse in code}
    dictionary["morse"]["/"] = " "
    dictionary["morse"][".-.-"] = "\n"
    dictionary["morse"]["--..--"] = ","
    
    if mode is "morse":
        sourcecode = sourcestring.upper().strip().split(" ")
    elif mode is "plain":
        sourcecode = [x.upper() for x in sourcestring]
    else:
        raise ValueError
    
    outstring=''
    for char in sourcecode:
        try: 
            outstring+=dictionary[mode][char]
        except:
            outstring+="*"
    return outstring
#%%
def morsetowav(morsestring,
          outfile,
          ditlength=60,
          frequency=220,
          framerate=44100,
          verbose = True):
    
    t = ditlength*100
    f = frequency
    
    on = lambda x: list(100*np.sin(np.arange(x)*f))
    off = lambda x: list(0*np.arange(x))
    
    dit = on(t)+off(t)
    dah = on(3*t)+off(t)
    letterspace = off(3*t)
    wordspace = off(7*t)
    
    d = {".":dit,
         "-":dah,
         " ":letterspace,
         "/":wordspace
         }
    
    if verbose is True: print("Opening file...")
    
    with wave.open(outfile,"wb") as wave_output:
        wave_output.setparams((2,2,framerate,0,'NONE','not compressed'))
        
        for char in "//"+morsestring+"//":
    
            if verbose is True: print(char,end="")
            
            sound = d[char]
            for j in sound:
                value = int(j)
                packed_value = struct.pack('h',value)
                wave_output.writeframes(packed_value)
    
    if verbose is True: print("\nComplete!")
#%%
if __name__ == "__main__":
    morse = translate("Hello world:")
    print(morse)
    
    recoded = translate(morse, "morse")
    print(recoded)
    
    #print(morsecode)
