#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques
# 
# imported modules
from os import system
from sys import exit
import requests

system('clear')
print('			R E K O N  v0.1')
print('	| Welcome to Rekon v0.1 an open source tool			\n' 
	  '	| for reconnaissance and information gathering	\n')

##get_input = input('Go Big Son: ')
get_input = 'fiap.com.br'
response = requests.get('http://api.hackertarget.com/whois/?q=' + get_input)

print(response)
if response.status_code == 200:
	print(response.text)
else:
	print('I don\'t know her')

get_menu = input('Wana go back?')