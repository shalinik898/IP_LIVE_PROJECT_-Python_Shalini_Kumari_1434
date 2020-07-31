#importing all required files
import requests
from bs4 import BeautifulSoup
import re


finalrecords=[]     #finallist having all records
sr=0
#pagination
pages=['ahmednagar','akola','amravati','aurangabad','beed','dhule','jalgaon','kolhapur','latur','mumbai','nagpur','nanded','nashik','navi-mumbai','osmanabad','pune','raigad','sangli','solapur' ,'thane']

#loop for accessing multiple pages

for page in pages:
    data = requests.get('https://www.extraprepare.com/'+ str(page)+'/engineering-institutes-'+str(page)+'.html')

    soup=BeautifulSoup(data.text,'html.parser')
   
    #extracting required data using regex
    collegename = re.findall(r'<h3[^>]*>([^<]+)</h3>', data.text) 
    phones = re.findall(r'<b>Phone:[^>]*>([^<]+)<br /><b>', data.text)
    phones+= [None] * (len(collegename)-len(phones))
    #print(phones)
    fax = re.findall(r'<b>Fax:[^>]*>([^<]+)<br /><b>', data.text)
    fax+= [None] * (len(collegename)-len(fax))
    #print(fax)
    website = re.findall(r'<b>Website:[^>]*>([^<]+)<br />', data.text)
    website+= [None] * (len(collegename)-len(website))
    #print(website)
    location = re.findall(r'<br[^>]*>([^<]+)-', data.text)
    location+= [None] * (len(collegename)-len(location))
    #print(location)
    affiliatedto=re.findall(r'<strong>Affiliated to:[^>]*>([^<]+)<br /><br />', data.text)
    affiliatedto+= [None] * (len(collegename)-len(affiliatedto))
    #print(affiliatedto)

    
    records = []      #single page list
    for i in range (len(collegename)):
        sr = sr+1
        collegeName1 = collegename[i]
        location1 = location[i]
        phones1 = phones[i]
        fax1 = fax[i]
        website1 = website[i]
        affiliatedto1 = affiliatedto[i]

        records.append((sr,collegeName1,location1,phones1,fax1,website1,affiliatedto1))

    finalrecords+=records    #multipage list

#print(finalrecords)

#saving in .csv

import pandas as pd     

df=pd.DataFrame(finalrecords,columns=['Sr No','CollegeName','Location','Phones','Fax','Websites','AffiliatedTo'])
print(df.head())

df.to_csv('CollegeList.csv',index=False,encoding='utf-8')
#saving into collegelist.csv



