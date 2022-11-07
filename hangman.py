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
    alphabet - set(string.ascii_uppercase) #import list of uppercase characters
    used_letters = set() # to track what the user has guessed
