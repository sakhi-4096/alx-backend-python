#!/usr/bin/env python3

"""
Duck typing example: Safely retrieve the first element of a sequence.
"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of a sequence.

    Parameters:
        sequence (Sequence[Any]): A sequence-like object.
    Returns:
        Union[Any, None]: The first element of the sequence if it exists; otherwise, None.
    """
    if lst:
        return lst[0]
    else:
        return None
