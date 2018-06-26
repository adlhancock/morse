# -*- coding: utf-8 -*-
""" newsticker.py
Created on Tue Jun 26 12:42:30 2018

@author: dhancock
"""

import urllib.request
#import re

def get_xml(url):
    with urllib.request.urlopen(url) as response:
        xmlcode=[x.decode() for x in response.readlines()]
    return xmlcode
    
def get_tag_contents(xmlcode,tag):

    contents = [x.strip().replace("<"+tag+">","").replace("</"+tag+">","")
                for x in xmlcode if "<"+tag+">" in x]
    return contents


def get_news(url = "http://feeds.reuters.com/reuters/UKTopNews"):
    titles,descriptions,dates = [
            get_tag_contents(get_xml(url),tag) 
            for tag in ("title","description","pubDate")]
    stories = [
            "("+date+")\n"+
            x.upper()+"... \n"+
            y.replace('&lt;div class="feedflare"&gt;',''+"\n")
            for date,x,y in zip(dates,titles[2:],descriptions[1:])]
    news = {
            "dates":dates,
            "titles":titles,
            "descriptions":descriptions,
            "stories":stories
            }
    return news

if __name__ == "__main__":
    [print(x) for x in get_news()["stories"]]

""" 
## another method...

import xml.etree.ElementTree as ET

url = "http://feeds.reuters.com/reuters/UKTopNews"

with urllib.request.urlopen(url) as response:
    root = ET.fromstring(response.read().decode())
    
for tag in root.iter("title"):
    print(tag.text,"\n")
"""