#!/usr/bin/env python

def active_recon(info):
    from core.build_menu import set_menu
    module = 'Active Reconnaissance'
    art=''
    menu = [ # '#' : ['module', 'description', 'function']
        # '1':['Ping/NPing Enumeration','xxx','piwebenum'],\
        # '2':['Grab HTTP Headers','xxx','grabhead'],\
        # '3':['HTTP Allowed Methods','xxx','httpmethods'],\
        ['robots.txt/sitemap.xml Hunt','Checks for public site data','modules.recon.active.robot','robot'],\
        # '5':['Scrape Comments','xxx','commentssrc'],\
        # '6':['Traceroute','xxx','traceroute'],\
        # '7':['DNS Hosts','xxx','sharedns'],\
        # '8':['SSL Certificate','xxx','sslcert'],\
        # '9':['CMS Detection','xxx','cms'],\
        # '10':['Apache Status','xxx','apachestat'],\
        # '11':['WebDAV HTTP Enumeration','xxx','dav'],\
        # '12':['PHPInfo Enumeration','xxx','phpinfo'],\
        # '13':['Server Detection','xxx','serverdetect'],\
        ['Alternate Sites','Check for alternate sites based on browser','modules.recon.active.altsites','altsites'],\
        # '15':['File Bruteforcers','xxx','filebrute'],\
    ]
    set_menu(info,menu,module,art)          # build menu