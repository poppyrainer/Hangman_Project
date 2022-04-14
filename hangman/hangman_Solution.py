
# I got rid of some code here "-> None", what does that mean?
# need to take into account lower case of letter
# need to install python v3


import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = list("_"*len(self.word))
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_letters = []
        
        print("The mistery word has " + str(self.num_letters) +" letters")
        print(self.word_guessed)
        pass

    def check_letter(self, letter):
        if letter in list(self.word):
            self.num_letters = self.num_letters - 1
            my_word_list = list(self.word)
            position_lst = []
            for pos,char in enumerate(self.word):
                if(char == letter):
                    position_lst.append(pos)
            print(position_lst)
            for i in position_lst:
                self.word_guessed[i] = letter  
        else:
            self.num_lives = self.num_lives - 1

    def ask_letter(self):
            letter = raw_input("enter a letter: ")
            if len(letter) >1:
                 print("Please, enter just one character")
            if letter in self.list_letters:
                print(letter + " was already tried")
            else:
                self.list_letters.append(letter)
                self.check_letter(letter)

def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game_won = False
    while game_won == False:
        if (game.word_guessed) == list(game.word):
            print("Congratulations! You won!")
            break
        elif game.num_lives == 0:
            print("You lost! The word was " + game.word)
            break
        else:
            game.ask_letter()

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)