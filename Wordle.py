########################################
# Name: Dominic Canale
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr): 1 (Milestone 0), 1 (Milestone 1), 3 (Milestone 2)
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    debug = True
    def enter_action():
        secretword = "frill"
        currentrow = 0
        # What should happen when RETURN/ENTER is pressed.
        # gw.show_message("You need to implement this method")
        currentword = str.lower(word_from_row(currentrow))
        debug and print("Current word is", currentword)
        if check_if_word_is_cool(currentword) == True:
            debug and print('starting process')
            nusecret = ""
            unmatched = currentword
            for i in range(0, N_COLS):
                debug and print("checking if", currentword[i], "=", secretword[i])
                if currentword[i] == secretword[i]:
                    debug and print('this letter is correct')
                    gw.set_square_color(currentrow, i, CORRECT_COLOR)
                    nusecret += '_'
                    unmatched = unmatched[:i] + '*' + unmatched[i+1:]
                    debug and print('New secret var is', nusecret, 'and new guess var is', unmatched)
                else:
                    debug and print('the current letter', currentword[i], 'is NOT correct')
                    nusecret += secretword[i]
            debug and print('New guess var is', unmatched, 'and new secret var is', nusecret)
            for i in range(0, N_COLS):
                if gw.get_square_color(currentrow, i) != CORRECT_COLOR:
                    debug and print('checking if', unmatched[i], 'within', nusecret)
                    if unmatched[i] in nusecret:
                        debug and print('yes!')
                        gw.set_square_color(currentrow, i, PRESENT_COLOR)
                        debug and print("removing letter", unmatched[i], "from", nusecret)
                        nusecret = censor_letter(unmatched[i], nusecret)
                        unmatched = unmatched[:i] + '*' + unmatched[i+1:]
                        debug and print('New secret var is', nusecret, 'and new guess var is', unmatched)
                    else:
                        debug and print('no')
                        gw.set_square_color(currentrow, i, MISSING_COLOR)
                        debug and print('Secret var is', nusecret, 'and guess var is', unmatched)

    def censor_letter(letter:str, word:str) -> str:
        for index in range(len(word)):
            if word[index] == letter:
                return word[:index] + '_' + word[index+1:]
        return word 

    def check_if_word_is_cool(word:str):
        import english
        if str.lower(word) in ENGLISH_WORDS and len(word) == 5:
            gw.show_message('jfgheriwyugkir3uwefgyjuekrwncbuyriwenlcygrbuew')
            return True
        else:
            gw.show_message('not in word list')
            return False

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
