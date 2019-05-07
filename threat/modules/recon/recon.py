#!/usr/bin/env python

def recon(target):
    print('recon')
    from core.build_menu import buildmenu
    menu = { # '#' : ['module', 'description', 'function']
        '1':['Passive Footprinting','(Open Source Intelligence)','xxx'],\
        '2':['Active Reconnaissance','(Gather via Interaction)','xxx'],\
        '3':['Information Disclosure','(Errors, Emails, etc)','xxx'],\
    }
    buildmenu(target,menu,'Reconnaissancea & OSINT','')          # build menu