#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests
import os.path

def whois(hostname):
	response = requests.get('http://api.hackertarget.com/whois/?q=' + hostname)
	whois = response.text
	if response.status_code == 200:
		for line in whois.split('\n'):
			if not line.startswith('%'):
				print(line)
			else:
				pass
		folder_path= './files/'
		save_to_folder = os.path.join(folder_path+'whois.txt')
		try:
			f = open(save_to_folder, 'w')
			f.write('\n')
			f.write(whois)
			f.close()
			print('Saved file to: ')
		except:
			print('Unable to save file')
		
	else:
		print('Invalid')