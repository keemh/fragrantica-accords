# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:24:09 2021

@author: keemh
"""

import pandas as pd

df = pd.read_csv("perfume_houses.csv")
dict_from_df = df.to_dict('list')

acc_list = ["citrus, woody, floral, fruity",
"aromatic, leather, white floral, powdery",
"green, warm spicy, iris, musky",
"fresh spicy, amber, rose, sweet",
"fresh, earhty, yellow floral, vanilla"]

fav_lst = []
fav_lst_copied = []
sorted_lst=[]
    
for acc in acc_list:
    print("\n""---------------------------------------------------------""\n"
          "choose your favorite accord among :""\n", acc)
    fav_ac = input("my favorite accord is: ")
    fav_lst.append(fav_ac)
    fav_lst_copied.append(fav_ac)

for el in fav_lst:
    print("\n""---------------------------------------------------------""\n"
          "choose your favorite accord among : ""\n", fav_lst_copied)
    accord = input("my favorite accord is: ")
    sorted_lst.append(accord)
    fav_lst_copied.remove(accord)
    if len(fav_lst_copied)==1:
        sorted_lst.append(fav_lst_copied[0])
        break

dict_accord1 = {}
dict_accord2 = {}
dict_accord3 = {}
dict_accord4 = {}
dict_accord5 = {}

for key, value in dict_from_df.items():
    if sorted_lst[0] in value:
        dict_accord1[key]=value
        
for key, value in dict_accord1.items():
    if sorted_lst[1] in value:
        dict_accord2[key]=value
        
for key, value in dict_accord2.items():
    if sorted_lst[2] in value:
        dict_accord3[key]=value
        
for key, value in dict_accord3.items():
    if sorted_lst[3] in value:
        dict_accord4[key]=value
        
for key, value in dict_accord4.items():
    if sorted_lst[4] in value:
        dict_accord5[key]=value
        
result = [list(dict_accord5), list(dict_accord4), list(dict_accord3), list(dict_accord2), list(dict_accord1)]

print("\n""----------------------------------------------------------""\n"
      "I Recommend You . . .")

if len(result[0])==0 and len(result[1])==0 and len(result[2])==0:
    print("\n""I'm Sorry :(""\n"
          "Your taste is so unique and speacial that I couldn't find the perfume for you.""\n"
          "I'll come back with more perfumes later!")
else:
    for x in range(5):
        if 0<len(result[x])<10:
            print(result[x], "\n")
            for element in result[x]:
                print(element, '\n', dict_from_df[element], '\n')
            break
