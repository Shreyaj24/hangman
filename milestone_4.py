import random

#Class definition
class Hangman():
    

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
        while True:
            if (self.num_letters >= 1 and self.num_lives >= 1) :
                self.guess = input('enter the letter: ')
                self.guess = self.guess.lower()
                if (len(self.guess) != 1) or (self.guess.isalpha() == False):
                    print('Invalid letter. Please, enter a single alphabetical character.')
                elif self.guess in self.list_of_guesses:
                    print("You already tried that letter!")
                else:
                    self.list_of_guesses.append(self.guess)
                    self.check_guess(self.guess)
            elif self.num_letters == 0:
                print ('Yay! You have won')
                break           
            else:
                print ('Sorry! You have lost')
                break

hangman1 = Hangman(['Apple','Blueberries','Cherry','Dragonfruit','Grapes'], 5 )
hangman1.ask_for_input()

                

        

        

