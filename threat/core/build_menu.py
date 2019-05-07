#!/usr/bin/env python
import os
import sys
from core.colors import color
from collections import OrderedDict
from core.functions import functions

def exit():
    print(color.red(' [-] Exiting...'))
    sys.exit(0)

def buildmenu(target,dict,banner,art):
    #os.system('clear')
    dictionary = OrderedDict(sorted(dict.items(), key=lambda x: int(x[0]))) 
    i=1
    print(color.blue('[+] Module Selected : ') + color.yellow(banner))
    print(art)
    print(color.yellow(' Choose from the options below:\n'))
    for key, value in dictionary.items():
        print(color.green(' ['+str(i)+'] ') + color.blue(value[0]) + " - " + color.custom(value[1], white=True))
        i+=1
    if 'Main Menu' in banner:
        print('\n ' + color.custom('[0] Exit',bold=True,white=True,bg_red=True)+'\n')
    else:
        if not 'Aux' in banner:
            print('\n'+color.green(' [A] ') + color.yellow('Run all\n'))
        print(" " + color.custom('[B] Back',bold=True,white=True,bg_red=True)+'\n')

    choice = input('[#] Choose Option:> ')
    found = False
    if choice == '0': # exit
        exit()
    elif choice.lower() == 'b': # go back
        os.system('clear')
    elif choice.lower() == 'a':
        for key, value in dictionary.items():
            results=functions[value[2]](target)
        found = True
    else:
        for key, value in dictionary.items():
            if str(choice) == str(key): # select option
                if 'Aux' in banner:
                    results=functions[value[2]]
                else:
                    results=functions[value[2]](target)
                found = True
                break

    if found == False:
        print(color.red('Invalid selection.'))
        pass
