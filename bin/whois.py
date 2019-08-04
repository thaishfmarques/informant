#!/usr/bin/python3

import requests

# funcao que consome a API Whois e fornece dados
def whois(get_input):
	response = requests.get('http://api.hackertarget.com/whois/?q=' + get_input)
	test = response.text
	if response.status_code == 200:
		for line in test.split('\n'):
			if not line.startswith('%'):
				print(line) 
			else:
				pass
	else:
		print('Invalid')



