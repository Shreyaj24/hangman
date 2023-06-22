import random

#Class definition
class Hangman():
    '''
    This class represents the Hangman game.
    Attributes:
    word_list: list : input for the list of words
    num_lives: int : number of chances user gets to guess the correct word.
    word : str : Random word choice to guess
    len_word : int : length of the random word.
    word_guessed : list : list of empty letters for the random guessed word.
    num_letters : int : length of the unique letters in the guessed word.
    list_of_guesses : list : list of guessed words.  
    '''
    #Class constructor
    def __init__(self, word_list : list, num_lives:int = 5):
        
        #attributes
        self.word_list = word_list
        self.num_lives = num_lives
        self.word : str = random.choice(self.word_list)
        self.len_word = len(self.word)
        self.word_guessed : list = [''] * self.len_word
        print(self.word_guessed)
        self.num_letters: int = len(set(self.word.lower()))
        self.list_of_guesses : list = []

    #methods
    def check_guess(self, guess):
        '''
        This method validates if the letter guessed by the user is present in the guesssed word.
        '''
        self.guess = guess
        
        if self.guess in self.word.lower()  :
            print(f"Good guess! {self.guess} is in the word.")
            for i in range(len(self.word)):
                if self.guess == self.word[i].lower():
                    self.word_guessed[i] = self.word[i]
            self.num_letters -= 1   
            print(self.word_guessed)   
        else:
            self.num_lives -= 1
            print(f"Sorry, {self.guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")    
        
    def ask_for_input(self):
        '''
        This method validates if the user input is alphabetical and single letter.
        and checks if the user has won or lost the game.
        '''
        
        self.guess = input('enter the letter: ')
        self.guess = self.guess.lower()
        if (len(self.guess) != 1) or (self.guess.isalpha() == False):
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif self.guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.list_of_guesses.append(self.guess)
            self.check_guess(self.guess)


#hangman1 = Hangman(['Apple','Blueberries','Cherry','Dragonfruit','Grapes'], 5 )
#hangman1.ask_for_input()

def play_game(word_list):
    num_lives = 5 
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break    
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives !=0 and game.num_letters <= 0:
            print('Congratulations! you won the game.')  
            break


play_game(['Apple','Samsung','LG','Motorola','Google', 'Amazon', 'Microsoft'])                                   

        

        

