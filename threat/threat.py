#!/usr/bin/env python
import sys
from core.build_menu import buildmenu

menu = { # '#' : ['module', 'description', 'function']
        '1':['Reconnaissance & OSINT','Description','recon'],\
        '2':['Scanning & Enumeration','Description','scanenum'],\
        '3':['Vulnerability Analysis','Description','vulnysis'],\
        '4':['Exploitation','Description','exploit'],\
        '5':['Post Analysis','Description','post']\
    }

def threat():
    while True:
        try:
            target = 'www.example.com'
            buildmenu(target,menu,'Main Menu','')
        except KeyboardInterrupt:
            print("Keyboard interrupted")
        finally:
            sys.exit()

if __name__=='__main__':
    try:
        threat()
    except KeyboardInterrupt:
        print("Keyboard interrupted")
    finally:
        sys.exit()
