class ClassWithMethod:
    def some_method(self, arg: int) -> int:
        return id(self) + arg
