from typing import Union


class SomeClass:
    pass

class ClassWithUnionField:
    cwufField1: Union[SomeClass, Union[int, None]]
