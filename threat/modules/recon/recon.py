#!/usr/bin/env python

def recon(info):
    from core.build_menu import set_menu
    menu = [ # '#' : ['module', 'description', 'function']
        ['Passive Reconnaissance','(Open Source Intelligence)','modules.recon.passive_recon','passive_recon'],\
        ['Active Reconnaissance','(Gather via Interaction)','modules.recon.active_recon','active_recon'],\
        ['Information Disclosure','(Errors, Emails, etc)','modules.recon.infodisc','info_disclosure'],\
    ]
    set_menu(info,menu,'Reconnaissance & OSINT','')