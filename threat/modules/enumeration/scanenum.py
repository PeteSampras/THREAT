#!/usr/bin/env python

# menu 2

def scanenum(target):
    from core.build_menu import set_menu
    menu = [ # '#' : ['module', 'description', 'function']
        #['Ping Sweep','(Scan a range of targets/IPs)','modules.enumeration.misconfig_bugs','xxx'],\
        ['Port Scanning','(Various port scan types)','modules.enumeration.nmap_menu','nmap_menu'],\
        ['Crawling','(Public and Brute Force methods)','modules.enumeration.photon_menu','photon_menu'],\
        ['Nikto Menu','(Web Server Vulnerability Scans Menu)','modules.enumeration.nikto_menu','nikto_menu'],\
        # '5':['Windows Enumeration','(Windows Specific Enumeration)','windows_enum'],\
    ]
    set_menu(target,menu,'Scanning and Enumeration','')          # build menu