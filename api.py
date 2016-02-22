#!env/bin/python

import urllib2
import json

locu_api = 'e560a6caee0e2f04edf1d827a0cb1cb757ceb918'

url = 'https://api.locu.com/v1_0/venue/search/?locality=Newport%20Beach&category=restaurant&api_key=e560a6caee0e2f04edf1d827a0cb1cb757ceb918'

json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

print data