#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import sys
import os

while True:
    print('Do you want to save the file?')
    answer = input('[*]: ')
    if answer.lower() in ('y', 's', 'sim', 'yes'):
        with open('whois.txt', 'w') as f:
            f.write('teste')
        sys.exit()


            


    elif answer.lower() in ('n', 'no', 'nao', 'não', 'nope', 'nein'):
        print('OK, NOPE')
        sys.exit()
    else:
        print('Invalid.')