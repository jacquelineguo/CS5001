from recipes import check_choices, separate_ing, check_ingredients,\
    clean_file_name, check_empty_name, is_empty_name
from pytest import raises


def test_check_choices():
    with raises(ValueError):
        check_choices("0", ["1", "2", "3"])
    with raises(ValueError):
        check_choices("one", ["1", "2", "3"])
    with raises(ValueError):
        check_choices("-1", ["1", "2", "3"])


def test_separate_ing():
    assert(separate_ing("tomato, water , eggs") == ["tomato", "water", "eggs"])
    assert(separate_ing("   eggs ") == ["eggs"])
    assert(separate_ing(" ") == [""])


def test_check_ingredients():
    assert(not check_ingredients(""))
    assert(check_ingredients("water,  , eggs"))
    assert(not check_ingredients(" , "))


def test_clean_file_name():
    assert(clean_file_name("Egg and Soldiers") == "egg_and_soldiers.txt")
    assert(clean_file_name(" FILE NOT FOUND") == "file_not_found.txt")
    assert(clean_file_name(" tomato s!oup") == "tomato_soup.txt")


def test_check_empty_name():
    assert(check_empty_name(".txt"))
    assert(not check_empty_name("tomato_soup.txt"))


def test_is_empty_name():
    with raises(FileNotFoundError):
        is_empty_name(".txt")
