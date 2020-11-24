from typing import Union


class ClassWithUnionField:
    # TODO: nested unions not supported yet
    cwufField1: Union[str, int]
