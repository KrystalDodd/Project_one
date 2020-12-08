#!/usr/bin/env python
# coding: utf-8

# ### Project_one Hypothesis:

# #### Dependencies and Setup

# In[ ]:


#Dependencies
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import json


# In[ ]:


#Import API key
api_key = "fsZSpGJjdpz_oH3iDeOHd_zCoLCffUje8ZNB9QACR8TMGkVKQiVRzGnD4im0CmCY6V3O3egacDsExbFEo0RFcHZysQocz2arAP9ab0BRcXbjludPtb-0IRu0HUnIX3Yx"


# In[ ]:


#Base url and authorization header
url='https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer %s' % api_key}


# In[ ]:


#Parameters
params = {'term':'seafood','location':'New York City'}


# In[ ]:


#Get request to the API
req = requests.get(url, params=params, headers=headers)


# In[ ]:


#Proceed if status code is 200
req.status_code


# In[ ]:


#Print text from response
json.loads(req.text)


# #### Generate lists

# In[ ]:




