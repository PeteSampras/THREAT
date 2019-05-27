#!/usr/bin/env python

# menu 3

def passive_recon(info):
    from core.build_menu import set_menu
    module = 'Passive Reconnaissance & OSINT'
    art=''
    menu = [ # '#' : ['module', 'description', 'function']
        ['HackerTarget','(Run all HackerTarget.com passive checks)','modules.recon.passive.hackertarget','hackertarget'],\
        ['dig lookup','(DIG SCAN)','modules.recon.passive.dig','dig'],\
        ['WhoIS lookup','(Gather via Interaction)','modules.recon.passive.whois','whois'],\
        ['NPING','(NPING Target)','modules.recon.passive.nping','nping'],\
        ['GeoIP Lookup','(Geographic IP Lookup)','modules.recon.passive.getgeoip','getgeoip'],\
        ['Reverse DNS Lookup','(Reverse DNS Lookup)','modules.recon.passive.revdns','revdns'],\
        ['Subnet Enumeration','(Enumerate subnets)','modules.recon.passive.subnet','subnet'],\
        ['Reverse IP Lookup','(Reverse IP Lookup)','modules.recon.passive.revip','revip'],\
        ['IP History','(Lookup previous IP addresses)','modules.recon.passive.iphistory','iphistory'],\
        ['Google Search','(Google Search)','modules.recon.passive.gsearch','gsearch'],\
        ['Check Username','(Check 160+ social media sites for username)','modules.recon.passive.checkuser','checkuser'],\
        ['LinkedIn Gathering','(Lookup LinkedIn Profiles)','modules.recon.passive.linkedin','linkedin'],\
        ['Public Contact Info','(all fullcontact.com information)','modules.recon.passive.getconinfo','getconinfo'],\
        ['CENSYS Gathering','(Gather CENSYS data if API not used up)','modules.recon.passive.censysdom','censysdom'],\
        # '5':['DNS Lookup','','dnschk'],\
        # '6':['Subdomain Scan','','subdom'],\
        # '11':['Page Links','','links'],\
        # '13':['Google Dorker','','googledorker'],\
        # '14':['Wayback Machine','','webarchive'],\
        # '15':['Hacked Email Check','','hackedmail'],\
        # '16':['Mail to Domain','','mailtodom'],\
        # '17':['Google Groups Enum','','googlegroups'],\
        # '19':['PasteBin Posts','','pastebin'],\
        # '21':['Google Plus Gathering','','googlenum'],\
        # '24':['Threat Intel Gathering','','threatintel'],\
    ]
    set_menu(info,menu,module,art)          # build menu