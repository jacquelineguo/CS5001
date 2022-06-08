from hangman import cover_word, letter_or_word, replace_covered,\
    process_letter, check_word, process_input


def test_cover_word():
    assert(cover_word("word") == "____")
    assert(cover_word("university") == "__________")
    assert(cover_word("OBVIOUS") == "_______")


def test_letter_or_word():
    assert(letter_or_word("x"))
    assert(not letter_or_word("word"))
    assert(letter_or_word(" "))


def test_replace_covered():
    assert(replace_covered("APPLE", "A", "_____") == "A____")
    assert(replace_covered("UNIVERSITY", "Z", "__________") == "__________")
    assert(replace_covered("corn", "r", "c___") == "c_r_")


def test_process_letter():
    assert(process_letter("P", "APPLE", "_PP__", "P") == (
        "You've already guessed that letter!" + "\n" + "_PP__" + "\n" +
        "Your guesses so far: P", "P", "_PP__"
        ))
    assert(process_letter("A", "APPLE", "_____", "") == (
        "A____" + "\n" + "Your guesses so far: A", "A", "A____"
        ))
    assert(process_letter("E", "APPLE", "_____", "") == (
        "____E" + "\n" + "Your guesses so far: E", "E", "____E"
        ))


def test_check_word():
    assert(check_word("APPLE", "APPLE", "_____", "A") == ("You win!", 1, True))
    assert(check_word("APPLE", "AE", "_____", "A") == (
        "_____" + "\n" + "Your guesses so far: " + "A", 0, False
        ))
    assert(check_word("WORD", "WORD", "____", "W") == ("You win!", 1, True))


def test_process_input():
    assert(process_input("D", "OBVIOUS", "OV__O__", "OV") == (
        "OV__O__" + "\n" + "Your guesses so far: " + "OVD",
        False, "OVD", 0, "OV__O__"
        ))
    assert(process_input("D", "OBVIOUS", "OV__O__", "OVDWAX") == (
        "You lose! The word was " + "OBVIOUS", True, "OVDWAX", 0, "OV__O__"
        ))
    assert(process_input("WORD", "WORD", "____", "") == (
        "You win!", True, "", 1, "____"
        ))
