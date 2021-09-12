import sys
from time import sleep

from colorama import Fore, Back, Style
from colorama import init

init()


def printPos(x, y, text_to_print):  # Function that let us print in desired Position
    sys.stdout.write("\x1b[%d;%df%s" % (x, y, text_to_print))
    sys.stdout.flush()


print(Fore.RED + "Command >>")  # Red-colored print statement
printPos(10, 11, "ddddddd ")  # Changing pos to 1, 11
sleep(1)
printPos(20, 23, "ddddddd ")  # Changing pos to 1, 11
inp = input()  # Getting the input
