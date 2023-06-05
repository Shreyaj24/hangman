#Import random library for random choice program 
import random

#create list
word_list = ['Apple','Blueberries','Cherry','Dragonfruit','Grapes']
print(word_list)
word = random.choice(word_list)
print(word)

# function to choose validate the letter for valid input 
def single_letter():
    guess = input('enter the letter: ')
    if len(guess) == 1 and guess.isalpha() :
        print('Good guess!')
    else:
        print('Oops! That is not a valid input.')    

    print(guess)

#calling the function 
single_letter()    