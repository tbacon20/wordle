# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, WordleGWindow, N_COLS, N_ROWS

def wordle():
    # THIS ASSIGNES A RANDOM WORD
    word = FIVE_LETTER_WORDS[random.randint(0, len(FIVE_LETTER_WORDS) - 1)]
    word = word.upper()
    # THIS CAN BE USED FOR TESTING
    print(word)

    def enter_action(s):
        row = gw.get_current_row()
        print("row " + str(row))
        guess = ""

        # THIS CONVERTS THE GUESS INTO A WORD AND 
        # CHECKS IT AGAINST THE WORD BANK
        for i in range(0, N_COLS) :
            if gw.get_square_letter(row,i) != " ":
                guess += gw.get_square_letter(row,i)

        # IF THE USER SUBMITTED A WORD THAT IS TOO
        # SHORT, THEY MUST FIX IT
        if len(guess) < 5 :
            gw.show_message("Word not long enough")

        # IF THE WORD IS GUESSED, YOU WIN
        elif word == guess :
            gw.show_message("YOU WIN")

            # ALL LETTERS WILL TURN GREEN
            for i in range(0, N_COLS) :
                gw.set_square_color(row,i,CORRECT_COLOR)

        # IF YOU RUN OUT OF ROWS, YOU LOSE
        elif (row + 1 == N_ROWS) :
            gw.show_message("You Lose. The word was " + word + ".")

        # THIS COMPLETES CHECKPOINT TWO BY DISPLAYING
        # WEATHER THE WORD IS IN THE WORD BANK OR NOT
        elif guess.lower() in FIVE_LETTER_WORDS :
            gw.show_message("Good guess! That is in the word list.")

            # INITIATE A STRING OF ALL GUESSED LETTERS
            guessed = ""

            # CHECK FOR LETTERS IN THE CORRECT PLACE
            # AND TURN THEM GREEN
            for i in range(0, N_COLS) :
                if guess[i] == word[i]:
                    gw.set_square_color(row,i,CORRECT_COLOR)
                    guessed += guess[i]

            # CHECK FOR CORRECT LETTERS IN THE WRONG
            # PLACE AND TURN THEM YELLOW
            for i in range(0, N_COLS) :
                if (guess[i] in word) and (guess[i] not in guessed):
                    gw.set_square_color(row,i,PRESENT_COLOR)
                    guessed += guess[i]

            # MOVE TO NEXT ROW
            gw.set_current_row(row + 1)
        else :
            # ALL LETTERS WILL RESET
            for i in range(0, N_COLS) :
                gw.set_square_letter(row,i," ")
                gw.set_current_row(row)
            
            # DISPLAY NOT IN WORD LIST ERROR MESSAGE 
            # IF THE USER INPUTS AN INCORRECT WORD
            gw.show_message("Not in word list.")

        

    # THIS WILL CREATE THE WINDOW AND ADD A LISTENER
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # THIS COMPLETES CHECKPOINT ONE BY SELECTING A
    # RANDOM WORD AND DISPLAYS IT IN THE TOP ROW
    # for i in range(0, len(word)) :
    #   gw.set_square_letter(0,i, word[i])
    # gw.show_message("CHECKPOINT 1 COMPLETE")

# Startup code

if __name__ == "__main__":
    wordle()