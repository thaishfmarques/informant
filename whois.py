#!/usr/bin/python3

import requests

get_input = 'fiap.com.br'
response = requests.get('http://api.hackertarget.com/whois/?q=' + get_input)
test = response.text
if response.status_code == 200:
	#print(response.text)
	for line in test.split('\n'):
		if not line.startswith('%'):
			print(line)
else:
	print('Invalid')
