# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:21:51 2021

@author: acer
"""

import json as js
import pandas as pd
import requests as rq
jData=rq.get("https://jsonplaceholder.typicode.com/todos")
jsonToExcel=pd.read_json(jData.text)
pd.to_excel(jsonToExcel.xlsx)