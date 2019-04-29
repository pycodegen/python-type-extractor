from typing import Mapping


def func_with_mapping(input: Mapping[str, int]) -> Mapping[int, str]:
    print(input)
    return {
        1: 'a',
    }
