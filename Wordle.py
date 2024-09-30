########################################
# Name: Dominic Canale
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): 1 (Milestone 0), 1 (Milestone 1), 3 (Milestone 2), 30m (Milestone 3),
# 2 (Milestone 4), 10m (Milestone 5)
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    secretword = ""
    while len(secretword) != 5:
        secretword = random.choice(ENGLISH_WORDS)
    
    # The main function to play the Wordle game.
    def enter_action():
        currentword = str.lower(word_from_row(gw.get_current_row()))
        if check_if_word_is_cool(currentword) == True:
            nusecret = ""
            unmatched = currentword
            if currentword == secretword:
                for i in range(0, N_COLS):
                    gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                    gw.set_key_color(currentword[i], CORRECT_COLOR)
                N_ROWS = gw.get_current_row()
                if N_ROWS == 0:
                    gw.show_message("Cheater") # Haha
                if N_ROWS == 1:
                    gw.show_message("Magnificent")
                if N_ROWS == 2:
                    gw.show_message("Impressive")
                if N_ROWS == 3:
                    gw.show_message("Splendid")
                if N_ROWS == 4:
                    gw.show_message("Great")  
                if N_ROWS == 5:
                    gw.show_message("Phew")
                return 0
            else:
                for i in range(0, N_COLS):
                    if currentword[i] == secretword[i]:
                        gw.set_square_color(gw.get_current_row(), i, CORRECT_COLOR)
                        gw.set_key_color(currentword[i], CORRECT_COLOR)
                        nusecret += '_'
                        unmatched = unmatched[:i] + '*' + unmatched[i+1:]
                    else:
                        nusecret += secretword[i]
                for i in range(0, N_COLS):
                    if gw.get_square_color(gw.get_current_row(), i) != CORRECT_COLOR:
                        if unmatched[i] in nusecret:
                            gw.set_square_color(gw.get_current_row(), i, PRESENT_COLOR)
                            if gw.get_key_color(unmatched[i]) != CORRECT_COLOR:
                                gw.set_key_color(unmatched[i], PRESENT_COLOR)
                            nusecret = censor_letter(unmatched[i], nusecret)
                            unmatched = unmatched[:i] + '*' + unmatched[i+1:]
                        else:
                            gw.set_square_color(gw.get_current_row(), i, MISSING_COLOR)
                            if gw.get_key_color(unmatched[i]) == UNKNOWN_COLOR:
                                gw.set_key_color(unmatched[i], MISSING_COLOR)
                if gw.get_current_row() == N_COLS:
                    gw.show_message("The word was")
                    gw.show_message(secretword)
                gw.set_current_row(gw.get_current_row() + 1)
        else:
            gw.show_message("Not in word list")

    def censor_letter(letter:str, word:str) -> str:
        for index in range(len(word)):
            if word[index] == letter:
                return word[:index] + '_' + word[index+1:]
        return word 

    def check_if_word_is_cool(word:str):
        import english
        return str.lower(word) in ENGLISH_WORDS and len(word) == 5

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
