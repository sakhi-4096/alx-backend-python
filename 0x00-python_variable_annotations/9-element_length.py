#!/usr/bin/env python3

""" Duck Typing Example: Calculating the length of elements in an iterable object """

from typing import Iterable, Sequence, List, Tuple


def element_length(iterable: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in an iterable object.

    Parameters:
        iterable (Iterable[Sequence]): The iterable object containing sequences.
    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains an element from
        the iterable and its length.
    """
    return [(item, len(item)) for item in iterable]
