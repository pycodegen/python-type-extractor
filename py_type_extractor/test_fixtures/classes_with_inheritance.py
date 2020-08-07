class ParentClassA:
    from_parent_a: int


class ParentClassB:
    from_parent_b: str


class ChildClass(ParentClassA, ParentClassB):
    b: str
