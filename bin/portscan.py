#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests

def portscan(hostname):
    response = requests.get('http://api.hackertarget.com/nmap/?q={}'.format(hostname))
    scan = response.text

    print('\n{}'.format(scan))