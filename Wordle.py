########################################
# Name: Dominic Canale
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): 1 (Milestone 0), 1 (Milestone 1)
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    debug = True
    def enter_action():
        currentrow = 0
        # What should happen when RETURN/ENTER is pressed.
        # gw.show_message("You need to implement this method")
        currentword = word_from_row(currentrow)
        debug and print("Current word is", currentword)
        check_if_word_is_cool(currentword)

    def check_if_word_is_cool(word:str):
        import english
        if str.lower(word) in ENGLISH_WORDS and len(word) == 5:
            gw.show_message('jfgheriwyugkir3uwefgyjuekrwncbuyriwenlcygrbuew')
        else:
            gw.show_message('not in word list')

    def word_to_row(word:str, row:int):
        col = 0
        for index in range(0, len(word)):
            gw.set_square_letter(row, col, word[index])
            col += 1

    def word_from_row(row:int) -> str:
        col = 0
        word = ""
        for i in range(5):
            word += str(gw.get_square_letter(row, col))
            col += 1
        return word

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
