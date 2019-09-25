from typing import Optional


def func_return_none(
        some_input: Optional[str],
        some_input2: Optional[bool],
) -> None:
    print(some_input)
    print(some_input2)
    return None
