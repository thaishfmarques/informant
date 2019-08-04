#!/usr/bin/python3

import requests
	
#get_input = '82.135.139.155'

# funcao que traz informacoes do geoip
def geoip(get_input):
	response = requests.get('http://api.hackertarget.com/geoip/?q=' + get_input)
	get_response = response.text
	if response.status_code == 200:
		for each_resp in get_response.split('\n'):
			print(each_resp)
	else:
		print('Invalid')

# TODO: get another use for this google maps geocoding api
# TODO: This is MY key. Please get this out of here. DO NOT FORGET
#mapp = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBvz9DkTVjFdrYuYZu8ytPp9q-uk5i3gYg&latlng='+str(lat)+','+lngt)