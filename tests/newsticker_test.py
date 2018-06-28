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

import winsound

#%%
news = get_news()

plain_titles = news["titles"]
morse_titles = [translate(x) for x in plain_titles]
retranslated_titles = [translate(x,"morse") for x in morse_titles]

print("MORSE HEADLINES\n"+"*"*50)
[print(translate(x)+"\n"+"="*50+"\n") for x in morse_titles]

print("RETRANSLATION CHECK:\n"+"*"*50)
[print(x.upper()+"\n"+y+"\n") for x,y in zip(plain_titles,retranslated_titles)]

#%%

morsetowav(morse_titles[-1],"news.wav",verbose=True)



