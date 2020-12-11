import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress
import json
import requests

my_api_key = "OIzAV_YrskR2xaVYw26sZFcsljo-eHZoTsLOQe-Zr-FUmbFv10fccUhLHEKRexJ9CQ4A9GtX3BGsD1MTux16iY_jxFcuCjEVbA_bTqYE_R70cf3iPJw5FAfXgD7IX3Yx"
headers = {'Authorization': 'Bearer %s' % my_api_key}

url='https://api.yelp.com/v3/businesses/search'
 

params = {'term':'vegan','location':'Baltimore'}

req = requests.get(url, params = params, headers = headers).json()

print(req)               