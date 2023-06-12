#create while loop to check for the alphabets in the input provided by the user

import milestone_2

random_fruit = milestone_2.word
random_fruit = random_fruit.lower()
print(random_fruit)
'''
import random

word_list = ['Apple','Blueberries','Cherry','Dragonfruit','Grapes']
print(word_list)
word = random.choice(word_list)
print(word)

while True:
    guess = input('enter the letter: ')
    if len(guess) == 1 and guess.isalpha():
        if guess.lower() in word.lower() :
            print(f'Good guess! {guess} is in the word.')
            break    
        else:
            print(f'Sorry, {guess} is not in the word. Try again')
            
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
'''
def check_guess(guess):
    #while True:
        if guess in random_fruit :
            print(f'Good guess! {guess} is in the word.') 
        else:
            print(f'Sorry, {guess} is not in the word. Try again')
            ask_for_input()

def ask_for_input():
    while True:
        guess = input('enter the letter: ')
        guess = guess.lower()
        print(guess)
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()