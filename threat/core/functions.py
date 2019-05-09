#!/usr/bin/env python
from modules.recon.recon import recon
from modules.enumeration.scanenum import scanenum
from modules.exploitation.exploitation import exploitation
from modules.vulnysis.vulnysis import vulnysis
from modules.recon.passive_recon import passive_recon
from modules.recon.dig import dig
from modules.recon.whois import whois
from modules.recon.nping import nping
from modules.recon.getgeoip import getgeoip
from modules.recon.iphistory import iphistory
from modules.recon.revdns import revdns
from modules.recon.revip import revip
from modules.recon.subnet import subnet
from modules.recon.linkedin import linkedin
from modules.recon.gsearch import gsearch

functions = {
    'recon':recon,
    'scanenum':scanenum,
    'exploitation':exploitation,
    'vulnysis':vulnysis,
    #'post':post

    # recon related
    'passive_recon':passive_recon,
    #'active_recon':active_recon,
    #'infodisc':infodisc,

    #'dig':dig,
    #''
}

multiprocess_functions = { 
    'dig':dig,
    'whois':whois,
    'nping':nping,
    'getgeoip':getgeoip,
    'iphistory':iphistory,
    'revdns':revdns,
    'revip':revip,
    'subnet':subnet,
    'linkedin':linkedin,
    'gsearch':gsearch,
}