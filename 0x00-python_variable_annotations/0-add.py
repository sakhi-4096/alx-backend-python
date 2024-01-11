#!/usr/bin/env python3

'''Simple module showcasing basic variable annotations.'''


def calculate_sum(a: float, b: float) -> float:
    '''
    Calculates the sum of two floating-point numbers.

    Parameters:
        first_number (float): The first number to be added.
        second_number (float): The second number to be added.
    Returns:
        float: The sum of the two input numbers.
    '''
    return a + b
