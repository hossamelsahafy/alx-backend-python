#!/usr/bin/env python3
"""zoom_array"""

from typing import List, Union, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
