from palindrome import unify_format, reverse, is_palindrome


def test_unify_format():
    assert(unify_format("SRA dowr") == "sradowr")
    assert(unify_format("CompuTER SCIENCe") == "computerscience")
    assert(unify_format("!Harry POTT!ER") == "!harrypott!er")


def test_reverse():
    assert(reverse("word") == "drow")
    assert(reverse("have a great day") == "yadtaergaevah")
    assert(reverse("RADar") == "radar")


def test_is_palindrome():
    assert(is_palindrome("RADAR"))
    assert(not is_palindrome("a"))
    assert(is_palindrome("madam Im adam"))
