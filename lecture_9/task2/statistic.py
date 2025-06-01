from typing import List


def mean(numbers: List[int]) -> float:
    sum: int = 0
    for i in numbers:
        sum += i
    mean: float = sum / len(numbers)
    return mean