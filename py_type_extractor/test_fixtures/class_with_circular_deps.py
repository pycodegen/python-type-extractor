from typing import Optional


class ClassA:
    b: 'ClassB'


class ClassB:
    a: Optional[ClassA]

