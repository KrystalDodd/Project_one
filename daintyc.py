### SETUP

# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
#from scipy.stats import linregress
#from config import api_key
import json

# Import API key
from api_keys import 

api_key = "fsZSpGJjdpz_oH3iDeOHd_zCoLCffUje8ZNB9QACR8TMGkVKQiVRzGnD4im0CmCY6V3O3egacDsExbFEo0RFcHZysQocz2arAP9ab0BRcXbjludPtb-0IRu0HUnIX3Yx"

headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/search'
 
# In the dictionary, term can take values like food, cafes or businesses like McDonalds
params = {'term':'seafood','location':'New York City'}

# Making a get request to the API
req=requests.get(url, params=params, headers=headers)
 
# proceed only if the status code is 200
print('The status code is {}'.format(req.status_code))

# printing the text from the response 
json.loads(req.text)

# Output File (CSV)
filepath = 

# Load JSON

# Read CSV File

# CSV shape and head


### GENERATE LIST

# 
