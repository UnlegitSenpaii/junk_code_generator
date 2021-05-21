from random import randint
import sys
import os

userinput = input("how many parts do you want?\n")
os.system('cls')
loops = int(userinput)
print("#define _JUNK_CONTENT_ \\")

for i in range(loops):
    randomEmit = "__asm _emit 0x"
    randomNumber = randint(10, 99)
    randomEmit += str(randomNumber)

    if randint(0, 4) == 1:
        randomEmit += " \\ \n__asm nop"

    if i != loops - 1:
        randomEmit += " \\"

    print(randomEmit)

print("#define JUNK_BLOCK(s) __asm jmp s _JUNK_CONTENT_ __asm s:")
print("//use with JUNK_BLOCK(variablename);")
