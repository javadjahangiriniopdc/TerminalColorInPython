# Escape Charcter \033

# # red
# print("\033[32m hi")
# print('javad')
# print("\033[0m")
# print('javad')
# # green
# print("\033[32m hi")
# print('javad')
# print("\033[0m")
# print('javad')
#
# # yellow
# print("\033[33m hi")
# print('javad')
# print("\033[0m")
# print('javad')
#
# print("\033[0m")
#
# # bold
# print("\033[33;1m")
# print('javad')

# for i in range(10):
#     print(f"\033[3{i};1m color{i} Hi \033[0m")

# r, g, b = 0, 0, 255
# print(f"\033[38;2;{r};{g};{b}m  {r}-{g}-{b} test \033[0m")

from colorama import Fore, Back, Style, init, Cursor
pos = lambda y, x: Cursor.POS(x, y)
init()


print(Fore.RED + pos(20, 3) + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.RESET_ALL)
print('back to normal now')

# import sys
# from termcolor import colored, cprint
#
# text = colored('Hello, World!', 'red', attrs=['bold'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red', attrs=['bold'])


# from random import randint
#
# R = randint(0, 255)
# G = randint(0, 255)
# B = randint(0, 255)
#
# print(f"\033[38;2;{R};{G};{B}m  javad \033[0m")
