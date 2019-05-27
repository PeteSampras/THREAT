#!/usr/bin/env python

def misconfig(info):
    from core.build_menu import set_menu
    module = 'Misconfigurations and Lower Priority Vulnerabilities'
    art=''
    menu = [ # '#' : ['module', 'description', 'function']
        ['iCORS','xxx','modules.vulnysis.misconfig.icors','icors'],\
        ['Same Site Scripting','xxx','modules.vulnysis.misconfig.ssscript','ssscript'],\
        ['Clickjack','xxx','modules.vulnysis.misconfig.clickjack','clickjack'],\
        ['Zone Transfer','xxx','modules.vulnysis.misconfig.zone','zone'],\
        ['Cookie Check','xxx','modules.vulnysis.misconfig.cookiecheck','cookiecheck'],\
        ['Sec. Headers','xxx','modules.vulnysis.misconfig.headers','headers'],\
        ['Cloudflare Misconfig','xxx','modules.vulnysis.misconfig.cloudflaremisc','cloudflaremisc'],\
        ['HSTS Check','xxx','modules.vulnysis.misconfig.hsts','hsts'],\
        ['Cross Site Tracing','xxx','modules.vulnysis.misconfig.xsstrace','xsstrace'],\
        ['Telnet Enabled','xxx','modules.vulnysis.misconfig.netmisc','netmisc'],\
        ['Email Spoof','xxx','modules.vulnysis.misconfig.mailspoof','mailspoof'],\
        ['Host Header Injection','xxx','modules.vulnysis.misconfig.hhi','hhi'],\
        ['Cookie Injection','xxx','modules.vulnysis.misconfig.sessionfix','sessionfix'],\
    ]
    set_menu(info,menu,module,art)          # build menu