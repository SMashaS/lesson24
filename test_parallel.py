from time import sleep


def test_int():
    digit_one = 6
    sleep(3)
    assert isinstance(digit_one, int)


def test_string():
    first_string = 'Hello from New York!'
    sleep(3)
    assert isinstance(first_string, str)


def test_bool():
    bool_value = False
    sleep(3)
    assert isinstance(bool_value, bool)
