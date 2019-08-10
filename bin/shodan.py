#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

from shodan import Shodan
from shodan.cli.helpers import get_api_key

api = Shodan(get_api_key('KEY'))

limit = 100
counter = 0


for banner in api.search_cursor('product:mongodb'):
    print(banner['data'])

    counter +=1
    if counter >= limit:
        break