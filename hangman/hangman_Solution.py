import random

class Hangman:
    """
    A class to represent the Hangman Game
    """

    def __init__(self, word_list: list, num_lives=5) -> None:
        """
        Constructs attributes for the Hangman Game Object
        """
        self.word = random.choice(word_list)
        self.word_guessed = list("_"*len(self.word))
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.list_letters = []
        
        pass

    def check_letter(self, letter:str) -> None:
        """
        Accepts a letter and checks to see whether it is in the word.
        If it is - it adds the letter to the guessed word.
        Otherwise, it decreases the lives by 1
        """
        if letter.lower() in list(self.word):
            # self.num_letters = self.num_letters - 1
            # my_word_list = list(self.word)
            position_lst = []
            for pos,char in enumerate(self.word):
                if(char == letter):
                    position_lst.append(pos)
            for i in position_lst:
                self.word_guessed[i] = letter
            print("Correct guess!")
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1
            print("Incorrect guess")
            print("You have " + str(self.num_lives) + " lives remaining")

    def ask_letter(self) -> None:
        """Asks the user to input a letter. 
        Checks to see whether this is a valid input.
        Passes the letter to the check_letter function
        """

        letter = input("enter a letter: ")
        if len(letter) >1:
                print("Please, enter just one character")
        if letter in self.list_letters:
            print(letter + " was already tried")
        else:
            self.list_letters.append(letter)
            self.check_letter(letter)


def play_game(word_list: list ) -> None:
    """
    Instantiates an instance of the Hangman class as our game.
    Creates a while loop to keep asking for a letter until
    either the user of the computer wins
    """

    game = Hangman(word_list, num_lives=5)
    print("The mistery word has " + str(game.num_letters) +" letters")
    print(game.word_guessed)

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