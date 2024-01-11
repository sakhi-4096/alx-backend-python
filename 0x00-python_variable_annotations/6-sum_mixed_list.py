#!/usr/bin/env python3

""" Mixed List Example: List of integers and floats, and sum calculation """

from typing import Union, List


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list containing integers and floats.

    Parameters:
        mixed_list (List[Union[int, float]]): The list containing integers and floats to be summed.
    Returns:
        float: The sum of the elements in the mixed list.
    """
    return float(sum(mixed_list))
