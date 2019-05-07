import os
from core.colors import color

def exit()
    print(colors.red('\n [-] Exiting...'))
    sys.exit(0)

def buildmenu(target,dict,banner,art):
    #os.system('clear')
    dictionary = OrderedDict(sorted(dict.items(), key=lambda x: int(x[0]))) 
    i=1
    print(color.blue('[+] Module Selected : ') + color.yellow(banner))
    print(art)
    print(color.yellow('\n Choose from the options below :\n'))
    for key, value in dictionary.items():
        print(color.blue(' ['+str(i)+'] '+ value[0]) + color.white(value[1]))
        i+=1
    print('\n')
    if 'Main Menu' in banner:
        print(color.blue(' [0] ') + color.red('Exit\n'))
    else:
        if not 'Aux' in banner:
            print(color.blue(' [A] ') + color.orange('Run all\n')
        print(color.custom(' [99] Back',bold=True,black=True,bg_light_grey=True))

    input_dirty = raw_input('[#] Choose Option:> ')
    choice = input_dirty.strip()
    found = False
    if choice == '0': # exit
        exit()
    elif choice == '99': # go back
        os.system('clear')
    elif choice == 'A' or 'a':
        for key, value in dictionary.items():
            results=all_functions[value[2]](target)
        found = True
    else:
        for key, value in dictionary.items():
            if str(choice) == str(key): # select option
                if 'Aux' in banner:
                    results=all_functions[value[2]]
                else:
                    results=all_functions[value[2]](target)
                found = True
                break

    if found == False:
        print(color.red('Invalid selection.'))
        pass
