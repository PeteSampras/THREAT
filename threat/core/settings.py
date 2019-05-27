#from threat import Target, target, menu
from core.colors import color
from core.build_menu import buildmenu
import re
import sys

class Target:
    def __init__(self,value,dtype):
        self.ip=''
        self.name=''
        self.short_url=''
        self.full_url=''
        if dtype=='ip':
            self.ip=value
        else:
            self.name=value
        if '//' in value:
            self.short_url=value.split('//')[1]
            self.full_url=value
        else:
            self.short_url=value
            self.full_url = 'https://'+value


def add_host(info):
    valid_ip_regex = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    valid_host_regex = r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'
    temp = input('\n[#] Input Host/IP (ie: 192.168.10.1):> ')# DEBUG: temp value
    if '//' in temp:
        prefix=temp.split('//')[0]
        host=temp.split('//')[1]
    else:
        prefix='https'
        host=temp
    url=prefix+'//'+host
    if(re.match(valid_ip_regex, host)):
        new=Target(url,'ip')
        info.hosts.append(new)
        settings(info)
    elif(re.match(valid_host_regex, host)):
        new=Target(url,'host')
        info.hosts.append(new)
    else:
        print('fail')
        print(color.red("Invalid Host Address, try again: ")) 
    settings(info)

def add_email(info):
    email = input('[#] Input email address:> ')
    info.emails.append(email)
    print(color.yellow(email+' added'))
    settings(info)

def add_username(info):
    username = input('[#] Input username:> ')
    info.usernames.append(username)
    print(color.yellow(username+' added'))
    settings(info)

def add_query(info):
    query = input('[#] Input query term:> ')
    info.queries.append(query)
    print(color.yellow(query+' added'))
    settings(info)

def settings(info):
    hosts = []
    emails = []
    usernames = []
    queries=[]
    for host in info.hosts:
        hosts.append(host.full_url)
    for email in info.emails:
        emails.append(email)
    for user in info.usernames:
        usernames.append(user)
    for query in info.queries:
        queries.append(query)
    settings_menu = [ # '#' : ['module', 'description', 'function']
        ['Add host',str(hosts),'core.settings','add_host'],\
        ['Add email',str(emails),'core.settings','add_email'],\
        ['Add username',str(usernames),'core.settings','add_username'],\
        ['Add query',str(queries),'core.settings','add_query'],\
            # '5':['xxxx','xxx','xxx'],\
            # '6':['xxxx','xxx','xxx'],\
            # '7':['xxxx','xxx','xxx'],\
            # '8':['xxxx','xxx','xxx'],\
            # '9':['xxxx','xxx','xxx'],\
            # '10':['xxxx','xxx','xxx'],\
            # '11':['xxxx','xxx','xxx'],\
            # '12':['xxxx','xxx','xxx'],\
            # '13':['xxxx','xxx','xxx'],\
            # '14':['xxxx','xxx','xxx'],\
            # '15':['xxxx','xxx','xxx'],\
        ]
    info.settings_menu=settings_menu
    buildmenu(info,settings_menu,'Settings','')