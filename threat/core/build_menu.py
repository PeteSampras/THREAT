#!/usr/bin/env python
from .colors import color
from collections import OrderedDict
import importlib

class Menu:
    def __init__(self,name,description,module,function):
        self.name=name
        self.description=description
        self.module=module
        self.function=function

def set_menu(info,menu,banner,art):
    info.previous_menu = info.current_menu
    info.current_menu = menu
    info.previous_banner=info.banner
    info.banner=banner
    info.previous_art = info.art
    info.art = art
    buildmenu(info,menu,banner,art)

def build_banner(banner):
    size = len(banner)*2 + 4
    padding = "".join("=" for i in range(size))
    letters = "| "
    for letter in banner:
        letters = letters + color.yellow(letter.upper()) + " "
    letters = letters + color.blue(" |")
    print(color.blue(padding))
    print(color.blue(letters))
    print(color.blue(padding))

def buildmenu(info,menu,banner,art):
    
    current={}
    i=1
    print(color.green(' [+] ')+color.blue('Module Selected: ') + color.yellow(banner)+'\n')
    for item in menu:
        try:
            module = importlib.import_module(item[2], package=[item[3]])
            new=Menu(item[0],item[1],module,item[3])
            current[i]=new
            i=i+1
        except Exception as e:
            print('Exception: '+e)
    dictionary = OrderedDict(sorted(current.items(), key=lambda x: int(x[0])))
    i=1
    for key, value in dictionary.items():
        print(color.green(' ['+str(i)+'] ') + color.blue(value.name) + " - " + color.custom(value.description, white=True))
        i+=1
    if 'Main Menu' in banner:
        print(color.green('\n [S] ') + color.yellow('Settings'))
        print(color.green(' [P] ') + color.yellow('Multiprocess Queue ') + color.custom('- Check Status of Multiprocesses\n',reset=True,white=True))
    else:
        if not 'Settings' in banner: # DEBUG: might want to not run all on a sub menu
            print(color.green('\n [A] ') + color.yellow('Run all'))
            print(color.green(' [S] ') + color.yellow('Settings'))
        print(color.green('\n [M] ') + color.yellow('Main Menu'))
        print(color.green(' [H] ') + color.yellow('Help\n'))
    print(" " + color.custom('[B] Back',bold=True,white=True,bg_blue=True)+'\n')
    print(" " + color.custom('[0] Exit',bold=True,white=True,bg_red=True)+'\n')
    try:
        choice = input('[#] Choose Option:> ')
        found = False
        if choice == '0': # exit
            exit()
        elif choice.lower() == 'b': # go back
            found = True
            set_menu(info,info.previous_menu,info.previous_banner,info.previous_art)
        elif choice.lower() == 'a':
            # for key, value in dictionary.items():
            #     target[0].module = value[0]
            #     target[0].description = value[1]
            #     build_banner(value[0].replace('(','').replace(')',''))
            #     try:
            #         multi(multiprocess_functions[value[2]],target)
            #     except Exception as e:
            #         pass
            #     finally:
            #         pass
            found = True
        elif choice.lower() == 'm':
            found = True
            set_menu(info,info.main_menu,'Main Menu','')
        elif choice.lower() == 's':
            found = True
            set_menu(info,info.settings_menu,'Settings','')
        elif choice.lower() == 'p':
            found = True
            # print('Process Status', processes)
            # # print('THREAT TASKS TO ACCOMPLISH QUEUE', tasks_to_accomplish.qsize())
            # # print('THREAT TASKS DONE QUEUE', tasks_that_are_done.qsize())

            # ########## These multiprocess prints with color break the menu ##########
            # # print('\n ' + color.green('[+] ') + color.blue('Status of Processes: ') + color.custom(processes,reset=True,white=True))
            # # print('\n ' + color.green('[+] ') + color.blue('Tasks to Accomplish Queue Size: ') + color.custom(tasks_to_accomplish.qsize(),reset=True,white=True))
            # # print('\n ' + color.green('[+] ') + color.blue('Tasks that are done Queue Size: ') + color.custom(tasks_that_are_done.qsize(),reset=True,white=True))
            # ########## These multiprocess prints with color break the menu ##########
            # buildmenu(target,target[0].main_menu,'Main Menu','')
        elif choice.lower() == 'h':
            found = True
            # if target[0].help == '':
            #     target[0].current_menu=target[0].last_menu
            #     art=color.red('\nInvalid selection. ') + color.blue('Help') + color.red(' is not implemented yet.\n')
            #     buildmenu(target,dict,banner,art)
            # if target[0].help.split('/')[1] == 'Photon':        # WORKING
            #     print(color.green('INFO: Grabbing Photon Help Page'))
            #     get_help = target[0].help + ' -h'
            #     # subprocess.run(get_help, shell=True)
            #     # buildmenu(target,dict,banner,art)
            # if target[0].help == 'nikto':       # DO NOT RUN
            #     print(color.green('INFO: Grabbing Nikto Help Page'))
            #     get_help = target[0].help + ' -H'
            #     # subprocess.run('nikto -H', shell=True)
            #     # buildmenu(target,dict,banner,art)

            # subprocess.run(get_help, shell=True)
            # buildmenu(target,dict,banner,art)
        else:
            for key, value in dictionary.items():
                if str(choice) == str(key): # select option
                    if 'Temp if statement in case dont want to pass target' in banner: # DEBUG: Might use this option
                        #results=functions[value[2]]
                        pass
                    else:
                        build_banner(value.name.replace('(','').replace(')',''))
                        mp = False
                        # try:
                        #     multi(multiprocess_functions[value[2]],target)
                        #     mp = True
                        #     buildmenu(target,target[0].main_menu,'Main Menu','')
                        # except Exception as e:
                        #     pass
                        # finally:
                        #     pass
                        if mp ==False:
                            try:
                                results = getattr(value.module,value.function)(info)
                            except Exception as e:
                                print(color.red('\nInvalid selection. ') + color.blue(value[0]) + color.red(' is not implemented yet.\n'))
                                set_menu(info,info.previous_menu,info.previous_banner,info.previous_art)
                            finally:
                                pass
                    found = True
                    break

        if found == False:
            print(color.red('Invalid selection.'))
            pass
    except EOFError as e:
        pass    