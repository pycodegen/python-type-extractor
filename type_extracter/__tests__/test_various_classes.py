from typing import NamedTuple, Dict
from type_extracter.type_extractor import CollectType
import dataclasses

def test_func_with_arg_class():
    typeCollector = CollectType()
    class ArgClass:
        arg1: str
        arg2: int

    @typeCollector.add_function(None)
    def func_with_arg_class(a: ArgClass) -> ArgClass:
        return a
    import pdb;pdb.set_trace()
    print('typeCollector.classes', typeCollector.classes)

# class ChildArgClass:
#     ca1: int

# class ParentArgClass:
#     pa1: str
#     pa2: ChildArgClass

# # @typeCollector.add_function(None)
# # def test_func_with_nested_arg_class(pac: ParentArgClass):
# #     return pac

# # @typeCollector.add_function(None)
# # def test(a: int, b: int) -> int:
# #     return a + b


# # @typeCollector.add_class(None)
# # @dataclasses.dataclass
# # class TestDataClass:
# #     permissions: Dict[str, bool]

# # @typeCollector.add_class(None)
# # class TestNormalClass:
# #     checklist: Dict[str, bool]

# print(typeCollector.classes)

# print("!!!")
# import pdb; pdb.set_trace()
# # map(lambda c: c ,typeCollector.classes)
# # print(test(1,2))