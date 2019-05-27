#!/usr/bin/env python

import subprocess
from core.colors import color

def nmap_menu(info):
    from core.build_menu import set_menu
    menu = [ # '#' : ['module', 'description', 'function']
        ['Run NMAP','Run your nmap string','modules.enumeration.nmap','nmap'],\
        ['Edit NMAP String','Create or Edit your NMAP String','modules.enumeration.nmap_editor','nmap_editor']
    ]

    set_menu(info,menu,'NMAP Configuration','')          # build menu