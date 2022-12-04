#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests, webbrowser
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time


# In[3]:


with open("Category Mappings via Scrapping.csv", newline="", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for r in csv_reader:
        # print(r)

        print(r["Name"])

        user_input = r["Name"]
       
        time.sleep(3)
        google_search = requests.get(
            "https://www.google.com/search?q=" + user_input + "+synonym"
        )
        # time.sleep(2)

        soup = BeautifulSoup(google_search.text, "html.parser")
        search_results = soup.select(".r, a")
       
        data ={}
        data = {"word": [], "synonym": []}
       
        # time.sleep(2)
        #for link in [1:2]:
        for link in search_results[1:2]:
            # item = {}
            actual_link = link.get("href")
            # data = {"word":user_input , "synonym":'https://google.com/'+actual_link}

   
            data["synonym"].append("https://google.com/" + actual_link)

            # print('https://google.com/'+actual_link)
            # webbrowser.open('https://google.com/'+actual_link[0])
            print(data)
            time.sleep(1)


# In[ ]:




