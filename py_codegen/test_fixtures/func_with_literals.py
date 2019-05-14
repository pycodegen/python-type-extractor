from typing_extensions import Literal


def func_with_literals(
        input1: Literal[
            'a',
            1,
            Literal[2,3],
        ],
) -> Literal[True, 0.5, Literal[3]]:
    return input1
