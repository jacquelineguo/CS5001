from password import count_char, secure_password


def test_count_char():
    assert(count_char("HelloWord!1") == (1, 1, 7, 2, 0))
    assert(count_char("norte^a123") == (0, 3, 6, 0, 1))
    assert(count_char("eaS123@ED~~") == (1, 3, 2, 3, 2))


def test_secure_password():
    assert(secure_password("HelloWord!1"))
    assert(not secure_password("norte^a123"))
    assert(not secure_password("eaS123@"))
