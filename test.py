from main import pythagoras, make_first_big


def test_pythagoras():
    a = 3
    b = 4
    expected_result = 5

    result = pythagoras(a, b)

    assert result == expected_result


def test_make_first_big():
    assert make_first_big('hello') == 'Hello'
    assert make_first_big('') == ''
    assert make_first_big('x') == 'X'
    assert make_first_big('XyZ') == 'XYz'


if __name__ == "__main__":
    test_pythagoras()
    test_make_first_big()

    print("Everything passed")
