from time import sleep
import os

from colorama import init, Cursor, Fore, Style, Back


clear = lambda: os.system('cls')
pos = lambda y, x: Cursor.POS(x, y)

init()

print(Fore.RED + pos(5, 20) + 'amin jafari')
sleep(.5)
clear()
print(Fore.RED + pos(5, 25) + 'amin jafari')
sleep(.5)
clear()
print(Fore.RED + pos(5, 30) + 'amin jafari')
sleep(.5)
clear()
print(Fore.RED + pos(5, 35) + 'amin jafari')
sleep(.5)
clear()
print(Fore.RED + pos(5, 40) + 'amin jafari')
print(Style.RESET_ALL)
ch = input()

# please run in terminal
#
# goto folder
# run cmd
# cd venv
# cd script
# active
# cd ../..
# python -m cursorpos.py
