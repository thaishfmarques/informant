#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import requests

def requests_get(url, param):
    response = requests.get(url + param)
    if response.status_code == 200:
        print(response.text)
    else:
        requests.post()