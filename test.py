import numpy as np
from main import pythagoras


def test_pythagoras():
        a = 3
        b = 4
        expected_result = 5
        
        result = pythagoras(a, b)
        
        self.assertEqual(result, expected_result)