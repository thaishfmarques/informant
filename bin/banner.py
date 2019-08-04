#!/usr/bin/python3

import whois, geoip, portscan


def banner():
    print(''.center(80, '-'))
    print(' Information Gathering '.center(80, '-'))
    print(' v0.1 an open source tool '.center(80, '-'))
    print(' for pentesting reconnaissance '.center(80, '-'))
    print(''.center(80, '-'))

def menu_online(menu_choice):
    banner()
    menu = '''
    [1] whois
    [2] geoip
    [3] portscan
    [4] sair\n'''
    
    print(menu)
    menu_choice = input('Selecione uma opção: ')

    if menu_choice == '1':
        get_host = input('Host: ')
        whois.whois(get_host)
    elif menu_choice == '2':
        get_ip = input('IP: ')
        geoip.geoip(get_ip)
    elif menu_choice == '3':
        get_ip = input('IP: ')
        portscan.portscan(get_ip)
    else:
        exit()

def menu_offline(menu_choice):
    banner()
    menu = '''
    [1] installation checklist
    [2] 
    [3] 
    [4] sair\n'''
    
    print(menu)
    menu_choice = input('Selecione uma opção: ')

    if menu_choice == '1':
        get_host = input('Host: ')
        whois.whois(get_host)
    elif menu_choice == '2':
        get_ip = input('IP: ')
        geoip.geoip(get_ip)
    elif menu_choice == '3':
        get_ip = input('IP: ')
        portscan.portscan(get_ip)
    else:
        exit()