#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

from os import system,name
import platform
import subprocess  # For executing a shell command
from time import sleep
from socket import gethostname, gethostbyname

import whois, geoip, portscan


VERSION = 'v0.7'


# funcao para limpar a tela - multiplataforma
def clear():
    # Clear command as function of OS
    if platform.system().lower()=='windows':
        command = 'cls' 
    else: 
        command = 'clear'
    return subprocess.call(command) == 0


# Define banner principal do script
def banner():
    os_dist = platform.linux_distribution()
    os = '{} - {}'.format(platform.system(),' '.join(os_dist).title())
    print(''.center(80, '-'))
    print(' # Informant {} # '.format(VERSION).center(80, '-'))
    print(' an open source tool '.center(80, '-'))
    print(' for information gathering '.center(80, '-'))
    print(''.center(80, '-'))
    print('OS: {} '.format(os).rjust(80, ' '))
    print('local hostname: {} '.format(gethostname()).rjust(80, ' '))


# menu principal da aplicação
def menu_splash(menu_option):
    try:
        while True:
        # limpa o console
            clear()

            banner()
            
            print( '''
            [1] Online Tools 
                [Online info gathering tool as whois, port scanning, geoip]
            [-] GHDB Search
                [search for google dorks]
            [3] sair\n'''
            )
            print('Development version in: {} '.format(VERSION).rjust(80, ' '))
            print('-'.rjust(80, '-'))
            menu = input('Choose: ')
            if menu == '1':
                menu_option=''
                menu_online(menu_option)    
            elif menu == '3':
                exit()
            else:
                print('Invalid option.')
                sleep(0.9)
    except KeyboardInterrupt as kboard:
        print('\nExiting...')
        sleep(0.3)

def menu_online(menu_option):
    hostname = input('Host: ')
    while True:
        clear()
        banner()
        print('''
        [1] whois
        [2] geoip
        [3] portscan
        [4] change host
        [5] back
        [6] exit\n''')
        print('[X]: {}'.format(hostname).ljust(80, ' '))
        print('Development version in: {} '.format(VERSION).rjust(80, ' '))
        print('-'.rjust(80, '-'))
        menu_option = input('Choose: ')
        
        if menu_option == '1':
            
            whois.whois(hostname)
            back = input('\nPress <enter> to return')

        elif menu_option == '2':
            geoip.geoip(hostname)
            back = input('\nPress <enter> to return')

        elif menu_option == '3':
            portscan.portscan(hostname)
            back = input('\nPress <enter> to return')

        elif menu_option == '4':
            hostname = input('Host: ')

        elif menu_option == '5':
            print('\nReturning...')
            sleep(0.9)
            menu_splash(menu_option)

        elif menu_option == '6':
            exit()

        else:
            print('Invalid option.')
            sleep(0.9)

