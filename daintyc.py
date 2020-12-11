#!/usr/bin/env python
# coding: utf-8

# ## Rise of the vegan: change in vegan restaurants in rural and urban areas

# #### Dependencies and Setup

# In[84]:


# Dependencies
import matplotlib.pyplot as plt
import pandas as pd
# from yelp import Client
# from ratelimit import limits
import numpy as np
import requests
import json
import csv
import random

# MY_API_KEY = "fsZSpGJjdpz_oH3iDeOHd_zCoLCffUje8ZNB9QACR8TMGkVKQiVRzGnD4im0CmCY6V3O3egacDsExbFEo0RFcHZysQocz2arAP9ab0BRcXbjludPtb-0IRu0HUnIX3Yx" #  Replace this with your real API key

# client = Client(MY_API_KEY)


# #### Create random sample data of 100 rural and 100 urban cities

# In[85]:


# Read census csv file for cities, state, and population for rural (<50000) and urban(>50000)
df = pd.read_csv("../Downloads/sub-est2019_all.csv", engine='python')

# In[86]:


# Create rural and urban dataframes
rural_city = df[(df["POPESTIMATE2019"] < 50000) & (df["POPESTIMATE2019"] > 1000)]
rural_df = rural_city[["NAME", "STNAME", "POPESTIMATE2019"]]
urban_city = df[df["POPESTIMATE2019"] >= 50000]
urban_df = urban_city[["NAME", "STNAME", "POPESTIMATE2019"]]

# In[87]:


# Create clean urban dataframe by dropping cities with state name
urban_index = urban_df.loc[urban_df["NAME"] == urban_df["STNAME"]].index
urban_clean = urban_df.drop(urban_index)

# In[88]:


# Narrow down cities for rural and urban to a 100 city names/samples
random_urban_city = urban_clean[["NAME", "STNAME", "POPESTIMATE2019"]].sample(n=200, random_state=1)
random_rural_city = rural_df[["NAME", "STNAME", "POPESTIMATE2019"]].sample(n=200, random_state=1)

# In[89]:


random_rural_city.columns

# In[90]:


random_rural_city.shape

# #### Yelp API request

# In[91]:


# Base url and authorization header
url = 'https://api.yelp.com/v3/businesses/{}'
# url='https://api.yelp.com/v3/businesses/search'


# ##### Pull data from Yelp Fusion using rural cities from random sample

# In[132]:


my_api_key = "fsZSpGJjdpz_oH3iDeOHd_zCoLCffUje8ZNB9QACR8TMGkVKQiVRzGnD4im0CmCY6V3O3egacDsExbFEo0RFcHZysQocz2arAP9ab0BRcXbjludPtb-0IRu0HUnIX3Yx"
headers = {'Authorization': 'Bearer %s' % my_api_key}

rural_dict = {
    "Searched": [],
    "City": [],
    "State": [],
    "Lat": [],
    "Lng": [],
    "Restaurant": [],
    "Category": [],
    "Category 2": [],
    "Category 3": [],
    "Transactions": [],
    "Prices": [],
    "Rating": [],
    "Reviews": []
}

url = 'https://api.yelp.com/v3/businesses/search'

for city, state in zip(random_urban_city["NAME"], random_urban_city["STNAME"]):
    params = {
        'limit': 50,
        'offset': 50,
        'location': f"{city}, {state}",
        'radius': 4000
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    business_list = data['businesses']
    for business in business_list:
        rural_dict["City"].append(business["location"]["city"])
        rural_dict["State"].append(business["location"]["state"])
        rural_dict["Lat"].append(business["coordinates"]["latitude"])
        rural_dict["Lng"].append(business["coordinates"]["longitude"])
        rural_dict["Restaurant"].append(business["name"])
        #             rural_dict["Category"].append([response["businesses"][business]["categories"][i]["title"] for i in range(len(response["businesses"][business]["categories"]))])
        rural_dict["Category"].append(business["categories"][0]["title"])
        #         rural_dict["Category 2"].append(business["categories"][1]["title"])
        #         rural_dict["Category 3"].append(business["categories"]["title"][2])
        rural_dict["Transactions"].append(business["transactions"])
        rural_dict["Prices"].extend(business["price"])
        rural_dict["Rating"].append(business["rating"])
        rural_dict["Reviews"].append(business["review_count"])

    pass

# In[ ]:


# import json
# with open('json_multidimensional.json','r') as string:
#     my_dict=json.load(string)
# string.close()
# def iterate_multidimensional(my_dict):
#     for k,v in my_dict.items():
#         if(isinstance(v,dict)):
#             print(k+":")
#             iterate_multidimensional(v)
#             continue
#         print(k+" : "+str(v))
# iterate_multidimensional(my_dict)


# In[133]:


# Create rural dataframe from rural cities (with <50000 est. pop.) Yelp API response
rural = pd.DataFrame.from_dict(rural_dict, orient='index')
rural = rural.transpose()
rural.head()

# In[134]:


rural.shape

# ##### Pull data from Yelp Fusion using urban cities from random sample

# In[ ]:


headers = {'Authorization': 'Bearer %s' % my_api_key}

urban_dict = {
    "Searched": [],
    "City": [],
    "State": [],
    "Lat": [],
    "Lng": [],
    "Restaurant": [],
    "Category": [],
    "Category 2": [],
    "Category 3": [],
    "Transactions": [],
    "Prices": []
    "Rating": []
}

url = 'https://api.yelp.com/v3/businesses/search'

for city, state in zip(random_urban_city["NAME"], random_urban_city["STNAME"]):
    params = {
        'limit': 50,
        'offset': 50,
        'location': f"{city}, {state}",
        'radius': 4000
    }
    response = requests.get(url, params=params, headers=headers).json()
    for business in range(len(response["businesses"])):
        try:
            urban_dict["Searched"].append(f"{city}, {state}")
            urban_dict["City"].append(response["businesses"][business]["location"]["city"])
            urban_dict["State"].append(response["businesses"][business]["location"]["state"])
            urban_dict["Lat"].append(response["businesses"][business]["coordinates"]["latitude"])
            urban_dict["Lng"].append(response["businesses"][business]["coordinates"]["longitude"])
            urban_dict["Restaurant"].append(response["businesses"][business]["name"])
            #             urban_dict["Category"].append([response["businesses"][business]["categories"][i]["title"] for i in range(len(response["businesses"][business]["categories"]))])
            urban_dict["Category"].append(response["businesses"][business]["categories"][0]["title"])
            urban_dict["Category 2"].append(response["businesses"][business]["categories"][1]["title"])
            urban_dict["Category 3"].append(response["businesses"][business]["categories"][2]["title"])
            urban_dict["Transactions"].append(response["businesses"][business]["transactions"])
        except KeyError:
            urban_dict["Searched"].append("No City Found")
            urban_dict["City"].append("No City Found")
            urban_dict["State"].append("No State Found")
            urban_dict["Lat"].append("No Lat Found")
            urban_dict["Lng"].append("No Lng Found")
            urban_dict["Restaurant"].append("No Restaurant Found")
            urban_dict["Category"].append("No Categories")
            urban_dict["Transactions"].append("No Transactions Found")
        except IndexError:
            urban_dict["Category 2"].append("")
            urban_dict["Category 3"].append("")

# In[ ]:


# Create urban dataframe from urban cities (with >50000 est. pop.) Yelp API response
urban = pd.DataFrame.from_dict(urban_dict, orient='index')
urban = urban.transpose()
urban.head()

# In[ ]:


rural.shape

# In[ ]:


# Save urban and rural city API results to csv files
urban.to_csv("../urban.csv")
rural.to_csv("../rural.csv")

# #### Extract urban city data with vegan/vegetarian places or options from Yelp Fusion

# In[5]:


rural_vegan = rural[(rural["Category"] == "Vegetarian")]

# In[135]:


rural_vegan = rural[(rural["Category"] == "Vegan")]
rural_vegan.head()

# #### Calculate percentage: Vegan/Vegetarian Places per State

# #### Identify: Top Vegan/Vegetarian restaurants by state

# In[ ]:


# In[ ]:


# In[ ]:




