# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:35:00 2020

@author: danie
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fprepare%2Fprevention.html'
r = requests.get('https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fprepare%2Fprevention.html')
html_doc = r.text
soup = BeautifulSoup(html_doc)


for link in soup.find_all('a'):
    print (link.get('href'))