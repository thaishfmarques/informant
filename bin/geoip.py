#!/usr/bin/python3

import requests

get_input = '82.135.139.155'
#lat = '-26.196223'
#lngt= '-52.689523'
response = requests.get('http://api.hackertarget.com/geoip/?q=' + get_input)


get_resp = response.text

if response.status_code == 200:
	for each_resp in get_resp.split('\n'):
		if each_resp.startswith('Latitude'):
			lat = each_resp[10:]
			lat = '-23.587470'
			#print(lat)
		elif each_resp.startswith('Longitude'):
				lngt = each_resp[11:]
				#print(lngt)
				lngt= '-46.633480'
		else:
    			print(each_resp)
	#mapp = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBvz9DkTVjFdrYuYZu8ytPp9q-uk5i3gYg&latlng='+str(lat)+','+lngt)
	#et_map = mapp.json()

	#print(get_map)
else:
	print('Invalid')