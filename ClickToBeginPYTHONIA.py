import colorama
from colorama import init, Fore, Style
import random
import winsound
import time
import sys
from sys import exit
init()
#starting values for globals
key = False
rustswd = False
items = False
playgame = False
fightmon = False
furslime = False
playerlocation = 1
monster = 0
monsterhp = 0
playrhp = 200
oneeye = False
wine = False
free = False
part1over = False
heal = False
talking = False
getgold = False
guard = False
runfrombeast = False
runfromdraco = False
telltruth = 3
displaybegin = False
meds = False
startgame = True
claymore = False
player = str("UNKNOWN_NAME")
playerchoi = str("UNKNOWN_ENTRY")
def ingamemusic(song):
    if song == 1:
        winsound.PlaySound("Music/titlescreen1.wav", winsound.SND_ASYNC)
    elif song == 2:
        winsound.PlaySound("Music/overworld2.wav", winsound.SND_ASYNC)
    elif song == 3:
        winsound.PlaySound("Music/cave_forest3.wav", winsound.SND_ASYNC)
    elif song == 4:
        winsound.PlaySound("Music/battle!4.wav", winsound.SND_ASYNC)
    elif song == 5:
        winsound.PlaySound("Music/ending5.wav", winsound.SND_ASYNC)
    elif song == 6:
        winsound.PlaySound("Music/dracoencounter6.wav", winsound.SND_ASYNC)
    elif song == 7:
        winsound.PlaySound("Music/VICTORY.wav", winsound.SND_ASYNC)
    elif song == 8:
        winsound.PlaySound("Music/DEFEAT.wav", winsound.SND_ASYNC)
#display location function
def printlocation (location):
    if location == 1:
        print(Style.DIM)
        print(Fore.GREEN + "               ,@@@@@@@,")
        print(Fore.GREEN + "       ,,,.   ,@@@@@@" + Fore.RED + "/" + Fore.GREEN + "@@,  .oo8888o.")
        print(Fore.GREEN + "    ,&%%&%&&%,@@@@@/@@@@@@,8888" + Fore.RED + "\ " + Fore.GREEN + "88" + Fore.RED + "/" + Fore.GREEN + "8o")
        print(Fore.GREEN + "   ,%&" + Fore.RED + "\"" + Fore.GREEN + "%&&%&&%,@@@" + Fore.RED + "\ " + Fore.GREEN + "@@@" + Fore.RED + "/" + Fore.GREEN + "@@@88" + Fore.RED + "\ " + Fore.GREEN + "88888" + Fore.RED + "/" + Fore.GREEN + "88'")
        print(Fore.GREEN + "   %&&%" + Fore.RED + "/" + Fore.GREEN + " %&%%&&@@" + Fore.RED + "\ V /" + Fore.GREEN + "@@' `88" + Fore.RED + "\ " + Fore.GREEN + "8 `" + Fore.RED + "/" + Fore.GREEN + "88'")
        print(Fore.GREEN + "   `&%" + Fore.RED + "\ ` /" + Fore.GREEN + "%&'    " + Fore.RED + "|.|        \ '|" + Fore.GREEN + "8'")
        print(Fore.RED + "       |o|        | |         | |")
        print(Fore.RED + "       |.|        | |         | |")
        print(Fore.GREEN + "   \ \\" + Fore.RED + "/ ._\ " + Fore.GREEN + "//_/_" + Fore.RED + "/  ,\ " + Fore.GREEN + "_//_\ " + Fore.RED + "/.  \ " + Fore.GREEN + "_//__/_" + Style.RESET_ALL)
        if displaybegin == True:
            print(Fore.YELLOW + " >You wander your way back to where you began." + Style.RESET_ALL)
    elif location == 2:
        print(Style.DIM)
        print(Fore.GREEN + "                      ___ ")
        print(Fore.GREEN + "                _,-'\"\"   \"\"\"\"`--. ")
        print(Fore.GREEN + "             ,-'          __,,-- \ ")
        print(Fore.GREEN + "           ,'    __,--\"\"\"\"" + Fore.RED + "dF" + Fore.GREEN + "      ) ")
        print(Fore.GREEN + "          /   .-\"" + Fore.RED + "Hb" + Fore.GREEN + ",--\"\"" + Fore.RED + "dF" + Fore.GREEN + "      / ")
        print(Fore.GREEN + "        ,'       _" + Fore.RED + "Hb" + Fore.GREEN + " ___" + Fore.RED + "dF" + Fore.GREEN + "\"-._,-' ")
        print(Fore.GREEN + "      ,'      _,-\"\"\"\"   \"\"--..__ ")
        print(Fore.GREEN + "     (     ,-'                  `. ")
        print(Fore.GREEN + "      `._,'     _   _             ; ")
        print(Fore.GREEN + "       ,'     ,' `-'" + Fore.RED + "Hb" + Fore.GREEN + "-.___..._,-' ")
        print(Fore.GREEN + "       \    ,'" + Fore.RED + "\"Hb" + Fore.GREEN + ".-'" + Fore.RED + "HH" + Fore.GREEN + "`-." + Fore.RED + "dHF\" ")
        print(Fore.GREEN + "        `--'   " + Fore.RED + "\"Hb  HH  dF\" ")
        print(Fore.RED + "                \"Hb HH dF ")
        print(Fore.RED + "                 \"HbHHdF ")
        print(Fore.RED + "                  |HHHF ")
        print(Fore.RED + "                  |HHH| ")
        print(Fore.RED + "                  |HHH| ")
        print(Fore.RED + "                  |HHH| ")
        print(Fore.RED + "                  |HHH| ")
        print(Fore.RED + "                  dHHHb ")
        print(Fore.RED + "                .dFd|bHb.               " + Fore.YELLOW + Style.BRIGHT + "o " + Style.DIM)
        print(Fore.RED + "      " + Fore.YELLOW + Style.BRIGHT + "o" + Fore.RED + Style.DIM + "       .dHFdH|HbTHb.          " + Fore.YELLOW + Style.BRIGHT + "o" + Fore.GREEN + Style.DIM + " / ")
        print(Fore.GREEN + "\  Y  |  \__," + Fore.RED + "dHHFdHH|HHhoHHb" + Fore.GREEN + "._        Y " + Style.RESET_ALL)
        print(Fore.GREEN + Style.DIM + "########################################## ")
        print(Style.RESET_ALL + Fore.YELLOW +" >You venture deeper into the forest." + Style.RESET_ALL)
    elif location == 3:
        print(Fore.GREEN + "    &&& ")
        print(Fore.GREEN + "   &&&/& ")
        print(Fore.GREEN + " &\/&|&&&& ")
        print(Fore.GREEN + "&&&\&|&/&&& ")
        print(Fore.GREEN + " &&&\|/&&& ")
        print(Fore.GREEN + "  & }}{ & ")
        print(Fore.GREEN + "    }{{ ")
        print (Fore.YELLOW +" >The trees begin to thin, revealing an open grassland with scattered shrubbery." + Style.RESET_ALL)
    elif location == 4:
        print(Style.DIM)
        print("                                  _")
        print("                        .-.      / \        _")
        print("            " + Style.RESET_ALL + "^^" + Style.DIM + "         /   \    /" + Style.RESET_ALL + "^" + Style.DIM + "./\__   _/ \ ")
        print("          _        .--'\/\_ \__/.      \ /    \  " + Style.RESET_ALL + "^^" + Style.DIM + "  ___")
        print("         / \_    _/ " + Style.RESET_ALL + "^" + Style.DIM + "      \/  __  :'   /\/\  /\  __/   \ ")
        print("        /    \  /    .'   _/  /  \   " + Style.RESET_ALL + "^" + Style.DIM + " /    \/  \/ .`'\_/\ ")
        print("       /\/\  /\/ :' __  " + Style.RESET_ALL + "^" + Style.DIM + "/  " + Style.RESET_ALL + "^" + Style.DIM + "/    `--./.'  " + Style.RESET_ALL + "^" + Style.DIM + "  `-.\ _    _:\ _")
        print("      /    \/  \  _/  \-' __/.' " + Style.RESET_ALL + "^" + Style.DIM + " _   \_   .'\   _/ \ .  __/ \ ")
        print("    /\  .-   `. \/     \ / -.   _/ \ -. `_/   \ /    `._/  " + Style.RESET_ALL + "^" + Style.DIM + "  \ ")
        print("   /  `-.__ " + Style.RESET_ALL + "^" + Style.DIM + "   / .-'.--'    . /    `--./ .-'  `-.  `-. `.  -  `.")
        print(" @/        `.  / /      `-.   /  .-'   / .   .'   \    \  \  .-  \%")
        print(Fore.GREEN + " @(88%@)@%% @)&@&(88&@." + Style.BRIGHT + Fore.BLUE + "-_=_-=_-=_-=_-=_." + Style.DIM + Fore.GREEN + "8@% &@&&8(8%@%8)(8@%8 8%@)%")
        print(Fore.GREEN + " @88" + Fore.YELLOW + ":::" + Fore.GREEN + "&(&8&&8" + Fore.YELLOW + "::" + Fore.GREEN + "JGS:&`." + Style.BRIGHT + Fore.BLUE + "~-_~~-~~_~-~_~-~~=." + Style.DIM + Fore.GREEN + "'@(&%" + Fore.YELLOW + "::::" + Fore.GREEN + "%@8&8)" + Fore.YELLOW + "::" + Fore.GREEN + "&#@8" + Fore.YELLOW + "::::")
        print(Fore.YELLOW + " `::::::" + Fore.GREEN + "8%@@%" + Fore.YELLOW + ":::::" + Fore.GREEN + "@%&8:`." + Style.BRIGHT + Fore.BLUE + "=~~-.~~-.~~=..~" + Style.DIM + Fore.GREEN + "'8" + Fore.YELLOW + "::::::::" + Fore.GREEN + "&@8" + Fore.YELLOW + ":::::" + Fore.GREEN + "&8" + Fore.YELLOW + "::::::'")
        print(Fore.YELLOW + "  `::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'" + Style.RESET_ALL)
        print(Fore.YELLOW + " >You take a brief pause to rest near a cliff overlooking the Burmese mountains." + Style.RESET_ALL)
    elif location == 5:
        print(Style.DIM + "                    /   \              /'\       _                              ")
        print("\_..           /'.,/     \_         .,'   \     / \_                            ")
        print("    \         /            \      _/       \_  /    \     _                     ")
        print("     \__,.   /              \    /           \/.,   _|  _/ \                    ")
        print("          \_/                \  /',.,''\      \_ \_/  \/    \                   ")
        print("                           _  \/   /    ',../',.\    _/      \                  ")
        print("             /           _/" + Style.BRIGHT + Fore.BLACK + "m" + Style.RESET_ALL + Style. DIM + "\  \  /    |         \  /.,/'\   _\                 ")
        print("           _/           /" + Style.BRIGHT + Fore.BLACK + "MMmm" + Style.RESET_ALL + Style. DIM + "\  \_     |          \/      \_/  \                ")
        print("          /      \     |" + Style.BRIGHT + Fore.BLACK + "MMMMmm" + Style.RESET_ALL + Style. DIM + "|   \__   \          \_       \   \_              ")
        print("                  \   /" + Style.BRIGHT + Fore.BLACK + "MMMMMMm" + Style.RESET_ALL + Style. DIM + "|      \   \           \       \    \             ")
        print("                   \  |" + Style.BRIGHT + Fore.BLACK + "MMMMMMmm" + Style.RESET_ALL + Style. DIM + "\      \___            \_      \_   \            ")
        print("                    \|" + Style.BRIGHT + Fore.BLACK + "MMMMMMMMmm" + Style.RESET_ALL + Style. DIM + "|____.'  /\_            \       \   \_          ")
        print("                    /'.,___________...,,'   \            \   \        \         ")
        print("                   /       \          |      \    |__     \   \_       \        ")
        print("                 _/        |           \      \_     \     \    \       \_      ")
        print("                /                               \     \     \_   \        \     ")
        print("                                                 \     \      \   \__      \    ")
        print("                                                  \     \_     \     \      \   ")
        print("                                                   |      \     \     \      \  ")
        print("                                                    \            |            \ " + Style.RESET_ALL)
        print(Fore.YELLOW + " >You begin the hike up Mount Burmese and see a small cave in the distance." + Style.RESET_ALL)
    elif location == 6 or location == 7:
        print(Style.DIM +"                  _________________")
        print("             ____/" + Style.BRIGHT + Fore.BLACK + "#################" + Style.RESET_ALL + Style. DIM + "\____")
        print("         ___/" + Style.BRIGHT + Fore.BLACK + "###########################" + Style.RESET_ALL + Style. DIM + "\___    ")
        print("       _/" + Style.BRIGHT + Fore.BLACK + "###################################" + Style.RESET_ALL + Style. DIM + "\_  ")
        print("      /" + Style.BRIGHT + Fore.BLACK + "#######################################" + Style.RESET_ALL + Style. DIM + "\ ")
        print("     /" + Style.BRIGHT + Fore.BLACK + "#########################################" + Style.RESET_ALL + Style. DIM + "\ ")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("    |" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|")
        print("\ | /" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "| \ | /")
        print("_\|/|" + Style.BRIGHT + Fore.BLACK + "###########################################" + Style.RESET_ALL + Style. DIM + "|__\|/___" + Style.RESET_ALL)
        print(Fore.YELLOW + " >The cave is eerily silent compared to the roaring winds of the mountains." + Style.RESET_ALL)
    elif location == 8:
        print(Fore.YELLOW + " >Its so dark, you can barely see anything!" + Style.RESET_ALL)
        if part1over == True:
            print(Fore.YELLOW + " >The kind plainsman is preparing for the trek back home." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + " >The figure, which appears to be a farmer, struggles in his bindings at the sight of you." + Style.RESET_ALL)
    elif location == 9:
        print(Style.DIM + Fore.GREEN)
        print("          &&& &&  & &&")
        print("      && &\/&\|& ()|/ @, &&")
        print("      &\/(/&/&||/& /_/)_&/_&")
        print("   &() &\/&|()|/&\/ '%\" & ()")
        print("  &_\_&&_\ |& |&&/&__%_/_& &&")
        print("&&   && & &| &| /& & % ()& /&&")
        print(" ()&_---()&\&\|&&-&&--%---()~")
        print("     &&     " + Fore.RED + "\|||")
        print("             |||")
        print("             |||")
        print("             |||")
        print("       , -=-~  .-^- _")
        print("              `" + Style.RESET_ALL)
        print(Fore.YELLOW + " >Trees seem to close around you as the forest swirls with a foggy aura." + Style.RESET_ALL)
    elif location == 10 or location == 11 or location == 12:
        print("                                             " + Fore.RED + Style.DIM + "__")
        print("                  |                          TT" + Style.RESET_ALL + "  )   )                   " + Fore.RED + Style.DIM + "|  ")
        print("                 " + Style.RESET_ALL + Fore.YELLOW + "/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\                         " + Fore.RED + Style.DIM + "||" + Style.RESET_ALL + "  )   )                  " + Style.RESET_ALL + Fore.YELLOW + "/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\  ")
        print("                " + Style.RESET_ALL + Fore.YELLOW + "/ " + Fore.RED + Style.DIM + "L " + Style.RESET_ALL + Fore.YELLOW + "\                        " + Fore.RED + Style.DIM + "||" + Style.RESET_ALL + "-^--^-'                 " + Style.RESET_ALL + Fore.YELLOW + "/ " + Fore.RED + Style.DIM + "L " + Style.RESET_ALL + Fore.YELLOW + "\  ")
        print("               " + Style.RESET_ALL + Fore.YELLOW + "/ " + Fore.RED + Style.DIM + "[O] " + Style.RESET_ALL + Fore.YELLOW + "\                       " + Fore.RED + Style.DIM + "||                       " + Style.RESET_ALL + Fore.YELLOW + "/ " + Fore.RED + Style.DIM + "[O]" + Style.RESET_ALL + Fore.YELLOW + " \  ")
        print("              " + Style.RESET_ALL + Fore.YELLOW + "/   " + Fore.RED + Style.DIM + "T   " + Style.RESET_ALL + Fore.YELLOW + "\                  _.+'" + Fore.RED + Style.DIM + "||" + Style.RESET_ALL + Fore.YELLOW + "'+._                  /   " + Fore.RED + Style.DIM + "T   " + Style.RESET_ALL + Fore.YELLOW + "\  ")
        print("             |____" + Fore.RED + Style.DIM + "|" + Style.RESET_ALL + Fore.YELLOW + "____|             _.+'____/\____'+._             |____" + Fore.RED + Style.DIM + "|" + Style.RESET_ALL + Fore.YELLOW + "____|  ")
        print("               " + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "|" + Style.RESET_ALL + "[_]              [_]" + Style.RESET_ALL + Fore.YELLOW + "_____" + Style.RESET_ALL + "[" + Fore.RED + Style.DIM + "||" + Style.RESET_ALL + "]" + Style.RESET_ALL + Fore.YELLOW + "_____" + Style.RESET_ALL + "[_]              [_]" + Fore.RED + Style.DIM + "|" + Style.RESET_ALL + "[_]  ")
        print("              ." + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "|" + Style.RESET_ALL + "[_].             [_]" + Style.RESET_ALL + Fore.YELLOW + "_____" + Style.RESET_ALL + "[" + Fore.RED + Style.DIM + "||" + Style.RESET_ALL + "]" + Style.RESET_ALL + Fore.YELLOW + "_____" + Style.RESET_ALL + "[_]             .[_]" + Fore.RED + Style.DIM + "|" + Style.RESET_ALL + "[_].  " + Style.RESET_ALL + Fore.YELLOW + " ")
        print("      ._._._._|" + Fore.RED + Style.DIM + "IIIIIII" + Style.RESET_ALL + Fore.YELLOW + "|._._._._.___." + Fore.RED + Style.DIM + "====================" + Style.RESET_ALL + Fore.YELLOW + ".___._._._._.|" + Fore.RED + Style.DIM + "IIIIIII" + Style.RESET_ALL + Fore.YELLOW + "|_._._._.  ")
        print("     /|\._./\|/   " + Fore.RED + Style.DIM + "L" + Style.RESET_ALL + Fore.YELLOW + "   \|/._._.\|" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + " \/   \\" + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "/   \/ " + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "|/._._.\|/   " + Fore.RED + Style.DIM + "L" + Style.RESET_ALL + Fore.YELLOW + "   \|/\._./|\  ")
        print("    " + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "TTTTTTT" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "==[O]==" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "TTTTTTTT" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + " /\_._." + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "_" + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + "_" + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "._._/\ " + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "TTTTTTTT" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "==[O]==" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "TTTTTTT" + Style.RESET_ALL + "[]  ")
        print("    []" + Style.RESET_ALL + Fore.YELLOW + "|._._.|" + Style.RESET_ALL + "[]   " + Fore.RED + Style.DIM + "T   " + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + "._./\._." + Style.RESET_ALL + "[_]" +Fore.YELLOW + "/  " + Style.RESET_ALL + "[__]" + Fore.YELLOW + "/  ||  \\" + Style.RESET_ALL + "[__]  " + Fore.YELLOW + "\\" + Style.RESET_ALL + "[_]" + Fore.YELLOW + "._./\._." + Style.RESET_ALL + "[]   " + Fore.RED + Style.DIM + "T   " + Style.RESET_ALL + "[]" + Fore.YELLOW + "|._._.|" + Style.RESET_ALL + "[]  ")
        print("    []" + Fore.RED + Style.DIM + "IIIIIII" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "IIIIIII" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "IIIIIIII" + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "===" + Style.RESET_ALL + "[__]" + Style.RESET_ALL + Fore.YELLOW + "\._||_./" + Style.RESET_ALL + "[__]" + Fore.RED + Style.DIM + "===" + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "IIIIIIII" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "IIIIIII" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "IIIIIII" + Style.RESET_ALL + "[]  ")
        print("   /" + Style.RESET_ALL + Fore.YELLOW + "|" + Fore.RED + Style.DIM + "--------" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "-------" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "--------" + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "---" + Style.RESET_ALL + "[__]" + Style.RESET_ALL + Fore.YELLOW + "-+=" + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "=+-" + Style.RESET_ALL + "[__]" + Fore.RED + Style.DIM + "---" + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "--------" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "-------" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "--------" + Style.RESET_ALL + "|" + Style.RESET_ALL + Fore.YELLOW + "\  ")
        print("  /" + Style.RESET_ALL + Fore.YELLOW + "|" + Style.RESET_ALL + "| _/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\_  " + Style.RESET_ALL + "||" + Fore.YELLOW + "\\\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_//" + Style.RESET_ALL + "||  " + Fore.YELLOW + "_/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\_ " + Style.RESET_ALL + "[_]    " + Fore.YELLOW + "\_\_/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\_/_/    " + Style.RESET_ALL + "[_] " + Fore.YELLOW + "_/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\_  " + Style.RESET_ALL + "||" + Fore.YELLOW + "\\\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_//" + Style.RESET_ALL + "||" + Style.RESET_ALL + Fore.YELLOW + "  _/" + Fore.RED + Style.DIM + "T" + Style.RESET_ALL + Fore.YELLOW + "\_ " + Style.RESET_ALL + "|" + Fore.YELLOW + "|\  ")
        print("  ||" + Style.RESET_ALL + "|" + Style.RESET_ALL + Fore.YELLOW + " |_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| ," + Style.RESET_ALL + "/|" + Fore.YELLOW + "=/_|_\=" + Style.RESET_ALL + "|\\" + Fore.YELLOW + ", |_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| " + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "    |_L_" + Fore.RED + Style.DIM + "LT||" + Fore.RED + Style.DIM + "TJ" + Style.RESET_ALL + Fore.YELLOW + "_J_|    " + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + " |_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| ," + Style.RESET_ALL + "/|" + Style.RESET_ALL + Fore.YELLOW + "=/_|_\=" + Style.RESET_ALL + "|\\" + Style.RESET_ALL + Fore.YELLOW + ", |_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| " + Style.RESET_ALL + "|" + Style.RESET_ALL + Fore.YELLOW + "||  ")
        print("  ||" + Style.RESET_ALL + "|" + Style.RESET_ALL + Fore.YELLOW + " |_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| " + Style.RESET_ALL + "|||" + Fore.YELLOW + "___|___" + Style.RESET_ALL + "|||" + Fore.YELLOW + " |_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| " + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "____" + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + "/|||/\|||\\" + Style.RESET_ALL + "[]    " + Style.RESET_ALL + "[_] " + Style.RESET_ALL + Fore.YELLOW + "|_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| " + Style.RESET_ALL + "|||" + Style.RESET_ALL + Fore.YELLOW + "___|___" + Style.RESET_ALL + "||| " + Fore.YELLOW + "|_" + Fore.RED + Style.DIM + "O" + Style.RESET_ALL + Fore.YELLOW + "_| " + Style.RESET_ALL + "|" + Style.RESET_ALL + Fore.YELLOW + "|| " + Style.RESET_ALL + " ")
        print("  [_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "IIIII" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "IIIII" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "IIIII" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_]" + Fore.RED + Style.DIM + "IIII" + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + "\==/" + Fore.RED + Style.DIM + "%%" + Style.RESET_ALL + Fore.YELLOW + "\==/" + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "IIII" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "IIIII" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "IIIII" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "IIIII" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_]  ")
        print("  [_]" + Style.RESET_ALL + Fore.YELLOW + ".\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_/." + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + ".\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_/." + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + ".\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_/." + Style.RESET_ALL + "[_]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + ".\_\\" + Fore.RED + Style.DIM + "%%" + Style.RESET_ALL + Fore.YELLOW + "/_/." + Style.RESET_ALL + "[]" + Style.RESET_ALL + Fore.YELLOW + "\\" + Fore.RED + Style.DIM + "II" + Style.RESET_ALL + Fore.YELLOW + "/" + Style.RESET_ALL + "[_].\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_/." + Style.RESET_ALL + "[_].\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_/." + Style.RESET_ALL + "[_].\_" + Fore.RED + Style.DIM + "I" + Style.RESET_ALL + Fore.YELLOW + "_/." + Style.RESET_ALL + "[_]  ")
        print("  L_J" + Style.RESET_ALL + Fore.YELLOW + "./   \." + Style.RESET_ALL + "L_J" + Fore.YELLOW + "./   \." + Style.RESET_ALL + "L_J" + Fore.YELLOW + "./   \." + Style.RESET_ALL + "L_J" + Fore.RED + Style.DIM + "I  I" + Style.RESET_ALL + "[]" + Fore.YELLOW + "./      \." + Style.RESET_ALL + "[]" + Fore.RED + Style.DIM + "I  I" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "./   \." + Style.RESET_ALL + "L_J" + Fore.YELLOW + "./   \." + Style.RESET_ALL + "L_J./   \." + Style.RESET_ALL + "L_J  ")
        print("  L_J" + Style.RESET_ALL + Fore.YELLOW + "|     |" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|     |" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|     |" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|  |" + Style.RESET_ALL + "[]" + Fore.YELLOW + "|        |" + Style.RESET_ALL + "[]" + Fore.YELLOW + "|  |" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|     |" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|     |" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|     |" + Style.RESET_ALL + "L_J  ")
        print("  L_J" + Style.RESET_ALL + Fore.YELLOW + "|_____|" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|_____|" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|_____|" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|__|" + Style.RESET_ALL + "[]" + Fore.YELLOW + "|        |" + Style.RESET_ALL + "[]" + Fore.YELLOW + "|__|" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|_____|" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|_____|" + Style.RESET_ALL + "L_J" + Fore.YELLOW + "|_____|" + Style.RESET_ALL + "L_J  ")
        print(Fore.YELLOW + " >You approach the yellow fortress, key in hand." + Style.RESET_ALL)
def resetstartingvalues():
    global startgame
    startgame = True
    global key
    key = False
    global rustswd
    rustswd = False
    global items
    items = False
    global playgame
    playgame = False
    global fightmon
    fightmon = False
    global furslime
    furslime = False
    global playerlocation
    playerlocation = 1
    global monster
    monster = 0
    global monsterhp
    monsterhp = 0
    global playrhp
    playrhp = 200
    global oneeye
    oneeye = False
    global wine
    wine = False
    global free
    free = False
    global part1over
    part1over = False
    global heal
    heal = False
    global talking
    talking = False
    global getgold
    getgold = False
    global guard
    guard = False
    global runfrombeast
    runfrombeast = False
    global runfromdraco
    runfromdraco = False
    global telltruth
    telltruth = 3
    global displaybegin
    displaybegin = False
    global meds
    meds = False
    global claymore
    claymore = False
def talkmenu():
    print (Fore.RED + " >\"What business do you have here?\"")
    time.sleep(1.5)
    print(Style.RESET_ALL + "<= Options = > \n TRUTH \n LIE \n PROVOKE \n BARGAIN \n END")
def talk(talkmenu):
    global fightmon
    global monster
    global monsterhp
    global telltruth
    global talking
    randomnumber = random.randint(0,1)
    if talkmenu == 1:
        playerchoi = str.upper (input(" >"))
        if playerchoi == ("TRUTH"):
            if telltruth == 0:
                print (Fore.YELLOW + " >You tell the lizard man yet again of your journey, even explaining him of the battle with the one-eyed beast.")
                time.sleep(2)
                print(Fore.RED + ">\"You'll have to come up with something better than that to fool me!\"" + Style.RESET_ALL)
                time.sleep(2)
            else:
                print (Fore.YELLOW + " >You tell the lizard man the truth, that you are searching for a princess and need to pass through the fortress.")
                time.sleep(2)
                print(" >The draco gives a hearty laugh that echoes through the trees.")
                time.sleep(2)
                print(Fore.RED + " >\"Hahaha! You must be joking! Do you think that I'm THAT stupid to believe that?\"")
                time.sleep(2)
                print(Fore.YELLOW + " >He gives a gruff grunt, waiting for a better answer." + Style.RESET_ALL)
                time.sleep(2)
                telltruth = 0
        elif playerchoi == ("LIE"):
            if randomnumber == 0:
                print (Fore.YELLOW + " >You lie to the dragon guard, and tell him that you have an important package to deliver to Kobra himself.")
                time.sleep(2)
                print(" >Hearing the urgency in your voice, the dragon sighs and asks for your key.")
                time.sleep(2)
                print(" >Snatching your silver key, the dragon unlocks the gate and reluctantly lets your inside." + Style.RESET_ALL)
                time.sleep(2)
                win()
            elif randomnumber == 1:
                print (Fore.YELLOW + " >You lie to the dragon guard, and tell him that you have an important package to deliver to Kobra himself.")
                time.sleep(2)
                print(" >The draco, still skeptical, asks how you knew Kobra.")
                time.sleep(2)
                print(" >You begin to choke up, the truth quickly unraveling.")
                time.sleep(2)
                print(Fore.RED + " >\"I knew you looked suspicious, and this confirms it!\"" + Style.RESET_ALL)
                time.sleep(2)
                monster = 2
                talking = False
                fightmon = True
                artmon(monster)
                monsterhp = 550
        elif playerchoi == ("PROVOKE"):
            print (Fore.YELLOW + " >You provoke the draco and tell him that he's horrible at his job.")
            time.sleep(2)
            print(Fore.RED + " >\"Oh, yeah? We'll see about that!\"" + Style.RESET_ALL)
            time.sleep(2)
            monster = 2
            talking = False
            fightmon = True
            artmon(monster)
            monsterhp = 500
        elif playerchoi == ("BARGAIN"):
            print (Fore.YELLOW + " >You attempt to bargain with the draco, and surprisingly, he gives in.")
            time.sleep(2)
            print(Fore.RED + " >\"Well... I could use some extra change. Any chance you got some Gold Coins?\"" + Style.RESET_ALL)
            time.sleep(2)
            if getgold == True:
                print (Fore.YELLOW + " >Hand over pouch of coins? \n " + Fore.GREEN + "YES" + Fore.RED + " \n NO")
                playerchoi = str.upper (input(" >"))
                if playerchoi == ("YES"):
                    print (Fore.YELLOW + " >You hand over the pouch of coins in exchange for entry. The lizard asks if you have a key, in which you hand over the silver key.")
                    time.sleep(2)
                    print(" >Snatching the key, he unlocks the gate and lets your inside, a smirk plastered on his face." + Style.RESET_ALL)
                    time.sleep(2)
                    win()
            else:
                pass
        elif playerchoi == ("END"):
            print (Fore.RED + " >\"Alright... 'cya around.\"" + Style.RESET_ALL)
            time.sleep(2)
            talking = False
            playerlocation = 10
            printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
def printmenu():
    print ("<= Options = > \n MOVE \n ITEM \n TALK \n FIGHT \n EXAMINE")
def artmon(monster):
    ingamemusic(4)
    if monster == 1:
        print("     :\"'._..---.._.'\";")
        print("     `.             .'")
        print("     .'     /;\      `.")
        print("    :       \`/       :                 __....._")
        print("    :     _.-0-._     :---'\"\"'\"-....--'\"        '.")
        print("     :  .'   :   `.  :                          `,`.")
        print("      `.:  --'--  :.'                             ; ;")
        print("       : `._   _.'                                ;.'")
        print("       `.   '\"'                                   ;")
        print("        `.               '                        ;")
        print("         `.     `        :           `            ;")
        print("          .`.    ;       ;           :           ;")
        print("        .'    `-.'      ;            :          ;`.")
        print("    __.'      .'      .'              :        ;   `.")
        print("  .'      __.'      .'`--..__      _._.'      ;      ;")
        print("  `......'        .'         `'\"\"'`.'        ;......-'")
        print("        `.......-'                 `........'")
        print (Fore.YELLOW + " >The hairy beast approaches you, snarling through his savage teeth."+ Style.RESET_ALL)
    if monster == 2:
        print("                                              ,--,  ,.-.")
        print("                ,                   \,       '-,-`,'-.' | ._")
        print("               /|           \    ,   |\         }  )/  / `-,',")
        print("               [ '          |\  /|   | |        /  \|  |/`  ,`")
        print("               | |       ,.`  `,` `, | |  _,...(   (      _',")
        print("               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\ ")
        print("                \  \_\,``,   ` , ,  /  |         )         _,/")
        print("                 \  '  `  ,_ _`_,-,<._.<        /         /")
        print("                  ', `>.,`  `  `   ,., |_      |         /")
        print("                    \/`  `,   `   ,`  | /__,.-`    _,   `\ ")
        print("                -,-..\  _  \  `  /  ,  / `._) _,-\`       \ ")
        print("                 \_,,.) /\    ` /  / ) (-,, ``    ,        |")
        print("                ,` )  | \_\       '-`  |  `(               \ ")
        print("               /  /```(   , --, ,' \   |`<`    ,            |")
        print("              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)")
        print("        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`")
        print("       (-, \           ) \ ('_.-._)/ /,`    /")
        print("       | /  `          `/ \\\\ V   V, /`     /")
        print("    ,--\(        ,     <_/`\\\\     ||      /")
        print("   (   ,``-     \/|         \-A.A-`|     /")
        print("  ,>,_ )_,..(    )\          -,,_-`  _--`")
        print("_ \|`   _,/_  /  \_            ,--`")
        print("  \( `   <.,../`     `-.._   _,-`")
        print("   `                      ```")
        print(Fore.YELLOW + " >The dragon man attacks!" + Style.RESET_ALL)
def monmenu():
    print ("<= Options = > \n FIGHT \n MAGIC \n ITEM \n CHECK \n RUN")
def getmonmenuchoice(monster):
    global meds
    global player
    global fightmon
    global monsterhp
    global playrhp
    global playerlocation
    global runfromdraco
    global runfrombeast
    randnumlow = random.randint(40, 70)
    randnummid = random.randint(50, 100)
    randnumhigh = random.randint(75, 150)
    playerchoi = str.upper (input(" >"))
    if monster == 1:
        if playerchoi == ("FIGHT"):
            global oneeye
            dmg = randnummid + 20
            playdmg = randnumlow - 5
            print(Fore.YELLOW + " >" + player + " DEALS " + str(dmg) + " DAMAGE" + Style.RESET_ALL)
            time.sleep(1)
            monsterhp = monsterhp - dmg
            if monsterhp <= 0:
                ingamemusic(7)
                print(Style.BRIGHT + Fore.YELLOW + " >You have defeated the creature!" + Style.RESET_ALL)
                time.sleep(10)
                ingamemusic(3)
                playerlocation = 7
                printlocation(playerlocation)
                fightmon = False
                oneeye = True # beast dead
                runfrombeast = False
            elif monsterhp >= 0:
                print (" >The creature lunges at you!")
                playrhp = playrhp - playdmg
                time.sleep(1)
                print(Fore.RED + " >MONSTER DEALS " + str(playdmg) + " DAMAGE" + Style.RESET_ALL)
                if playrhp <= 0:
                    time.sleep(1)
                    endgame()
        elif playerchoi == ("MAGIC"):
            print(Fore.YELLOW + " >You haven't learned any magic!" + Style.RESET_ALL)
        elif playerchoi == ("ITEM"):
            if meds == True:
                print (Fore.YELLOW + " >Which item?" + Style.RESET_ALL)
                time.sleep(0.5)
                print(itemlist[1] + "\n >EXIT")
                playerchoi = str.upper (input(" >"))
                if playerchoi == ("MEDICAL SUPPLIES") or ("MEDS"):
                    print (Fore.YELLOW + " >Are you sure you'd like to use the medical supplies? This item can only be used once." + Style.RESET_ALL)
                    time.sleep(1)
                    playerchoi = str.upper(input(" >"))
                    if playerchoi == "YES" or "Y":
                        print (Fore.GREEN + " >You used the medical supplies to restore your HP!" + Style.RESET_ALL)
                        time.sleep(1)
                        playrhp = playrhp + 50
                        if part1over == True and playrhp >= 250:
                                playrhp = 250
                        elif part1over == False and playrhp >= 200:
                                playrhp = 200
                        meds = False
                    elif playerchoi == "NO" or "N":
                        print(Fore.YELLOW + " >You put the bandages back into you inventory." + Style.RESET_ALL)
            else:
                print (Fore.YELLOW + " >You don't have any items you can use right now!" + Style.RESET_ALL)
        elif playerchoi == ("CHECK"):
            print (Fore.YELLOW + " >Monster = " + str(monsterhp) + "\n >" + player + " = " + str(playrhp) + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("RUN"):
            print(Fore.YELLOW + " >You manage to escape..." + Style.RESET_ALL)
            time.sleep(2)
            ingamemusic(3)
            playerlocation = 13
            printlocation(playerlocation)
            fightmon = False
            runfrombeast = True
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
    if monster == 2:
        if playerchoi == ("FIGHT"):
            global guard
            playdmg = randnummid - 5
            if claymore == True:
                dmg = randnumhigh + 20
            else:
                dmg = randnummid + 20
            print(Fore.YELLOW + " >" + player + " DEALS " + str(dmg) + " DAMAGE" + Style.RESET_ALL)
            time.sleep(1)
            monsterhp = monsterhp - dmg
            if monsterhp <= 0:
                ingamemusic(7)
                print(Style.BRIGHT + Fore.YELLOW + " >You have defeated the creature!" + Style.RESET_ALL)
                time.sleep(10)
                ingamemusic(6)
                playerlocation = 11
                printlocation(playerlocation)
                fightmon = False
                guard = True # guard dead
                runfromdraco = False
            elif monsterhp >= 0:
                print (" >The dragon man strikes you with his broad sword!")
                time.sleep(1)
                playrhp = playrhp - playdmg
                print(Fore.RED + " >FOE DEALS " + str(playdmg) + " DAMAGE" + Style.RESET_ALL)
                time.sleep(2)
                if playrhp <= 0:
                    endgame()
        elif playerchoi == ("MAGIC"):
            print(Fore.YELLOW + " >You haven't learned any magic!" + Style.RESET_ALL)
        elif playerchoi == ("ITEM"):
            if meds == True:
                print (Fore.YELLOW + " >Which item?" + Style.RESET_ALL)
                time.sleep(0.5)
                print(itemlist[1] + "\n >EXIT")
                playerchoi = str.upper (input(" >"))
                if playerchoi == ("MEDICAL SUPPLIES") or ("MEDS"):
                    print (Fore.YELLOW + " >Are you sure you'd like to use the medical supplies? This item can only be used once." + Style.RESET_ALL)
                    time.sleep(1)
                    playerchoi = str.upper(input(" >"))
                    if playerchoi == "YES" or "Y":
                        print (Fore.GREEN + " >You used the medical supplies to restore your HP!" + Style.RESET_ALL)
                        time.sleep(1)
                        playrhp = playrhp + 50
                        if part1over == True and playrhp >= 250:
                                playrhp = 250
                        elif part1over == False and playrhp >= 200:
                                playrhp = 200
                        meds = False
                    elif playerchoi == "NO" or "N":
                        print(Fore.YELLOW + " >You put the bandages back into you inventory." + Style.RESET_ALL)
            else:
                print (Fore.YELLOW + " >You don't have any items you can use right now!" + Style.RESET_ALL)
        elif playerchoi == ("CHECK"):
            print (Fore.YELLOW + " >FOE = " + str(monsterhp) + "\n >" + player + " = " + str(playrhp) + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("RUN"):
            print(Fore.YELLOW + " >You manage to escape..." + Style.RESET_ALL)
            time.sleep(2)
            ingamemusic(3)
            playerlocation = 12
            printlocation(playerlocation)
            fightmon = False
            runfromdraco = True
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
def getmenuchoice(menu):
    global playerlocation # my globals that look horrifying
    global key
    global claymore
    global rustswd
    global furslime
    global fightmon
    global monster
    global monsterhp
    global playrhp
    global wine
    global free
    global part1over
    global heal
    global getgold
    global talking
    global meds
    playerchoi = str.upper (input(" >"))
    if menu == 1: # entrance of pythonia. bag of gold 1
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.GREEN + " >A old hermit sits under one of the oaks, lost in thought.")
            time.sleep(2)
            print(" >Oh, hello Young One! Heading off to find that princess, eh?")
            time.sleep(2)
            print(" >Well, shes 'round here somewhere. Bunch'a commotion in some cave nearby too.")
            time.sleep(2)
            print(" >I'd check there first if I was you. Safe travels!" + Style.RESET_ALL)
            time.sleep(2)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >The forest emits an mystifying glow in the moonlight. ")
            time.sleep(1.5)
            print(" >An owl flies above your head, something caught in its claws.")
            time.sleep(2)
            print(" >Maybe you can follow it deeper in the forest!" + Style.RESET_ALL)
            time.sleep(1.5)
            key = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Left or Right?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("LEFT"):
                playerlocation = 2
                printlocation(playerlocation)
            elif playerchoi == ("RIGHT"):
                playerlocation = 3
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
    elif menu == 2: # pre - forest, first thing if u go left @ beginning. bag of gold 2
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >There's no one to talk to!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >The massive oak sways with the wind, creating an eerie atmosphere." + Style.RESET_ALL)
            time.sleep(2)
            if key == True:
                print(Fore.YELLOW + " >You examine the tree to find a small object lodged in one of its branches.")
                time.sleep(2)
                print(" >You aquire the bag of coins." + Style.RESET_ALL)
                time.sleep(1)
                getgold = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Left or Right?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("LEFT"):
                playerlocation = 9
                printlocation(playerlocation)
            elif playerchoi == ("RIGHT"):
                playerlocation = 1
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 3: # pre - cliff, first thing if u go right @ beginning. meds
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >You encounter a friendly wanderer!")
            time.sleep(1.2)
            print(Fore.GREEN + " >Hey, stranger! If you were planning on going left and heading through the forest, I've heard its been closed off.")
            time.sleep(2)
            print(" >Kobra probably regained the idle fortress. You'll need a key if you want to get through there!")
            time.sleep(2)
            print(" >Farewell!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >You find a some medical supplies, most likely left behind by travellers." + Style.RESET_ALL)
            time.sleep(2)
            meds = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Left or Right?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("LEFT"):
                playerlocation = 1
                printlocation(playerlocation)
            elif playerchoi == ("RIGHT"):
                playerlocation = 4
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 4: #cliff that took me 100 years to make look pretty
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >There's no one to talk to!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            if part1over == False:
                print (Fore.YELLOW + " >You pause near the edge of the cliff to fully take in the view before you.")
                time.sleep(2)
                print(" >The sun peeks out from the clouds, its rays coating the side of the mountain and illuminating the lake.")
                time.sleep(3)
                print(" >Although it is a calming scene, you soon remember why you were here in the first place and continue on." + Style.RESET_ALL)
                time.sleep(3)
            elif part1over == True:
                print(Fore.YELLOW + " >Arriving back to the beautiful mountains, you pause for a quick break near the lake.")
                time.sleep(2)
                print(" >Spotting a metallic flash, you discover an elegant blade, much more useful than your current weapon.")
                time.sleep(3)
                print(" >You recieve the Soldier's Claymore." + Style.RESET_ALL)
                time.sleep(2)
                claymore = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Left or Forward?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("LEFT"):
                playerlocation = 3
                printlocation(playerlocation)
            elif playerchoi == ("FORWARD"):
                playerlocation = 5
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 5: # Entrance to cave. Rusted sword
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >There's no one to talk to!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >Approaching the cliffside, you find a rusted sword, most likely from a fallen warrior." + Style.RESET_ALL)
            time.sleep(3)
            rustswd = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("BACK"):
                playerlocation = 4
                printlocation(playerlocation)
            elif playerchoi == ("FORWARD"):
                ingamemusic(3)
                if oneeye == True:
                    playerlocation = 7
                    printlocation(playerlocation)
                elif runfrombeast == True:
                    playerlocation = 13
                    printlocation(playerlocation)
                else:
                    playerlocation = 6
                    printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 6: #cave before defeat of beast. need rusted sword
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >You shout into the darkness.")
            time.sleep(1)
            print(" >... ")
            time.sleep(2)
            print(" >You hear distant muffling, almost as if someone was crying for help!" + Style.RESET_ALL)
            time.sleep(2)
        elif playerchoi == ("FIGHT"):
            if furslime == True:
                if rustswd == True:
                    print (Fore.YELLOW + " >You retrieve the rusted sword and strike the fleshy mound. ")
                    time.sleep(2)
                    print(" >It yowls in pain, jumping back to face its foe" + Style.RESET_ALL)
                    time.sleep(2)
                    monster = 1
                    fightmon = True
                    artmon(monster)
                    monsterhp = 200
                else:
                    print(Fore.YELLOW + " >You try to punch the slimy object, but it doesn't even flinch! ")
                    time.sleep(2)
                    print(" >You might need a weapon to defeat this foe." + Style.RESET_ALL)
                    time.sleep(2)
            else:
                print (Fore.YELLOW + " >You can't see anything to fight!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >Eyes adjusting to the darkness, You can barely make out a few skeletons and a large beast at the back of the cave. " + Style.RESET_ALL)
            time.sleep(3.5)
            furslime = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("BACK"):
                ingamemusic(2)
                playerlocation = 5
                printlocation(playerlocation)
            elif playerchoi == ("FORWARD"):
                print (Fore.YELLOW + " >You attempt to continue, but you accidentally run into a slime-covered furry object blocking your path. ")
                time.sleep(2.5)
                print(" >You briskly wipe its thin slime from your body and think of another plan of action." + Style.RESET_ALL)
                time.sleep(2.5)
                furslime = True
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 7: #cave after defeat of beast
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            if part1over == True:
                print (Fore.YELLOW + " >You need to get closer to talk to the plainsman." + Style.RESET_ALL)
                time.sleep(1)
            else:
                print (Fore.YELLOW + " >Standing in the silence of the cave, you shout into the darkness. ")
                time.sleep(2)
                print(" >A muffled voice answers, but appears to be deeper in the cave." + Style.RESET_ALL)
                time.sleep(2)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >You have already defeated the enemy!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            if heal == True:
                print (Fore.YELLOW + " >You check the body of the one-eyed beast. ")
                time.sleep(1.5)
                print(" >You've already collected all of his belongings!" + Style.RESET_ALL)
                time.sleep(1.5)
            else:
                print (Fore.YELLOW + " >You check the body of the one-eyed beast and find a herb of healing. ")
                time.sleep(2)
                print(Fore.GREEN + " >HP RESTORED! " + Style.RESET_ALL)
                time.sleep(1)
                playrhp = 200
                heal = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("BACK"):
                ingamemusic(2)
                playerlocation = 5
                printlocation(playerlocation)
            elif playerchoi == ("FORWARD"):
                playerlocation = 8
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 8: # dark cave after defeat of beast
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            if free == False:
                print (Fore.YELLOW + " >You try to speak to the person, but he's still trapped and can't respond! ")
                time.sleep(2)
                print(" >Maybe there is an item nearby to free him..." + Style.RESET_ALL)
                time.sleep(2)
            elif free == True:
                print (Fore.GREEN + " >\"Thank you so much! That beast was one of Kobra's minions.\" ")
                time.sleep(2)
                print(" >\"Rumor has it that he's been spotted at a yellow fortress deep in forest. Please, take my belongings with you!\"" + Style.BRIGHT + Fore.YELLOW)
                time.sleep(3)
                print(" >" + player + " RECEIVED THE SILVER KEY AND LEATHER ARMOR" + Style.RESET_ALL)
                time.sleep(1.5)
                print(Fore.GREEN + " >\"That key should unlock the gateway located deep into the forest. Good luck!\"" + Style.RESET_ALL)
                time.sleep(3)
                if part1over == False:
                    playrhp = 250
                else:
                    pass
                part1over = True
            elif part1over == True:
                print(Fore.GREEN + " >\"Don't worry about me," + player + "! Continue on your quest!\"" + Style.RESET_ALL)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >The farmer does not appear to be an enemy!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >You find a shattered wine bottle carelessly broken on the floor of the cave. " + Style.RESET_ALL)
            time.sleep(2)
            wine = True
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("BACK"):
                playerlocation = 7
                printlocation(playerlocation)
            elif playerchoi == ("FORWARD"):
                print(Fore.YELLOW + " >Its too dark to continue!" + Style.RESET_ALL)
                time.sleep(1)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 9: #forest before draco, single tree. stops player without part1over
        if playerchoi == ("ITEM"):
            if items == True:
                print (Fore.YELLOW + " >You can't use that now!" + Style.RESET_ALL)
                time.sleep(1)
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >There's no one to talk to!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >The forest thickens." + Style.RESET_ALL)
            time.sleep(1)
            if part1over == True:
                print(Fore.YELLOW + " >There seems to be a fortress in the distance!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Right or Forward?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("FORWARD"):
                if part1over == True:
                    ingamemusic(6)
                    if runfromdraco == True:
                        playerlocation = 12
                        printlocation(playerlocation)
                    elif guard == True:
                        playerlocation = 11
                        printlocation(playerlocation)
                    else:
                        playerlocation = 10
                        printlocation(playerlocation)
                else:
                    print(Fore.YELLOW + " >The thick forest blocks your path!" + Style.RESET_ALL)
                    time.sleep(1)
            elif playerchoi == ("RIGHT"):
                playerlocation = 2
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 10: #pre draco encounter
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >The only person to talk to is a dragon man in the distance, but he's too far away!" + Style.RESET_ALL)
            time.sleep(3)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >There's nothing to fight!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
                print(Fore.YELLOW + " >Mist pools at your feet as you approach the keep. ")
                time.sleep(2)
                print(" >Damaged from war, erosion, and everything between, the fortress looks as if it dates back 300 years. ")
                time.sleep(3)
                print(" >You would examine it further, but an agitated draco man paces the perimeter of the structure." + Style.RESET_ALL)
                time.sleep(3)
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("FORWARD"):
                print (Fore.YELLOW + " >You approach the gate to use the key, and are stopped by a dragon guard!"  + Style.RESET_ALL)
                time.sleep(2)
                talking = True
            elif playerchoi == ("BACK"):
                ingamemusic(2)
                playerlocation = 9
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 11: #after kill on goblin/dragon
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >You can't speak to the lizard man." + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >You've already defeated the foe!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
                print(Fore.YELLOW + " >Mist pools at your feet as you approach the keep. ")
                time.sleep(2)
                print(" >Damaged from war, erosion, and everything between, the fortress looks as if it dates back 300 years. ")
                time.sleep(3)
                print(" >Searching the poor humanoid's body, you can only find sentimental items that have no use to you." + Style.RESET_ALL)
                time.sleep(3)
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("FORWARD"):
                print(Fore.YELLOW + " >Opening the entrance, you step inside the fortress without a glance back.")
                time.sleep(2.5)
                print(" >The gate creaks shut behind you." + Style.RESET_ALL)
                time.sleep(2)
                win()
            elif playerchoi == ("BACK"):
                ingamemusic(2)
                playerlocation = 9
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 12: #run away from goblin/dragon
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >The only person to talk to is a dragon man in the distance, but he seems like he'll attack at any second!" + Style.RESET_ALL)
            time.sleep(3)
        elif playerchoi == ("FIGHT"):
            print (Fore.YELLOW + " >You're too far away!" + Style.RESET_ALL)
            time.sleep(1)
        elif playerchoi == ("EXAMINE"):
                print(Fore.YELLOW + " >Mist pools at your feet as you approach the keep. ")
                time.sleep(2)
                print(" >Damaged from war, erosion, and everything between, the fortress looks as if it dates back 300 years. ")
                time.sleep(3)
                print(" >You would examine it further, but the agitated half-dragon glares at you, calling you a coward for retreating." + Style.RESET_ALL)
                time.sleep(3.5)
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("FORWARD"):
                print (Fore.YELLOW + " >You approach the gate to use the key, and are stopped by a dragon guard!" + Fore.RED)
                time.sleep(2)
                print("\n >\"You coward! Come face me like a true hero!\"" + Style.RESET_ALL)
                time.sleep(2)
                fightmon = True
                artmon(monster)
                monsterhp = 600
            elif playerchoi == ("BACK"):
                ingamemusic(2)
                playerlocation = 9
                printlocation(playerlocation)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
    elif menu == 13: #run away from beast in cave
        if playerchoi == ("ITEM"):
            if items == True:
                itemsmenu()
            else:
                print (Fore.YELLOW + " >You don't have any items!" + Style.RESET_ALL)
                time.sleep(1)
        elif playerchoi == ("TALK"):
            print (Fore.YELLOW + " >You shout into the darkness. ")
            time.sleep(1)
            print(" >... ")
            time.sleep(1)
            print(" >You hear distant muffling, and a low growl. ")
            time.sleep(1.5)
            print(" >The beast is not very pleased by your cowardice." + Style.RESET_ALL)
            time.sleep(1.5)
        elif playerchoi == ("FIGHT"):
            monster = 1
            fightmon = True
            artmon(monster)
            monsterhp = monsterhp + 25
        elif playerchoi == ("EXAMINE"):
            print (Fore.YELLOW + " >Eyes adjusting to the darkness, You can barely make out a few skeletons and a large beast. ")
            time.sleep(3)
            print(" >The beast, who is not pleased in the slightest, is now fully aware and much more menacing than previously. " + Style.RESET_ALL)
            time.sleep(3)
        elif playerchoi == ("MOVE"):
            print (Fore.YELLOW + " >Forward or Back?" + Style.RESET_ALL)
            time.sleep(0.5)
            playerchoi = str.upper (input(" >"))
            if playerchoi == ("BACK"):
                ingamemusic(2)
                playerlocation = 5
                printlocation(playerlocation)
            elif playerchoi == ("FORWARD"):
                monster = 1
                fightmon = True
                artmon(monster)
                monsterhp = monsterhp + 25
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
            time.sleep(1)
def win():
    global playgame
    global talking
    global displaybegin
    global startgame
    ingamemusic(5)
    print(Style.BRIGHT + "██████" + Fore.YELLOW + "╗  " + Fore.WHITE + "█████" + Fore.YELLOW + "╗ " + Fore.WHITE + "██████" + Fore.YELLOW + "╗ " + Fore.WHITE + "████████" + Fore.YELLOW + "╗     " + Fore.WHITE + "██" + Fore.YELLOW + "╗     " + Fore.WHITE + "██████" + Fore.YELLOW + "╗ " + Fore.WHITE + "██████" + Fore.YELLOW + "╗ " + Fore.WHITE + "███" + Fore.YELLOW + "╗   " + Fore.WHITE + "███" + Fore.YELLOW + "╗" + Fore.WHITE + "██████" + Fore.YELLOW + "╗ " + Fore.WHITE + "██" + Fore.YELLOW + "╗     " + Fore.WHITE + "███████" + Fore.YELLOW + "╗" + Fore.WHITE + "████████" + Fore.YELLOW + "╗" + Fore.WHITE + "███████" + Fore.YELLOW + "╗")
    print(Fore.WHITE + "██" + Fore.YELLOW + "╔══" + Fore.WHITE + "██" + Fore.YELLOW + "╗" + Fore.WHITE + "██" + Fore.YELLOW + "╔══" + Fore.WHITE + "██" + Fore.YELLOW + "╗" + Fore.WHITE + "██" + Fore.YELLOW + "╔══" + Fore.WHITE + "██" + Fore.YELLOW + "╗╚══" + Fore.WHITE + "██" + Fore.YELLOW + "╔══╝    " + Fore.WHITE + "███" + Fore.YELLOW + "║    " + Fore.WHITE + "██" + Fore.YELLOW + "╔════╝" + Fore.WHITE + "██" + Fore.YELLOW + "╔═══" + Fore.WHITE + "██" + Fore.YELLOW + "╗" + Fore.WHITE + "████" + Fore.YELLOW + "╗ " + Fore.WHITE + "████" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "╔══" + Fore.WHITE + "██" + Fore.YELLOW + "╗" + Fore.WHITE + "██" + Fore.YELLOW + "║     " + Fore.WHITE + "██" + Fore.YELLOW + "╔════╝╚══" + Fore.WHITE + "██" + Fore.YELLOW + "╔══╝" + Fore.WHITE + "██" + Fore.YELLOW + "╔════╝")
    print(Fore.WHITE + "██████" + Fore.YELLOW + "╔╝" + Fore.WHITE + "███████" + Fore.YELLOW + "║" + Fore.WHITE + "██████" + Fore.YELLOW + "╔╝   " + Fore.WHITE + "██" + Fore.YELLOW + "║       ╚" + Fore.WHITE + "██" + Fore.YELLOW + "║    " + Fore.WHITE + "██" + Fore.YELLOW + "║     " + Fore.WHITE + "██" + Fore.YELLOW + "║   " + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "╔" + Fore.WHITE + "████" + Fore.YELLOW + "╔" + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██████" + Fore.YELLOW + "╔╝" + Fore.WHITE + "██" + Fore.YELLOW + "║     " + Fore.WHITE + "█████" + Fore.YELLOW + "╗     " + Fore.WHITE + "██" + Fore.YELLOW + "║   " + Fore.WHITE + "█████" + Fore.YELLOW + "╗  ")
    print(Fore.WHITE + "██" + Fore.YELLOW + "╔═══╝ " + Fore.WHITE + "██" + Fore.YELLOW + "╔══" + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "╔══" + Fore.WHITE + "██" + Fore.YELLOW + "╗   " + Fore.WHITE + "██" + Fore.YELLOW + "║        " + Fore.WHITE + "██║    ██" + Fore.YELLOW + "║     " + Fore.WHITE + "██" + Fore.YELLOW + "║   " + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "║╚" + Fore.WHITE + "██" + Fore.YELLOW + "╔╝" + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "╔═══╝ " + Fore.WHITE + "██" + Fore.YELLOW + "║     " + Fore.WHITE + "██" + Fore.YELLOW + "╔══╝     " + Fore.WHITE + "██" + Fore.YELLOW + "║   " + Fore.WHITE + "██" + Fore.YELLOW + "╔══╝  ")
    print(Fore.WHITE + "██" + Fore.YELLOW + "║     " + Fore.WHITE + "██" + Fore.YELLOW + "║  " + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "║  " + Fore.WHITE + "██" + Fore.YELLOW + "║   " + Fore.WHITE + "██" + Fore.YELLOW + "║        " + Fore.WHITE + "██║    " + Fore.YELLOW + "╚" + Fore.WHITE + "██████" + Fore.YELLOW + "╗╚" + Fore.WHITE + "██████" + Fore.YELLOW + "╔╝" + Fore.WHITE + "██" + Fore.YELLOW + "║ ╚═╝ " + Fore.WHITE + "██" + Fore.YELLOW + "║" + Fore.WHITE + "██" + Fore.YELLOW + "║     " + Fore.WHITE + "███████" + Fore.YELLOW + "╗" + Fore.WHITE + "███████" + Fore.YELLOW + "╗   " + Fore.WHITE + "██" + Fore.YELLOW + "║   " + Fore.WHITE + "███████" + Fore.YELLOW + "╗")
    print(Fore.YELLOW + "╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═╝     ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝   ╚═╝   ╚══════╝" + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.YELLOW + " >Congratulations! You've completed Part 1! Would you like to play again?" + Style.RESET_ALL)
    time.sleep(0.5)
    playerchoi = str (input(" >"))
    if playerchoi == ("YES") or ("Y"):
        resetstartingvalues()
        start()
    elif playerchoi == ("NO") or ("N"):
        print(Fore.YELLOW + " >Thanks for playing! :) "+ Style.RESET_ALL)
        resetstartingvalues()
        startgame = False
    else:
        print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
def start():
    global player
    global playgame
    global playerlocation
    global startgame
    ingamemusic(1)
    print(Style.RESET_ALL)
    print(Style.BRIGHT)
    print(Fore.YELLOW + "     _____    _____      _____  _________________  ____   ____         _____  _____   ______    ____       _____   ")
    print(Fore.YELLOW + " ___|\    \  |\    \    /    /|/                 \|    | |    |   ____|\    \|\    \ |\     \  |    |  ___|\    \  ")
    print(Fore.YELLOW + "|    |\    \ | \    \  /    / |\______     ______/|    | |    |  /     /\    \ \\    \| \     \ |    | /    /\    \ ")
    print(Fore.YELLOW + "|    | |    ||  \____\/    /  /   \( /    /  )/   |    |_|    | /     /  \    \\\\|    \  \     ||    ||    |  |    |")
    print(Fore.YELLOW + "|    |/____/| \ |    /    /  /     ' |   |   '    |    .-.    ||     |    |    ||     \  |    ||    ||    |__|    |")
    print(Fore.YELLOW + "|    ||    ||  \|___/    /  /        |   |        |    | |    ||     |    |    ||      \ |    ||    ||    .--.    |")
    print(Fore.YELLOW + "|    ||____|/      /    /  /        /   //        |    | |    ||\     \  /    /||    |\ \|    ||    ||    |  |    |")
    print(Fore.YELLOW + "|____|            /____/  /        /___//         |____| |____|| \_____\/____/ ||____||\_____/||____||____|  |____|")
    print(Fore.YELLOW + "|    |           |`    | /        |`   |          |    | |    | \ |    ||    | /|    |/ \|   |||    ||    |  |    |")
    print(Fore.YELLOW + "|____|           |_____|/         |____|          |____| |____|  \|____||____|/ |____|   |___|/|____||____|  |____|")
    time.sleep(1)
    print(Fore.GREEN + " .---..-.  .-..----. .----.    .----..---.  .--.  .----.  .---. ")
    print("{_   _}\ \/ / | {}  }| {_     { {__ {_   _}/ {} \ | {}  }{_   _}")
    print("  | |   }  {  | .--' | {__    .-._} } | | /  /\  \| .-. \  | |  ")
    print("  `-'   `--'  `-'    `----'   `----'  `-' `-'  `-'`-' `-'  `-'  ")
    print(Style.RESET_ALL)
    playerchoi = str.upper (input(" >"))
    if playerchoi != ("START"):
        playerchoi = str (input("Type START to continue: "))
    if playerchoi == ("Start") or ("START") or ("start"):
        global displaybegin
        player = str.upper(input(" >Enter your name : "))
        ingamemusic(2)
        printlocation(1)
        playerlocation = 1
        print(Fore.YELLOW + " >We begin our story in a forest at the center of Pythonia. A young warrior is sent to rescue a princess captured by the evil wizard, Kobra.")
        time.sleep(2)
        print(" >Good luck, Great Warrior!" + Style.RESET_ALL)
        displaybegin = True
        playgame = True
        startgame = False
def endgame():
    global talking
    global playgame
    global fightmon
    global startgame
    global displaybegin
    print(Fore.YELLOW + " >The foe strikes you down..." + Style.RESET_ALL)
    ingamemusic(8)
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + " _____ ____  _      _____   ____  _     _____ ____  ")
    print("/  __//  _ \/ \__/|/  __/  /  _ \/ \ |\/  __//  __\ ")
    print("| |  _| / \|| |\/|||  \    | / \|| | //|  \  |  \/| ")
    print("| |_//| |-||| |  |||  /_   | \_/|| \// |  /_ |    / ")
    print("\____\\\_/ \|\_/  \|\____\  \____/\__/  \____\\\_/\_\ " + Style.RESET_ALL)
    time.sleep(2)
    print(Fore.YELLOW + " >Would you like to retry from the start? " + Style.RESET_ALL)
    time.sleep(1)
    playerchoi = str (input(" >"))
    resetstartingvalues()
    if playerchoi == ("YES") or ("Y"):
        start()
    elif playerchoi == ("NO") or ("N"):
        print(Fore.YELLOW + " >Thanks for playing! :) "+ Style.RESET_ALL)
        startgame = False
    else:
        print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
def itemsmenu():
    global rustswd
    global meds
    global getgold
    global claymore
    global wine
    global part1over
    global playerlocation
    items = (" >RUSTED SWORD"," >MEDICAL SUPPLIES 1"," >POUCH OF GOLD COINS"," >SOLDIER'S CLAYMORE"," >WINE BOTTLE"," >SILVER KEY")
    print("<= ITEMS =>")
    if rustswd == True:
        print(items[0])
    if meds == True:
        print(items[1])
    if getgold == True:
        print(items[2])
    if claymore == True:
        print(items[3])
    if wine == True:
        print(items[4])
    if part1over == True:
        print(items[5])
    print(" >EXIT")
    getitemmenuchoice(playerlocation)
def getitemmenuchoice(location):
    global rustswd
    global wine
    global getgold
    global meds
    global claymore
    global wine
    global part1over
    global playrhp
    global furslime
    global runfrombeast
    global free
    global playerlocation
    playerchoi = str.upper (input(" >"))
    if rustswd == True and playerchoi == "RUSTED SWORD" or playerchoi == "SWORD" or playerchoi == "RUST SWORD":
        if furslime == True and oneeye == False and playerlocation == 6:
                print (Fore.YELLOW + " >You retrieve the rusted sword and strike the fleshy mound. ")
                time.sleep(2)
                print(" >It yowls in pain, jumping back to face its foe" + Style.RESET_ALL)
                time.sleep(2)
                monster = 1
                fightmon = True
                artmon(monster)
                monsterhp = 200
        elif runfrombeast == True and oneeye == False and playerlocation == 6:
            print (Fore.YELLOW + " >You retrieve the rusted sword to strike the beast. ")
            monster = 1
            fightmon = True
            artmon(monster)
            monsterhp = monsterhp + 25
        else:
            print (Fore.YELLOW + " >A severely damaged sword. Not the best weapon, but better than nothing!" + Style.RESET_ALL)
            time.sleep(1.5)
    elif meds == True and playerchoi == "MEDICAL SUPPLIES" or playerchoi == "MED KIT" or playerchoi == "MEDS":
        print (Fore.YELLOW + " >Are you sure you'd like to use the medical supplies? This item can only be used once." + Style.RESET_ALL)
        time.sleep(1)
        playerchoi = str.upper(input(" >"))
        if playerchoi == "YES" or "Y":
            print (Fore.GREEN + " >You used the medical supplies to restore your HP!" + Style.RESET_ALL)
            time.sleep(1)
            playrhp = playrhp + 50
            if part1over == True and playrhp >= 250:
                playrhp = 250
            elif part1over == False and playrhp >= 200:
                playrhp = 200
            meds = False
        elif playerchoi == "NO" or "N":
            print(Fore.YELLOW + " >You put the bandages back into you inventory." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
    elif getgold == True and playerchoi == "POUCH OF GOLD COINS" or playerchoi == "POUCH OF GOLD COIN" or playerchoi == "GOLD COINS" or playerchoi == "GOLD" or playerchoi == "GOLD COIN" or playerchoi == "POUCH OF GOLD":
        print (Fore.YELLOW +" >The gold coins shimmer in the palms of your hands. ")
        time.sleep(1.5)
        print(" >They seem to be useful, but you don't know their purpose beside bargaining." + Style.RESET_ALL)
        time.sleep(2)
    elif claymore == True and playerchoi == "SOLDIER'S CLAYMORE" or playerchoi == "SOLDIERS CLAYMORE" or playerchoi == "CLAYMORE" or playerchoi == "SOLDEIR'S CLAYMORE" or playerchoi == "SOLDEIRS CLAYMORE" or playerchoi == "SOLDIER" or playerchoi == "SOLDIERS":
        print (Fore.YELLOW +" >The elegant blade shines in your hands, ready to be weld. ")
        time.sleep(1.5)
        print(" >Using this magnificent weapon for anything besides battle would be a crime!" + Style.RESET_ALL)
        time.sleep(2)
    elif wine == True and playerchoi == "WINE" or playerchoi == "WINE BOTTLE" or playerchoi == "BOTTLE" or playerchoi == "SHATTERED WINE" or playerchoi == "BOTTLE OF WINE":
        if location == 8 and free == True:
            print(Fore.YELLOW + " >The man has already been freed!" + Style.RESET_ALL)
        elif location == 8:
            print(Fore.YELLOW + " >You use the wine bottle to free the trapped person! ")
            time.sleep(1.5)
            print(" >He gasps for breath, thankful for your kindness." + Style.RESET_ALL)
            time.sleep(1.5)
            free = True
        else:
            print (Fore.YELLOW +" >A shattered wine bottle. You can smell a faint trace of grapes if you're close enough." + Style.RESET_ALL)
            time.sleep(2)
    elif part1over == True and playerchoi == "SILVER KEY" or playerchoi == "SILVER" or playerchoi == "KEY":
        if location == 10 or location == 11 or location == 12:
            print(Fore.YELLOW + " >You need to get closer to the gate to use your key!" + Style.RESET_ALL)
            time.sleep(1.5)
        else:
            print(Fore.YELLOW + " >A silver key, gifted to you by the man you saved.")
            time.sleep(1.5)
            print(" >He said it unlocked a keep deep into the forest." + Style.RESET_ALL)
            time.sleep(1.5)
    else:
        print(Fore.YELLOW + " >Pick an option." + Style.RESET_ALL)
if startgame == True:
    start()
while playgame == True:
    printmenu()
    getmenuchoice(playerlocation)
    if getgold == True or meds == True or rustswd == True or claymore == True: #items
        items = True
        itemlist = (" >Pouch of Coins", " >Medical Supplies", " >Rusted Sword", " >Soldier's Claymore")
    while talking == True:
        talkmenu()
        talk(1)
    while fightmon == True:
        monmenu()
        getmonmenuchoice(monster)
