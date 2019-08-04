#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques
# 
# imported modules
from os import system

from sys import exit

# limpa o console
system('clear')

# banner (criar def?)
print(''.center(80, '-'))
print(' Information Gathering '.center(80, '-'))
print(' v0.1 an open source tool '.center(80, '-'))
print(' for pentesting reconnaissance '.center(80, '-'))
print(''.center(80, '-'))

menu = '''
    [1] whois
    [2] geoip
    [3] sair\n'''
    
print(menu)
menu_choice = input('Escolha uma opção: ')

if menu_choice == '1':
    #whois(get_host)
    print('whois')
elif menu_choice == '2':
    #geoip(get_ip)
    print('geoip')
else:
    exit()