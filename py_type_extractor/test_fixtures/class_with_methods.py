class SomeArgClass:
    a: int


class ClassWithMethod:
    def some_method(self, arg: SomeArgClass) -> int:
        return id(self) + arg.a
