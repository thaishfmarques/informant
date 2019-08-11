#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

import os.path
import shodan


def search_shodan(search):
        api = shodan.Shodan(search)
        try:
                search = input('Search: ')
                results = api.search(search)
                folder_path= './files/'
                save_to_folder = os.path.join(folder_path+'shodan.txt')
                f = open(save_to_folder, 'w')
                f.write("Results found: {}".format(results['total']))
                print ("Results found: {}".format(results['total']))
                print('File saved in ./files/shodan.txt')
                for result in results['matches']:
                        try:
                                f.write('\n')
                                f.write('IP: {}'.format(result['ip_str']))
                                f.write(' ')
                                f.write(result['ip_str'])
                                f.write(' ')
                                f.write(result['data'])
                                f.write(' ')
                        except:
                                print ("error")
                                pass

        except shodan.APIError as err_shodan:
                print('Error: {}'.format(err_shodan))

        