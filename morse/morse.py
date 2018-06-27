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

if __name__ == "__main__":
    morse = translate("Hello world:")
    print(morse)
    
    recoded = translate(morse, "morse")
    print(recoded)
    
    #print(morsecode)