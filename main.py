import os

os.system("title ZYNC - Hash Identifier")
from colored import fg
color = fg("45")
print(color + """

███████╗██╗░░░██╗███╗░░██╗░█████╗░
╚════██║╚██╗░██╔╝████╗░██║██╔══██╗
░░███╔═╝░╚████╔╝░██╔██╗██║██║░░╚═╝
██╔══╝░░░░╚██╔╝░░██║╚████║██║░░██╗
███████╗░░░██║░░░██║░╚███║╚█████╔╝
╚══════╝░░░╚═╝░░░╚═╝░░╚══╝░╚════╝░

by Akiko#4200
""")
print("Enter HASH")
string = input(">> ")
stringlength = len(string)

lengths = (32,64,8,4,40,56,128,96)

if stringlength in lengths:

    if stringlength == 32:
        print("MD5")
        input("Press ENTER to close...")

    if stringlength == 64:
        print("SHA256")
        input("Press ENTER to close...")
    if stringlength == 4:
        print("CRC-16")
        input("Press ENTER to close...")
    if stringlength == 8:
        print("CRC-32")
        input("Press ENTER to close...")
    if stringlength == 40:
        print("SHA1")
        input("Press ENTER to close...")
    if stringlength == 56:
        print("SHA384")
        input("Press ENTER to close...")
    if stringlength == 128:
        print("SHA512")
        input("Press ENTER to close...")

    if stringlength == 96:
        print("SHA1")
        input("Press ENTER to close...")
else:
    print("Couldnt identify Hash type")
    input("Press ENTER to close...")
