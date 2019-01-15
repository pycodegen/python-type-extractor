from mypy_extensions import TypedDict



SimpleTypedDict1 = TypedDict('SimpleTypedDict1', {
    'a': str,
})

NestedTypedDict = TypedDict('NestedTypedDict', {
    'child': SimpleTypedDict1,
})

class SomeClass:
    def __init__(self, a: int):
        self.a = a

OutputType = TypedDict('OutputType', {
    'b': int,
    's': SomeClass,
})


def func_with_typed_dict(input: NestedTypedDict) -> OutputType:
    return {
        'b': len(str(input['child']['a'])),
        's': SomeClass(123)
    }
