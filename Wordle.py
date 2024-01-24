# File: Wordle.py

import random
from WordleDictionary import FIVE_LETTER_WORDS

from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    
    def enter_action(s):

        def compare_guess(target, guess):
            nonlocal current_row

            for i in range(0, 5):
                if target[i] == guess[i]:
                    gw.set_square_color(current_row, i, CORRECT_COLOR)
                elif guess[i] in target:
                    if target.count(guess[i]) > guess[:i].count(guess[i]):
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                    else:
                        gw.set_square_color(current_row, i, MISSING_COLOR)
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)

            if target == guess:
                gw.show_message("Correct!")
            else:
                gw.show_message("Incorrect! Try again")
                current_row += 1
                gw.set_current_row(current_row)

        l1 = gw.get_square_letter(current_row, N_COLS - 5)
        l2 = gw.get_square_letter(current_row, N_COLS - 4)
        l3 = gw.get_square_letter(current_row, N_COLS - 3)
        l4 = gw.get_square_letter(current_row, N_COLS - 2)
        l5 = gw.get_square_letter(current_row, N_COLS - 1)

        user_word = (l1 + l2 + l3 + l4 + l5)
        user_array = list(user_word)
        
        if user_word.lower() in FIVE_LETTER_WORDS:
            compare_guess(rand_array, user_array)


    
    print("Random word:", random_word)

    current_row = 0
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    


# Startup code

if __name__ == "__main__":
    wordle()


