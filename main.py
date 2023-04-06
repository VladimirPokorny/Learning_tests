import numpy as np


def pythagoras(a: float, b: float) -> float:
    c = np.sqrt(a**2 + b**2)
    return c


def vytvor_seznam_zvirat() -> list:
    return ['pes', 'kočka', 'králík', 'had']


def make_first_big(string: str) -> str:
    if len(string) == 0:
        output = ''
    else:
        output = string[0].upper() + string[1:]

    return output
