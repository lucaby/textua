from utils import clear_window

def player_creation_prompt():
    
    """ Prompts information for player creation """

    finished = False

    while not finished:

        clear_window()

        print("==================================================")
        print("\*/ \*/ \*/ \*/ Character Creation \*/ \*/ \*/ \*/")
        print("==================================================")

        print("_____________ Enter your Hero's name _____________")
        name = str(input("---> "))

        