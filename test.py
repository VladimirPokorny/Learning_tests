import numpy as np
from main import pythagoras

def test_pythagoras():
    # Test a few cases
    assert np.isclose(pythagoras(3, 4), 5)
    assert np.isclose(pythagoras(5, 12), 13)
    assert np.isclose(pythagoras(7, 24), 25)

    # Test some edge cases
    assert np.isclose(pythagoras(0, 0), 0)
    assert np.isclose(pythagoras(1, 0), 1)
    assert np.isclose(pythagoras(0, 1), 1)

    # Test negative inputs
    assert np.isnan(pythagoras(-3, 4))
    assert np.isnan(pythagoras(3, -4))
    assert np.isnan(pythagoras(-3, -4))