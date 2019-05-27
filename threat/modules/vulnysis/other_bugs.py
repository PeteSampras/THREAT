#!/usr/bin/env python

def other(info):
    from core.build_menu import set_menu
    module = 'Brute Force Tools'
    art=''
    menu = [ # '#' : ['module', 'description', 'function']
        ['FTP Brute','xxx','modules.vulnysis.other.ftpbrute','ftpbrute'],\
        ['SSH Brute','xxx','modules.vulnysis.other.sshbrute','sshbrute'],\
        ['SQL Brute','xxx','modules.vulnysis.other.sqlbrute','sqlbrute'],\
        ['POP 3/2 Brute','xxx','modules.vulnysis.other.popbrute','popbrute'],\
        ['SMTP Brute','xxx','modules.vulnysis.other.smtpbrute','smtpbrute'],\
        ['TELNET Brute','xxx','modules.vulnysis.other.telnetbrute','telnetbrute'],\
        ['XMPP Brute','xxx','modules.vulnysis.other.xmppbrute','xmppbrute'],\
        #['Other Bugs','xxx','modules.vulnysis.other.othbugs.othbugs','othbugs'],\
    ]
    set_menu(info,menu,module,art)          # build menu