#!/usr/bin/env python

def aux(info):
    from core.build_menu import set_menu
    menu = [ # '#' : ['module', 'description', 'function']
        ['Generate Hashes','Generate Hashes from String','modules.aux.hashes','hashes'],\
        ['Encode/Decode Strings','Base64, Base32, Base16/Hex, URL','modules.aux.encodeall','encodeall'],\
        # '3':['Extract Metadata','','modules.aux.imgext','imgext'],\
        ['Honeypot Detector','Shodan Honeypot Check','modules.aux.honeypot','honeypot'],\
    ]
    set_menu(info,menu,'Aux Modules','')          # build menu