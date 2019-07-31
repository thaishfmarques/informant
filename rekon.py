#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques
# 
# imported modules
from os import system
from sys import exit
from requests import get

system('clear')
print('			R E K O N  v0.1')
print('	| Welcome to Rekon v0.1 an open source tool			\n' 
	  '	| for reconnaissance and information gathering	\n')

def whois(get_input):
	response = get('http://api.hackertarget.com/whois/?q=' + get_input).text
	return response




# menu function that does not go here
# def menu(get_option):
# 	while True:
# 		print('		[1]\n'
# 	      '		[2]\n'
# 		  '		[3]\n'
# 		  '		[4]\n'
# 		  '		[5] Exit\n')
# 	get_option = int(input())
# 	if get_option == 5:
# 		exit()
# 	return get_option