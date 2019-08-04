#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques
#
# TODO: Avoid getter and setter methods. (clean get_)
# TODO: Importing order: System imports Third-party imports Local source tree imports

# imported modules
from os import system # importa funcao de comandos unix
import banner
from time import sleep


while True:
    # limpa o console
    system('clear')

    # banner 
    banner.banner()
    
    print( '''
    [1] Online Tools 
        [Online tools as whois, port scanning, geoip]
    [2] Offline Tools
        [Checklist auditing tool]
    [3] sair\n'''
    )
    print('Developed by @thaishfmarques'.rjust(80, ' '))
    print('-'.rjust(80, '-'))
    menu = input('R: ')
    if menu == '1':
        system('clear')
        menu_choice=''
        banner.menu_online(menu_choice)
        
    elif menu == '2':
        system('clear')
        menu_choice=''
        banner.menu_offline(menu_choice)
    elif menu == '3':
        exit()
    else:
        print('Invalid option.')
        sleep(0.9)