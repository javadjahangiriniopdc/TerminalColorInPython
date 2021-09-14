from random import randint

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)

print(f"\033[38;2;{R};{G};{B}m  javad \033[0m")