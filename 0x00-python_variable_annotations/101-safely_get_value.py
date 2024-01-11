#!/usr/bin/env python3

"""
More involved type annotations for safely retrieving values from a mapping.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(data_map: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """
    Safely retrieves a value from a mapping using a specified key.

    Parameters:
        data_map (Mapping): A mapping (e.g., dictionary) containing key-value pairs.
        key (Any): The key for which the value needs to be retrieved.
        default (Union[T, None], optional): The default value to return if the key 
        is not present. Defaults to None.
    Returns:
        Union[Any, T]: The value associated with the specified key if it exists;
        otherwise, the default value.
    """
    if key in data_map:
        return data_map[key]
    else:
        return default
