#!env/bin/python

import urllib2
import json


def locu_search(query):
	locu_api = 'e560a6caee0e2f04edf1d827a0cb1cb757ceb918'

	api_key = locu_api
	url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
	locality = query.replace(' ', '%20')
	final_url = url + "&locality=" + locality + "&category=restaurant"


	json_obj = urllib2.urlopen(final_url)

	data = json.load(json_obj)

	for item in data['objects']:
		print item['name'], item['phone']

locu_search("San Francisco")