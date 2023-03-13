
import os
from colorama import Fore, Back, Style #pip install colorama

def main() :
    print(Fore.YELLOW + "     ____  _________")
    print("    |    |/   _____/")
    print("    |    |\_____  \ ")
    print("/\\__|    |/        \\")
    print("\\________/_______  /")
    print("                 \\/ ")
    print("")
    print("Remove console.X() functions from JavScript file" + Fore.RESET)

    fileName = input(Fore.CYAN + "File name (exclude .js extension): " + Fore.RESET)
    try :
        file = open(fileName + ".js", "r+")
    except :
        print(Fore.RED + "An error occurred opening the file" + Fore.RESET)
        return

    print(Back.CYAN + "Succesfully opened " + fileName + ".js" + Back.RESET)
    print("\n")

    tmp = open("tmp", "w")

    for line in file :
        for char in line :
            if char == ";" :
                print(char, end="\n")
                tmp.write(char + "\n")
            else :
                print(char, end="")
                tmp.write(char)

if __name__ == "__main__" :
    os.system("")
    main()
