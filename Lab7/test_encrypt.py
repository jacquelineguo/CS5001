from encrypt import check_input, check_amount, convert_amount, encrypt,\
    dencrypt
from py.test import approx


def test_check_input():
    assert(check_input('a'))
    assert(not check_input('1'))
    assert(not check_input(' '))


def test_check_amount():
    assert(not check_amount(27))
    assert(check_amount(0))
    assert(not check_amount(99))


def test_conver_amount():
    assert(convert_amount(46) == 21)
    assert(convert_amount(25) == 25)
    assert(convert_amount(27) == 2)


def test_encrypt():
    assert(encrypt('pizza', 3) == 'slccd')
    approx(encrypt(
        'Beware the Ides of March', 10) == 'logkbo dro snoc yp wkbmr'
        )
    assert(encrypt('bird124', 6) == 'hoxj124')


def test_dencrypt():
    assert(dencrypt('slccd', 3) == 'pizza')
    assert(dencrypt(
        'logkbo dro snoc yp wkbmr', 10) == 'beware the ides of march'
        )
    assert(dencrypt('mfuud', 5) == 'happy')
