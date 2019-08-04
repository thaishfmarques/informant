#!/usr/bin/python3

import requests

def portscan(get_ip):
    response = requests.get('http://api.hackertarget.com/nmap/?q={}'.format(get_ip))
    scan = response.text

    print(scan)