from typing_extensions import Literal


def func_with_literals(
        input1: Literal[
            'a',
            1,
            Literal[2, 3],
            Literal[True, 3],
        ],
        input2: Literal[
            1,
            None
        ]
) -> Literal[True, 5, Literal[3]]:
    print(input1)
    print(input2)
    return 5
