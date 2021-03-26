# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 15:52:57 2021

@author: keemh
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import time
import re
import pandas as pd

with open('perfume_houses.txt', 'r') as f:
    list_file = []
    for line in f:
        list_file.append(line)

dict_data = {'perfume_name':['accord1', 'accord2', 'accord3', 'accord4', 'accord5']}
df = pd.DataFrame(dict_data)

for perfume in list_file:
    req = Request(perfume, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    bsObject = bs(urlopen(req), "html.parser") 

    data1_list=bsObject.findAll('div',{'class':'cell accord-box'})
    #print(data1_list)

    main_accords_list = []

    for data1 in data1_list:
        data2=data1.findAll('div',{'class':'accord-bar'})
        
        accord_list = [t.text for t in data2]
        main_accords_list.append(accord_list)
        
    name = perfume.split('/')
    perfume_name = " ".join(re.findall("[a-zA-Z]+",name[5][0:-5]))
    
    try:
        df[perfume_name] = main_accords_list[0:5]
    except ValueError:
        df[perfume_name] = 'Error'

    print(df)
    
    df.to_csv("perfume_houses.csv")

    time.sleep(30)

df.drop('perfume_name', axis=1, inplace=True)
print(df)

df.to_csv("perfume_houses.csv")