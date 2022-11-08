import random
from words import words
import string
# print(words)

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    while '_' in word or ' ' in word: # while - or ' ' is in this word keep choosing the word
        word = random.choice(words)

    return word

# which letters we guess and which letters we correctly guessed
def hangman():
    word = get_valid_word(words)
    word_letters = set(words) #variable that saves letters in the word
    alphabet = set(string.ascii_uppercase) #import list of uppercase characters
    used_letters = set() # to track what the user has guessed

    #getting user input
    user_letter = input('Guess a letter: ').upper() #lower case a is diff than a uppercase A in python
    if user_letter in alphabet - used_letters: # if this is a valid char in the alphabet that i havent used yet
        used_letters.add(user_letter) # then im gonna add this to my used_letters set
        if user_letter in word_letters: # if the letter that i just guessed is in the word, then Im gonna remove that letter from word letters
            word_letters.remove(user_letter) # every time i guesse correctly then this word letters (which is keeping track of all letters in a word) decreases

    elif user_letter in used_letters: # if this user letter that user just entered is in used letters, that means they already used it before and is an invalid guess. Then print sth saying You already used that word
        print('You have already used that character. Please try again') #559

    #


user_input = input('Type something') #ask for user input in python directly
print(user_input) # then user can type a character and we can use that as input