#!/usr/bin/env python

def critical(info):
    from core.build_menu import set_menu
    module = 'Critical Vulnerabilities'
    art=''
    menu = [ # '#' : ['module', 'description', 'function']
        ['LFI','xxx','modules.vulnysis.critical.lfi','lfi'],\
        ['RFI','xxx','modules.vulnysis.critical.rfi','rfi'],\
        ['RCE','xxx','modules.vulnysis.critical.rce','rce'],\
        ['Path Traversal','xxx','modules.vulnysis.critical.pathtrav','pathtrav'],\
        ['CSRF','xxx','modules.vulnysis.critical.csrf','csrf'],\
        ['XSS','xxx','modules.vulnysis.critical.xss','xss'],\
        ['SQLi','xxx','modules.vulnysis.critical.sqli','sqli'],\
        ['LDAP Injection','xxx','modules.vulnysis.critical.ldap','ldap'],\
        ['HTML Code Injection','xxx','modules.vulnysis.critical.htmli','htmli'],\
        ['HTTP Response Splitting','xxx','modules.vulnysis.critical.crlf','crlf'],\
        ['PHP Code Injection','xxx','modules.vulnysis.critical.phpi','phpi'],\
        ['XPATH Injection','xxx','modules.vulnysis.critical.xpathi','xpathi'],\
        ['Shellshock','xxx','modules.vulnysis.critical.shellshock','shellshock'],\
        ['Apache Struts Shock','xxx','modules.vulnysis.critical.strutsshock','strutsshock'],\
        #['URL Validation','xxx','modules.vulnysis.critical.redirect','redirect'],\
        ['Subdomain Takeover','xxx','modules.vulnysis.critical.subdomover','subdomover'],\
    ]
    set_menu(info,menu,module,art)          # build menu