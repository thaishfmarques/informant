#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# author: @thaishfmarques

# TODO: Importing order: System imports Third-party imports Local source tree imports

'''
Todas as informações de utilização do programa e funções estão disponíveis em
informant/bin/doc e informant/README.md

Comentários gerais em inglês por questões de comunidade
Demais comentários em português por questões acadêmicas
'''

import banner


try:
    menu_option=''
    banner.menu_splash(menu_option)
except KeyboardInterrupt as kboard:
    print('\nExiting...')


