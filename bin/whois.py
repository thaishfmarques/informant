#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests

def whois(hostname):
	response = requests.get('http://api.hackertarget.com/whois/?q=' + hostname)
	test = response.text
	if response.status_code == 200:
		for line in test.split('\n'):
			if not line.startswith('%'):
				print(line)
			else:
				pass
	else:
		print('Invalid')