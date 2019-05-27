#!/usr/bin/env python
import re
import sys
from core.colors import color
# from multiprocessing import Queue
from core.settings import settings

menu = [ # '#' : ['module', 'description', 'function']
        ['Reconnaissance & OSINT','Passive/Active Recon & Information Disclosure','modules.recon.recon','recon'],\
        ['Scanning & Enumeration','Port Scanning and Directory Enumeration','modules.enumeration.scanenum','scanenum'],\
        ['Vulnerability Analysis','Check for bugs, misconfigs, crit vulns, and bruters','modules.vulnysis.vulnysis','vulnysis'],\
        ['Exploitation','Exploit Modules','modules.exploitation.exploitation','exploitation'],\
        ['Auxillary Modules','Auxillary Modules','modules.aux.aux','aux'],\
        # ['Database', 'Access Stored Results', 'db_menu'],\
        # ['Settings','View/Change Settings','settings'],\
    ]

class Info(dict):
    # credit: https://paddy3118.blogspot.com/2019/05/nested-attribute-lookup-in-dicts.html?m=1
    # "Move none-hidden attribute access to dict item"
 
    def __init__(self, *args, **kwargs):
        self._extra_attr = set()
        super().__init__(*args, **kwargs)
 
    def __getattr__(self, item):
        if item[0] != '_':
            if (not super().__contains__(item)  # Its new
                or (item in self._extra_attr    # It's an attr, now None
                    and super().__getitem__(item) is None)):
                super().__setitem__(item, Info())
            return super().__getitem__(item)
        else:
            return super().__getattr__(item)
 
    def __setattr__(self, item, val):
        if item[0] != '_':
            super().__setitem__(item, val)
            self._extra_attr.add(item)
        else:
            super().__setattr__(item, val)
 
    def __dir__(self):
        "To get tooltips working"
        supr = set(super().__dir__())
        return list(supr | self._extra_attr)

if __name__=='__main__':
    # from core.build_menu import buildmenu
    info = Info(main_menu=menu,current_menu=menu)
    info.usernames=[]
    info.emails=[]
    info.hosts=[]
    info.queries=[]
    try:
        settings(info)
    except KeyboardInterrupt:
        print("Keyboard interrupted")
    finally:
        sys.exit()