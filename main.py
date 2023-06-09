import numpy as np


def pythagoras(a: float, b: float) -> float:
    c = np.sqrt(a**2 + b**2)
    return c


def vytvor_seznam_zvirat() -> list:
    return ['pes', 'kočka', 'králík', 'had']


def crop_first_last(input_str: str) -> str:
    """Method which crop first and last letter from a given string.

    Args:
        string (str): input string such as word or sentence.

    Returns:
        str: return input string without first and last letter. 
    """

    if len(input_str) < 2:
        output = ''
    else:
        output = input_str[1:-1]

    return output


def make_first_big(input_str: str) -> str:
    """Method which makes first letter big

    Args:
        string (str): input string

    Returns:
        str: return string with big first letter
    """
    if len(input_str) == 0:
        output = ''
    else:
        output = input_str[0].upper() + input_str[1:]

    return output
