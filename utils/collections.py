from typing import List, TypeVar

T = TypeVar("T")


def flatten(enum: List[List[T]]) -> List[T]:
    return [item for sublist in enum for item in sublist]
