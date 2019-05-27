#!/usr/bin/env python

def info_disclosure(info):
    from core.build_menu import set_menu
    module = 'Information Disclosure'
    art=''
    menu = [ # '#' : ['module', 'description', 'function']
        ['Credit Card Enumeration','(If disclosed in plain text)','modules.recon.info.creditcards','creditcards'],\
        # '2':['Extract All Emails','(Absolute)','emailext'],\
        ['Enumerate Errors + FPD','(Includes Full Path Disclosure)','modules.recon.info.errors','errors'],\
        # '4':['Internal IP disclosure','(Find out any leaks of internal IP addresses)','internalip'],\
        # '5':['Extract out all Phone Numbers','(If plaintext disclosure)','phone'],\
        # '6':['Extract out all Social Security Numbers','(US Based)','ssn']
    ]
    set_menu(info,menu,module,art)          # build menu