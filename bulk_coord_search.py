import os
import json
import requests
import argparse
import time
from requests.auth import HTTPBasicAuth

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('=======end-of-3-sec-timer=======') 

PLANET_API_KEY = '123456'

parser = argparse.ArgumentParser()
parser.add_argument('--coords', metavar ='N', type = float, nargs ='+')
parser.add_argument("--lte")
parser.add_argument("--gte")
  
for key, value in parser.parse_args()._get_kwargs():
  if key == 'coords':
    coordsValue = value
  if key == 'lte':
    lteValue = value
  if key == 'gte':
    gteValue = value

geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": {"type":"Point","coordinates":coordsValue}
  #value evaluates to [66.95100965894038, 25.02051729810101]
}
print ("*******coords*******")
print (coordsValue)

date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": gteValue,
    "lte": lteValue
#    evaluates to below
#    "gte": "2016-01-01T00:00:00.000Z",
#    "lte": "2016-12-31T00:00:00.000Z"
  }
}
print ("*******time intervals*******")
print (lteValue)
print (gteValue)

cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
     "lte": 1.0
  }
}

combined_filter = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}
  
search_request = {
  "interval": "day",
  "item_types": ["PSScene3Band"], 
  "filter": combined_filter
}
#print ('search_request')
#print (search_request)
  
quick_search_url = 'https://api.planet.com/data/v1/quick-search'

search_result = requests.post(quick_search_url, auth=HTTPBasicAuth(PLANET_API_KEY, ''), json=search_request)

image_ids = [feature['id'] for feature in search_result.json()['features']]
#print(geometry_filter['config']['coordinates'])
#print()
print ("*******image hit count*******")
print(len(image_ids))
#print(image_ids)
print('-------------------')
#print(image_ids)
countdown(3)
