'''
Xuan Guo
CS5001, Fall 2020

This program helps user to identify if a string contain a vowel
'''


BASE = 1
NONE = 0


def contains_vowel(lst):
    '''
        Function -- contains_vowel
        Parameters:
            lst -- a list contains none or several words as string
        Returns:
            True if the given list contains at least a vowel in every word
            in the list, False if any word does not contains at least a vowel
    '''
    if len(lst) == NONE:
        return False
    if len(lst) == BASE:
        return check_vowels(lst[0])
    else:
        return check_vowels(lst[0]) and check_vowels(lst[1:][0])


def check_vowels(word):
    '''
        Function -- check_vowels
        Parameters:
            word -- an English word as a string
        Returns:
            True if the word contains at least one vowel, False if the word
            contains none vowel
    '''
    VOWELS = ["a", "e", "i", "o", "u"]
    if len(word) == NONE:
        return False
    if len(word) == BASE:
        return word[0].lower() in VOWELS
    else:
        return (word[0].lower() in VOWELS) or check_vowels(word[1:].lower())
