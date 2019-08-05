#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests

# funcao que traz informacoes do geoip
def geoip(hostname):
	response = requests.get('http://api.hackertarget.com/geoip/?q=' + hostname)
	#response = response.text
	if response.status_code == 200:
		
		print(response.text)
	else:
		print('Invalid')

# TODO: get another use for this google maps geocoding api
# TODO: This is MY key. Please get this out of here. DO NOT FORGET
#mapp = requests.get('https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBvz9DkTVjFdrYuYZu8ytPp9q-uk5i3gYg&latlng='+str(lat)+','+lngt)