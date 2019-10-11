# Makes a random phrase of specified input length. Letters a-z and space
from letter_conversion import letter_conversion
from random import randint


def rand_string(length):

    word = ["a"] * length
    for i in range(len(word)):
        word[i] = letter_conversion(randint(0, 26))  # 26 characters including space
    return word


# returns a character between a-z or space.
def rand_char():
    character = letter_conversion(randint(0, 26))
    return character
