#!/usr/bin/env python3
"""to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple with string and square of the number """
    return k, v**2
