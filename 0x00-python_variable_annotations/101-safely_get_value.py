#!/usr/bin/env python3
"""safely_get_value"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
        Return the value of the key in the mapping
        if it exists, otherwise return the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
