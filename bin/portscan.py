#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests
from os import system

def portscan(ip_address):
    response = requests.get('http://api.hackertarget.com/nmap/?q={}'.format(ip_address))
    scan = response.text

    print('\n{}'.format(scan))