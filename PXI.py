# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:31:49 2022

@author: Homa
"""

#To extract the first question of every topic for PXI usb, the following code is used, however, we can extract other keywords simply by replacing the respective url. 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

page=1
urls=[]
kudos=[]
question = []
replies=[]

while page < 101:
      url = f"https://forums.ni.com/t5/forums/searchpage/tab/message?filter=location&q=pxi&location=category:discussion-forums&page={page}&collapse_discussion=true"
      result = requests.get(url)    

## To make sure the website is accessible
      print(result.status_code)
## To make sure we are scrapping the correct website
#print(result.headers)
      src=result.content
## parse and process the source
      soup=BeautifulSoup(src, 'lxml')
      
     ## #Find all the links
      for y in soup.find_all("a", class_="page-link lia-link-navigation lia-custom-event"):
          href=y.attrs.get("href")
          print(href)
          if "m-p" in href:
              urls.append(href)
              
      page+=1
for i in range(len(urls)):
        urls[i]="https://forums.ni.com/" + urls[i]
        response = requests.get(urls[i])
        html = response.content
        soup = BeautifulSoup(html, "lxml")
        for x in soup.find_all('div',class_='lia-message-body-content', limit=1):
              
               Question= x.get_text()
               print(Question)
               question.append(Question)
               Q = {"Questions": question} 
               # dataframe
               Comment_df = pd.DataFrame(Q)
               Comment_df.to_csv('National_PXI_data.csv'
                                 
         ##replies scrapping####
    
        for p in soup.find_all('span', class_= 'MessagesPositionInThread','aria-label', limit=1):

            Replies=p.get_text()
            replies.append(Replies)
            R= {"number of replies": replies}
            Comment_df = pd.DataFrame(R)
            Comment_df.to_csv('NationalPXI_DATA1.csv')
        #### to scrape the users’ reputation by scrapping their profile:
page=1
user_type=[]        
kudos=[]
urls=[]
solutions=[]


while page < 101:
      url = f"https://forums.ni.com/t5/forums/searchpage/tab/message?filter=location&q=pxi&location=category:discussion-forums&page={page}&collapse_discussion=true"
      result = requests.get(url)    

## To make sure the website is accessible

      print(result.status_code)
## To make sure we are scrapping the correct website
#print(result.headers)

      src=result.content
## parse and process the source
      soup=BeautifulSoup(src, 'lxml')

# Find all the links

         
      for y in soup.find_all("a", class_="lia-link-navigation lia-page-link lia-user-name-link"):
          href=y.attrs.get("href")
          print(href)
          if "user-id" in href:
               urls.append(href)
               #print(urls)
         
      page+=1


for i in range(len(urls)):
       
        #urls[i]="https://forums.ni.com/" + urls[i]
        
      response = requests.get(urls[i])
      html = response.content
      soup = BeautifulSoup(html, "lxml")
        #print(html)
      for x in soup.find_all("div", class_=["rank-icon"]):

         User_type=x.get_text()
         user_type.append(User_type)
         U = {"user_type": user_type}
         Comment_df = pd.DataFrame(U)
         Comment_df.to_csv('NationalPXI_NEW_DATA2.csv')
            
         
      for y in soup.find_all('div', class_=['kudos-received','stat-value']):
           
          Kudos=y.get_text()
          kudos.append(Kudos)
          d = {"kudos": kudos}
          Comment_df = pd.DataFrame(d)
          Comment_df.to_csv('NationalPXI_DATA3.csv')

      for z in soup.find_all("div", class_= ['solutions','stat-value']):
          Solutions=z.get_text()
          solutions.append(Solutions)
          S= {"number of solutions": solutions}
          Comment_df = pd.DataFrame(S)
          Comment_df.to_csv('NationaPXI_DATA4.csv') 
