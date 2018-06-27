# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:10:29 2018

@author: dhancock
"""

from newsticker import get_news
from morse import translate

news = get_news()
print("MORSE HEADLINES\n"+"*"*50)
[print(translate(x)+"\n"+"="*50+"\n") for x in news["titles"][2:]]

titles = [translate(translate(x),"morse") for x in news["titles"]]

print("RETRANSLATION CHECK:\n"+"*"*50)
[print(x+"\n"+y.upper()+"\n") for x,y in zip(titles,news["titles"])]