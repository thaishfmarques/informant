#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

from os import system,name
from time import sleep
from socket import gethostname, gethostbyname
import platform
import whois, geoip, portscan 


VERSION = 'v0.5'

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
    while True:
        # limpa o console
        system('clear')

        banner()
        
        print( '''
        [1] Online Tools 
            [Online tools as whois, port scanning, geoip]
        [2] Offline Tools  /!\\
            [Checklist auditing tool] [-- in development --]
        [3] sair\n'''
        )
        print('Development version in: {} '.format(VERSION).rjust(80, ' '))
        print('-'.rjust(80, '-'))
        menu = input('Choose: ')
        if menu == '1':
            menu_option=''
            menu_online(menu_option)

        elif menu == '2':
            print('Sorry, this is still in development...')
            sleep(1.6)        
        elif menu == '3':
            exit()
        else:
            print('Invalid option.')
            sleep(0.9)

def menu_online(menu_option):
    hostname = input('Host: ')
    while True:
        system('clear')
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
        print('\n')
        
        if menu_option == '1':
            whois.whois(hostname)
            back = input('\nPress <enter> to return')

        elif menu_option == '2':
            geoip.geoip(hostname)
            back = input('Press <enter> to return')

        elif menu_option == '3':
            portscan.portscan(hostname)
            back = input('Press <enter> to return')

        elif menu_option == '4':
            hostname = input('Host: ')

        elif menu_option == '5':
            print('Returning...')
            sleep(0.9)
            menu_splash(menu_option)

        elif menu_option == '6':
            exit()

        else:
            print('Invalid option.')
            sleep(0.9)


def menu_offline(menu_option):
    while True:
        system('clear')
        banner()
        print('''
        [1] installation checklist
        [2] sair\n''')
        print('Development version in: {} '.format(VERSION).rjust(80, ' '))
        print('-'.rjust(80, '-'))

        menu_option = input('Choose: ')

        if menu_option == '1':
            print('Sorry, this is still in development...')
            sleep(1.6)  
        elif menu_option == '2':
            exit()
        else:
            print('Invalid option.')
            sleep(0.9)