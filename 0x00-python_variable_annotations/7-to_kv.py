#!/usr/bin/env python3

""" Complex Types Example: Converting a string and int/float to a tuple """

from typing import Union, Tuple


def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string `key` and an integer or float `value` to a tuple.

    Parameters:
        key (str): The string key.
        value (Union[int, float]): The numeric value (integer or float).
    Returns:
        Tuple[str, float]: A tuple containing the string key and the square of the numeric value.
    """
    return (key, value**2)
