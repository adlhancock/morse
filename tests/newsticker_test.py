# -*- coding: utf-8 -*-
""" morse and newsticker test
Created on Tue Jun 26 15:10:29 2018

@author: dhancock
"""
#%%
import sys

sys.path.append("../")

from morse.newsticker import get_news
from morse.morse import translate
from morse.morse import morsetowav

#import winsound

#%%
print("getting news...")
news = get_news()
print("...got news!")

plain_titles = news["titles"]

print("translating titles to morse")
morse_titles = [translate(x) for x in plain_titles]

print("retranslating morse titles to plaintext")
retranslated_titles = [translate(x,"morse") for x in morse_titles]

response = input("print morse headlines [Y/n] ")
if response in ["Y",""]:
    print("MORSE HEADLINES\n"+"*"*50)
    [print(translate(x)+"\n"+"="*50+"\n") for x in morse_titles]


response = input("print retranslation check [Y/n] ")
if response in ["Y",""]:
    print("RETRANSLATION CHECK:\n"+"*"*50)
    [print(x.upper()+"\n"+y+"\n") for x,y in zip(plain_titles,retranslated_titles)]

response = input("record wav file [Y/n] ")
if response in ["Y",""]:
    morsetowav(morse_titles[-1],"news.wav",verbose=True)

