'''
Xuan Guo
CS 5001, Fall 2020

This program takes a sring as the input and checks if the supplied string is a
palindrome or not
'''


def unify_format(word):
    '''
        Function -- unify_format
        Parameters:
            word -- a string input
        Returns:
            A string in lower case and without space
    '''
    return word.lower().replace(" ", "")


def reverse(word):
    '''
        Function -- reverse
        Parameters:
            word -- a string input
        Returns:
            Returns a reversed sting of the input
    '''
    word = unify_format(word)
    new_word = ""
    i = len(word) - 1
    while i >= 0:
        new_word = new_word + word[i]
        i -= 1
    return new_word


def is_palindrome(word):
    '''
        Function -- is_palindrome
        Parameters:
            word -- a string input
        Returns:
            Returns True if the string input is palindrome False if not
    '''
    VAILD_LENGTH = 2
    return len(word) >= VAILD_LENGTH and unify_format(word) == reverse(word)


def main():
    print(is_palindrome("madam Im adam"))
    print(is_palindrome("a"))
    print(is_palindrome("RADar"))


if __name__ == "__main__":
    main()
