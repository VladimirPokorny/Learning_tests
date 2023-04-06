from main import pythagoras, make_first_big
import numpy as np


def test_pythagoras():
    testing_values = [
        (3.0, 4.0, 5.0),
        (5.0, 12.0, 13.0),
        (7.0, 24.0, 25.0),
        (8.0, 15.0, 17.0),
        (9.0, 40.0, 41.0),
        (11.0, 60.0, 61.0),
        (12.0, 35.0, 37.0),
        (13.0, 84.0, 85.0),
        (16.0, 63.0, 65.0),
        (20.0, 21.0, 29.0),
        (-3.0, -4.0, np.sqrt(3**2 + 4**2)),
        (-5.0, 12.0, 13.0),
        (7.0, -24.0, 25.0),
        (-8.0, -15.0, np.sqrt(8**2 + 15**2)),
        (-9.0, -40.0, 41.0),
        (11.0, 60.0, 61.0),
        (-12.0, 35.0, 37.0),
        (-13.0, -84.0, 85.0),
        (16.0, -63.0, 65.0),
        (20.0, -21.0, 29.0),
    ]

    for input in testing_values:
        a, b, c = input
        assert pythagoras(a, b) == c


def test_make_first_big():
    assert make_first_big('hello') == 'Hello'
    assert make_first_big('') == ''
    assert make_first_big('x') == 'X'
    assert make_first_big('XyZ') == 'XyZ'
    assert make_first_big('XyZ') != 'XYZ'


if __name__ == "__main__":
    test_pythagoras()
    test_make_first_big()

    print("Everything passed")
