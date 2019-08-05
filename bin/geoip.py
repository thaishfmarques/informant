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

