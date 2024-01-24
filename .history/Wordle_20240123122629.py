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
    
    def enter_action(s):

        def compare_guess(row, target, guess):
            for i in range(0,5):
                if target[i] == guess[i]:
                    gw.set_square_color(row, guess[i], CORRECT_COLOR)
                elif guess[i] in target:
                    gw.set_square_color(row, guess[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(row, guess[i], MISSING_COLOR)
            print()  # Move to the next line after printing the guess

        l1 = gw.get_square_letter(N_ROWS -6, N_COLS - 5)
        l2 = gw.get_square_letter(N_ROWS -6, N_COLS - 4)
        l3 = gw.get_square_letter(N_ROWS -6, N_COLS - 3)
        l4 = gw.get_square_letter(N_ROWS -6, N_COLS - 2)
        l5 = gw.get_square_letter(N_ROWS -6, N_COLS - 1)
        user_word = (l1 + l2 + l3 + l4 + l5)
        user_array = list(user_word)
        
        if user_word.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Valid Word")
            for i in range(0,5):
                if user_array[i] == rand_array[i]:
                    gw.set_square_color(0, i, CORRECT_COLOR)
                    gw.show_message("correct" + i)
                elif user_array[i] in rand_array:
                    gw.set_square_color(0, i, PRESENT_COLOR)
                    gw.show_message("present" + i)
                else:
                    gw.set_square_color(0, i, MISSING_COLOR)
                    gw.show_message("correct" + i)
        else:
            gw.show_message("Not in word list")
        
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
        
    random_word = random.choice(FIVE_LETTER_WORDS)
    rand_array = list(random_word)

    print("Random word:", random_word)
         
    for col, letter in enumerate(random_word):
        gw.set_square_letter(N_ROWS - 6, N_COLS - 5 + col, letter[0])
        
        
    


# Startup code

if __name__ == "__main__":
    wordle()
