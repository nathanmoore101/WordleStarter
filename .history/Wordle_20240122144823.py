# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

# test suzi

def wordle():


    def enter_action(s):
        l1 = gw.get_square_letter(N_ROWS -6, N_COLS - 5)
        l2 = gw.get_square_letter(N_ROWS -6, N_COLS - 4)
        l3 = gw.get_square_letter(N_ROWS -6, N_COLS - 3)
        l4 = gw.get_square_letter(N_ROWS -6, N_COLS - 2)
        l5 = gw.get_square_letter(N_ROWS -6, N_COLS - 1)
        user_word = (l1 + l2 + l3 + l4 + l5)

        if user_word.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        else:
            gw.show_message("Valid Word")
            for o in :
                for i
                if li == random_word[0]:
                    l1 = 
                
            

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    random_word = random.choice(FIVE_LETTER_WORDS)

    for col, letter in enumerate(random_word):
        gw.set_square_letter(N_ROWS - 6, N_COLS - 5 + col, letter[0])

        
    

    print("Random word:", random_word)


# Startup code

if __name__ == "__main__":
    wordle()
