#!/usr/bin/env python3

"""
Type Checking Example: Zooming into a Tuple with a specified factor.
"""

from typing import Tuple, List


def zoom_array(source_tuple: Tuple, factor: int = 2) -> List:
    """
    Zooms into a Tuple by repeating its elements based on a specified factor.

    Parameters:
        source_tuple (Tuple): The Tuple to zoom into.
        factor (int, optional): The factor by which each element should be repeated.
            Defaults to 2.
    Returns:
        List: A List containing the zoomed-in elements.
    """
    zoomed_in: List = [
        item for item in source_tuple
        for _ in range(factor)
    ]
    return zoomed_in


# Example usage:
array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)