# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR, KEY_COLOR 

# test suzi

def wordle():
    
    random_word = random.choice(FIVE_LETTER_WORDS)
    characters_array = list(random_word)

    def enter_action(s):
        
        def color_print(char, color):
            print(colors[color] + char + end_color, end='')

        def compare_guess(target, guess):
            for i in range(1,6):
                if target[i] == l[i]:
                    color_print(l[i], CORRECT_COLOR)
                elif guess[i] in target:
                    color_print(l[i], PRESENT_COLOR)
                else:
                    color_print(l[i], MISSING_COLOR)
            print()  # Move to the next line after printing the guess

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
            compare_guess
                
            

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)


    for col, letter in enumerate(random_word):
        gw.set_square_letter(N_ROWS - 6, N_COLS - 5 + col, letter[0])

        
    

    print("Random word:", random_word)


# Startup code

if __name__ == "__main__":
    wordle()
