#!/usr/bin/env python3
"""element_length"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with sequence and its length"""
    return [(i, len(i)) for i in lst]
