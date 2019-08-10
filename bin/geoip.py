#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests

def geoip(hostname):
	response = requests.get('http://api.hackertarget.com/geoip/?q=' + hostname)
	if response.status_code == 200:
		
		print(response.text)
	else:
		print('Invalid')