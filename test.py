# import numpy as np
from main import pythagoras


def test_pythagoras():
        a = 3
        b = 4
        expected_result = 5        
        
        result = pythagoras(a, b)

        assert result == expected_result
    

if __name__ == "__main__":
    test_pythagoras()
    print("Everything passed")
