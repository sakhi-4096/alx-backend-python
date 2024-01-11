#!/usr/bin/env python3

""" Complex Types Example: Function that generates a multiplier function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Generates a multiplier function based on the specified float multiplier.

    Parameters:
        multiplier (float): The multiplier used to generate the multiplier function.
    Returns:
        Callable[[float], float]: A function that takes a float `n` as input and returns
        the result of multiplying `n` by the specified multiplier.
    """
    def f(n: float) -> float:
        """ Multiplies a float by the specified multiplier """
        return float(n * multiplier)

    return f
