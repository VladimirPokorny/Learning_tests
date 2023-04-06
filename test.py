from main import pythagoras, make_first_big, crop_first_last, make_first_big
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


def test_crop_first_last():
    test_values = [
        ('', ''),
        ('Ahoj', 'ho'),
        ('Tohle je dlouhá věta', 'ohle je dlouhá vět'),
        ('éíáýžřčšě+', 'íáýžřčšě'),
        ('...', '.'),
        ('a', ''),
        ('fr', '')
    ]

    for input_str, output_str in test_values:
        assert crop_first_last(input_str) == output_str


def test_make_first_big():
    test_values = [
        ('test', 'Test'),
        ('čeněk', 'Čeněk'),
        ('24. prosince', '24. prosince'),
        ('', ''),
        ('1', '1'),
        ('@', '@')
    ]

    for input_str, output_str in test_values:
        assert make_first_big(input_str) == output_str


if __name__ == "__main__":
    test_pythagoras()
    test_make_first_big()
    test_crop_first_last()
    test_make_first_big()

    print("Everything passed")
