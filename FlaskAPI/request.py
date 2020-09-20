# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 18:45:56 2020
@author: Safoora Naureen
"""

import requests 
from data_input import data_in

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()