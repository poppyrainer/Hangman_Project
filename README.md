# Hangman Project

## Table of contents
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


# Intoduction

This is the first training project as part of The AiCore 16w Accelerator programme. 

The project is to build a programme that allows a user to play the traditional childhood game of "hangman".

The game is played as follows:

1) The computer randomly selects a word from a list of words
2) The user inputs a character to see if it exists in the word
3) If the character exists, they continue to guess until the word is guessed
4) If the character dose not exist then they loose a life
5) The computer wins if the player looses all their lives before the word is guessed. The player wins if they guess the word before they loose all their lives.

# Technologies Used
- Python

# Technical Description
- The main function of the programme is the *play_game* function which takes in a hardcoded list of words as the argument.
- This function then instantiates the *Hangman Class* and runs a while loop that asks the user for input and validates this input. The while loop breaks when either the computer or the user wins the game.
- The *Hangman Class* has three methods:
    - *innit* - the constructor method contains the object attributes which include:
        - the word itself
        - the word guessed (which includes _ for unknown letters)
        - the number of letters in the word
        - the number of lives remaining
        - list of letters guessed
    - *ask_letter* - this is called within the while loop. It performs three steps:
        1. It checks that the letter is valid
        2. It checks to see whether the letter has been tried before
        3. It checks to see if the letter is in the word via the *check_letter* method
    - *check_letter* - for the inputted letter, this method checks the word to see where the letter exists in this word and adds the guessed letters to the word which is displayed to the user. If it doesn't exist, it reduces the lives by one.




