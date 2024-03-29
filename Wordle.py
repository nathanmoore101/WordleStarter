# File: Wordle.py

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, CB_CORRECT_COLOR, CB_PRESENT_COLOR, KEY_LABELS

def wordle():
    
    def colorblind_callback():
        global CORRECT_COLOR, PRESENT_COLOR
        # Toggle between colorblind and regular mode
        if CORRECT_COLOR == "#66BB66":
            # Switch to colorblind mode
            CORRECT_COLOR = CB_CORRECT_COLOR
            PRESENT_COLOR = CB_PRESENT_COLOR
        else:
            # Switch to regular mode
            CORRECT_COLOR = "#66BB66"
            PRESENT_COLOR = "#CCBB66"

        # Update colors in the WordleGWindow
        for i in range(N_ROWS):
            for j in range(N_COLS):
                current_color = gw.get_square_color(i, j)
                if current_color == "#66BB66":
                    gw.set_square_color(i, j, CORRECT_COLOR)
                elif current_color == "#CCBB66":
                    gw.set_square_color(i, j, PRESENT_COLOR)
                # Add similar checks for other colors if needed

        # Update key colors
        for row in KEY_LABELS:
            for label in row:
                current_color = gw.get_key_color(label)
                if current_color == "#66BB66":
                    gw.set_key_color(label, CORRECT_COLOR)
                elif current_color == "#CCBB66":
                    gw.set_key_color(label, PRESENT_COLOR)
            
    def enter_action(s):
        def compare_guess(target, guess):
            nonlocal current_row


            for i in range(0, 5):
                if target[i] == guess[i]:
                    gw.set_square_color(current_row, i, CORRECT_COLOR)
                    gw.set_key_color(guess[i], CORRECT_COLOR)
                elif guess[i] in target:
                    if target.count(guess[i]) > guess[:i].count(guess[i]):
                        gw.set_square_color(current_row, i, PRESENT_COLOR)
                        if gw.get_key_color(guess[i]) != CORRECT_COLOR:
                            gw.set_key_color(guess[i], PRESENT_COLOR)
                    else:
                        gw.set_square_color(current_row, i, MISSING_COLOR)
                        gw.set_key_color(guess[i], MISSING_COLOR)
                else:
                    gw.set_square_color(current_row, i, MISSING_COLOR)
                    gw.set_key_color(guess[i], MISSING_COLOR)

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
        else:
            gw.show_message("Not in word list")
            
    random_word = random.choice(FIVE_LETTER_WORDS)
    rand_array = list(random_word.upper())
    
    print("Random word:", random_word)

    current_row = 0
    gw = WordleGWindow(colorblind_callback)
    gw.add_enter_listener(enter_action)
    
    

# Startup code

if __name__ == "__main__":
    wordle()



