########################################
# Name: Dominic Canale
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): 1 (Milestone 0)
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")
        word_to_row("hello", 0)

    def word_to_row(word:str, row:int):
        col = 0
        for index in range(0, len(word)):
            gw.set_square_letter(row, col, word[index])
            col += 1
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
