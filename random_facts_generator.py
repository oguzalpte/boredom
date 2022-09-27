# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:36:58 2022

@author: oguzhan.alptekin
"""

import requests
from bs4 import BeautifulSoup
from random import random
from win10toast import ToastNotifier

response = requests.get(
	url="https://www.cs.cmu.edu/~bingbin/",
)
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')


i = int(random() * 100)
print(i)

#title = soup.findAll("li")[i].getText()
#print(title)
textt ="***" + soup.find_all("p")[i].getText() + "****"

toast = ToastNotifier()
toast.show_toast(
    "Random Information from Wikipedia!",
    textt,
    duration = 20,
    threaded = True,
)
