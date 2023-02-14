from utils import clear_window

def intro():

    """ Prompts the intro text and info """

    clear_window()
    print(""" ▄▄▄· ·▄▄▄▄   ▌ ▐·▄▄▄ . ▐ ▄ ▄▄▄▄▄▄• ▄▌▄▄▄  ▄▄▄ .▄▄▄  .▄▄ ·      ▄ .▄      • ▌ ▄ ·. ▄▄▄ .
         ▐█ ▀█ ██▪ ██ ▪█·█▌▀▄.▀·•█▌▐█•██  █▪██▌▀▄ █·▀▄.▀·▀▄ █·▐█ ▀.     ██▪▐█▪     ·██ ▐███▪▀▄.▀·
         ▄█▀▀█ ▐█· ▐█▌▐█▐█•▐▀▀▪▄▐█▐▐▌ ▐█.▪█▌▐█▌▐▀▀▄ ▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄    ██▀▐█ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄
         ▐█ ▪▐▌██. ██  ███ ▐█▄▄▌██▐█▌ ▐█▌·▐█▄█▌▐█•█▌▐█▄▄▌▐█•█▌▐█▄▪▐█    ██▌▐▀▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌
          ▀  ▀ ▀▀▀▀▀• . ▀   ▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀ .▀  ▀ ▀▀▀▀     ▀▀▀ · ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀ """)
    print("                         Dream fantasy home right in your terminal!")
    print()
    input("...Press any key to continue...")

def menu():
    
    """ Menu functionality """

    def menu_text():

        """ Prompts the menu text """

        clear_window()
        print("Type the number of the option, then press the 'enter' key to select")
        print("1. New game")
        print("2. Load game")
        print("3. Credits")
        print("4. Quit")

    def menu_select():
        
        """ Handles menu choices """
        
        opt = str(input("---> "))

        if opt == '1':
            pass
        elif opt == '2':
            pass
        elif opt == '3':
            pass
        elif opt == '4':
            quit()
        else:
            menu_text()
            menu_select()

    # Displays menu
    menu_text()
    menu_select()


def main():

    """ Main program to start the game"""

    intro()
    menu()

main()