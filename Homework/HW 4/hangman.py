'''
Xuan Guo
CS5001, Fall 2020

This program asks a player to guess a secret word one letter at a time and
guesses 6 times for letters, if the user guessed the correct word they win,
otherwise, they lose
'''


def cover_word(word):
    '''
        Function -- cover_word
        Parameters:
            word -- A word
        Returns:
            Returns a string which replaced every letter in the given word
            with '_'
    '''
    return "_" * len(word)


def letter_or_word(user_input):
    '''
        Fuction -- letter_or_word
        Parameters:
            user_input -- a string
        Returns:
            Returns True if the string length is 1, False if not equal to 1
    '''
    LETTER_LENGTH = 1
    return len(user_input) <= LETTER_LENGTH


def replace_covered(word, user_input, covered_word):
    '''
        Function -- replace_covered
        Parameters:
            word -- an english word
            user_input -- a string which length equals to 1
            covered_word -- a string has the same length with 'word', but
            replaced its letters with '_'
        Returns:
            Returns a new covered word but replaced the actually letter if
            'user_input' is in the 'word'
    '''
    i = 0
    word_length = len(word)
    result = ""
    WRONG_ANS = "_"
    while i < word_length:
        if covered_word[i] != WRONG_ANS:
            result += covered_word[i]
        else:
            if user_input != word[i]:
                result += WRONG_ANS
            else:
                result += user_input
        i += 1
    return result


def process_letter(user_input, word, covered, guesses):
    '''
        Function -- process_letter
        Parameters:
            user_input -- an English letter from user's guess
            word -- an English word for user to guess
            covered -- a word covered with '_'
            guesses -- user's guesses so far
        Returns:
            Returns guessed letters and covered word with description
    '''
    result = ""
    if user_input not in guesses or not user_input:
        if user_input not in guesses:
            guesses += user_input.upper()
            covered = replace_covered(word, user_input, covered)
        result = covered + "\n" + "Your guesses so far: " + guesses
    elif user_input:
        result = "You've already guessed that letter!" + "\n" + covered +\
            "\n" + "Your guesses so far: " + guesses
    return result, guesses, covered


def check_word(word, user_input, covered, guesses):
    '''
        Function -- check_word
        Parameters:
            word -- a english word
            user_input -- another english word
        Returns:
            Returns "You win!" and win times as 1 if 'word' and 'user_input'
            are equal. Returns "You lose! The word was " plus actual word and
            win times as 0 if 'word' and 'user_input' are not equal
        '''
    if_finished = False
    if user_input == word:
        result = "You win!"
        win_num = 1
        if_finished = True
    else:
        result = covered + "\n" + "Your guesses so far: " + guesses
        win_num = 0
    return result, win_num, if_finished


def process_input(user_input, word, covered, guesses):
    '''
        Function -- process_input
        Parameters:
            user_input -- user's word or letter guesses
            word -- a word needs to be guess
            covered -- the word needs to be guess but covered with '_'
            guesses -- user's guesses so far
        Returns:
            Returns guess failed discription if the user still didn't get
            correct answer if guesses time reach to 6. Returns the word guess
            result if the user guesses a word
    '''
    MAXIUM_TASK = 6
    result = ""
    if_win = 0
    if_finished = False
    if letter_or_word(user_input):
        result, guesses, covered =\
            process_letter(user_input, word, covered, guesses)
        if len(guesses) == MAXIUM_TASK:
            result = ("You lose! The word was " + word)
            if_finished = True
    else:
        result, if_win, if_finished =\
            check_word(word, user_input, covered, guesses)
    return result, if_finished, guesses, if_win, covered


def main():
    SECRET_WORDS = ["APPLE", "OBVIOUS", "XYLOPHONE"]
    win_num = 0
    for word in SECRET_WORDS:
        print(cover_word(word))
        if_finished = False
        guesses = ""
        covered = cover_word(word)
        while not if_finished:
            user_input = input("Enter a letter or word: ").upper()
            result, if_finished, guesses, if_win, covered =\
                process_input(user_input, word, covered, guesses)
            win_num += if_win
            print(result)
    print("You won {} out of {}".format(win_num, len(SECRET_WORDS)))


if __name__ == "__main__":
    main()
