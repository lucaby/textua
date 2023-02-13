from utils import clear_window

def intro():

    """ Prompts the intro text and info """

    clear_window()
    print(""" ▄▄▄· ·▄▄▄▄   ▌ ▐·▄▄▄ . ▐ ▄ ▄▄▄▄▄▄• ▄▌▄▄▄  ▄▄▄ .▄▄▄  .▄▄ ·      ▄ .▄      • ▌ ▄ ·. ▄▄▄ .
             ▐█ ▀█ ██▪ ██ ▪█·█▌▀▄.▀·•█▌▐█•██  █▪██▌▀▄ █·▀▄.▀·▀▄ █·▐█ ▀.     ██▪▐█▪     ·██ ▐███▪▀▄.▀·
             ▄█▀▀█ ▐█· ▐█▌▐█▐█•▐▀▀▪▄▐█▐▐▌ ▐█.▪█▌▐█▌▐▀▀▄ ▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄    ██▀▐█ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄
             ▐█ ▪▐▌██. ██  ███ ▐█▄▄▌██▐█▌ ▐█▌·▐█▄█▌▐█•█▌▐█▄▄▌▐█•█▌▐█▄▪▐█    ██▌▐▀▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌
              ▀  ▀ ▀▀▀▀▀• . ▀   ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀ .▀  ▀ ▀▀▀▀     ▀▀▀ · ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ """)
    print("Dream fantasy home right in your terminal!")
    print()
    input("...Press any key to continue...")

def menu():
    
    """ Menu functionality """
    
    clear_window()
    print("Type the number of the option, then press the 'enter' key to select")
    print("1. New game")
    print("2. Load game")
    print("3. Credits")
    print("4. Quit")

    choice = int(input("--->"))

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        quit()

def main():

    """ Main program to start the game"""

    # intro()
    # menu()