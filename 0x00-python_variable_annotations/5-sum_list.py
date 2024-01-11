#!/usr/bin/env python3

""" Complex Types Example: List of floats and sum calculation """

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of a list of floats.

    Parameters:
        input_list (List[float]): The list of floats to be summed.
    Returns:
        float: The sum of the input list elements.
    """
    return sum(input_list)
