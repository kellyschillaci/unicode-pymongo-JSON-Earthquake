# -*- coding: utf-8 -*-
"""
Created on Tue May 14 21:24:40 2019

@author: kdoyl
"""

import urllib.request 
import json 
earthquake_url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significa nt_month.geojson" 
response = urllib.request.urlopen(earthquake_url) 
json_string = response.read().decode('utf-8')
eq_parsed_json = json.loads(json_string) 
type(eq_parsed_json) 
eq_parsed_json.keys() 
eq_parsed_json['type'] 
eq_parsed_json['metadata'] 
title = eq_parsed_json['metadata']['title'] 
title
quakelist = eq_parsed_json['features'] 
len(quakelist) 
quake1 = quakelist[0] 
type(quake1) 
quake1.keys() 
print(json.dumps(quake1, indent=2)) 