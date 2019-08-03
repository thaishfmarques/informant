#!/usr/bin/python3

import requests

get_input = '200.147.3.157'
lat = '-26.196223'
lngt= '-52.689523'
response = requests.get('http://api.hackertarget.com/geoip/?q=' + get_input)
map = requests.get('http://maps.googleapis.com/maps/api/geocode/xml?key=AIzaSyBvz9DkTVjFdrYuYZu8ytPp9q-uk5i3gYg?latlng='+str(lat)+','+lngt)

if response.status_code == 200:
	print(response.text)
	print(map.text)
else:
	print('Invalid')


	