from utils import clear_window

choice = ["X", " ", " ", " "]


def prompt_intro():

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
    
    """ Prompts the menu choices """

    clear_window()
    print("Use the arrow keys to change selection, then press the 'enter' key to select")
    print("[ "+choice[0]+" ] New game")
    print("[ "+choice[1]+" ] Load game")
    print("[ "+choice[2]+" ] Credits")
    print("[ "+choice[3]+" ] Quit")

def main():

    """ Main program to start the game"""

    # prompt_intro()
    # prompt_menu()
    # 