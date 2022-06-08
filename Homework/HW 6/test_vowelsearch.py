from vowelsearch import check_vowels, contains_vowel


def test_check_vowels():
    assert(check_vowels("garage"))
    assert(not check_vowels(""))
    assert(not check_vowels("TV"))


def test_contains_vowel():
    assert(contains_vowel(["garage", "this", "man"]))
    assert(not contains_vowel(["fine", "TV", "Happy"]))
    assert(not contains_vowel([]))
