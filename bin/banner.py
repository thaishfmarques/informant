#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

# system imports
import platform
import subprocess 
from os import system
from time import sleep
from socket import gethostname

# local imports
import whois, geoip, portscan, shodanz # local source imports


VERSION = 'v0.8'


# clean console screen
# TODO: Windows cls still not working 
def clear():
    if platform.system().lower()=='windows':
        command = 'cls' 
    else: 
        command = 'clear'
    return subprocess.call(command) == 0


# Defines the principal banner
def banner():
    # TODO: os_dist windows compatibility
    os_dist = platform.linux_distribution()
    os = '{} - {}'.format(platform.system(),' '.join(os_dist).title())

    print(''.center(80, '-'))
    print(' # Informant {} # '.format(VERSION).center(80, '-'))
    print(' an open source tool '.center(80, '-'))
    print(' for information gathering '.center(80, '-'))
    print(''.center(80, '-'))
    print('OS: {} '.format(os).rjust(80, ' '))
    print('local hostname: {} '.format(gethostname()).rjust(80, ' '))


# defines the splash menu
def menu_splash(menu_option):
    try:
        while True:
            clear()
            banner()
            
            print( '''
            [1] Online Tools 
                [Online info gathering tool as whois, port scanning, geoip]
            [2] Shodan Search
                [search for devices with shodan]
            [3] exit\n'''
            )
            print('Development version in: {} '.format(VERSION).rjust(80, ' '))
            print('-'.rjust(80, '-'))
            menu = input('Choose: ')
            if menu == '1':
                menu_option=''
                menu_online(menu_option)    
            elif menu == '2':
                menu_option=''
                menu_shodan(menu_option)    
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


# define menu call for shodan options
def menu_shodan(menu_option):
    api_key=''
    print('To use the Shodan API, you will need an key generated in\n'
          'https://account.shodan.io/'.center(80, ' '))
    api_key = input('API key: ')
    if len(api_key) < 25:
        print('Invalid. Please insert a valid key.')
        sleep(0.9)
    else:
        clear()
        banner()
        print('SHODAN'.center(80,' '))
        print('search engine for devices connected to the internet'.center(80,' '))
        print('https://shodan.io - All Rights Reserved'.center(80,' '))

        print('''
        [1] basic search
        [2] MORE OPTIONS
        [3] BACK
        [4] exit\n''')

        print('Development version in: {} '.format(VERSION).rjust(80, ' '))
        print('-'.rjust(80, '-'))
        menu_option = input('Choose: ')
        
        if menu_option == '1':
            print('In development')
            back = input('\nPress <enter> to return')

        elif menu_option == '2':
            print('In development')
            back = input('\nPress <enter> to return')

        elif menu_option == '3':
            print('\nReturning...')
            sleep(0.9)
            menu_splash(menu_option)

        elif menu_option == '4':
            exit()

        else:
            print('Invalid option.')
            sleep(0.9)
