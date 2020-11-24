from typing import (
    Generator,
)


def some_func_with_generator(
        tag: str,
        count: int,
) -> Generator[float, int, str]:
    while count > 0:
        print('T-minus {} ({})'.format(count, tag))
        # yield from asyncio.sleep(0.1)
        a = yield count
        count -= a
    return "Blastoff!"
