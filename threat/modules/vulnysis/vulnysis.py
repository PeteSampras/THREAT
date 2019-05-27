#!/usr/bin/env python

def vulnysis(info):
    from core.build_menu import set_menu
    menu = [ # '#' : ['module', 'description', 'function']
        ['Basic Bugs & Misconfigurations','(Low Priority [P0x3-P0x4])','modules.vulnysis.misconfig_bugs','misconfig'],\
        ['Critical Vulnerabilities','(High Priority [P0x1-P0x2])','modules.vulnysis.critical_bugs','critical'],\
        ['Others','(Bruter Force Tools)','modules.vulnysis.other_bugs','other'],\
    ]
    set_menu(info,menu,'Vulnerability Analysis','')          # build menu