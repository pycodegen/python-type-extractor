from typing import Tuple


def func_with_tuple(input: Tuple[str, int]) -> Tuple[int, str]:
    return (input[1], input[0])
