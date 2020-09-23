# baseNode: BaseNodeType --> ( BaseNodeWithoutOptions, options )
# Dict <
#   Hash(BaseNodeWithoutOptions) ,
#   options
# >
from typing import List, Set

from py_type_extractor.type_extractor.__tests__.test_class_with_union_field import SomeOption
from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.TypeOR import TypeOR


def dedupe_type(
        node_list: List[NodeType],
) -> Set[NodeType]:
    # Q. merging options?
    result = set()


dedupe_type([
    ClassFound(
        name='ClassWithUnionField',
        fields={
            'cwufField1': TypeOR(
                a=str, b=int
            )
        },
        options={SomeOption(some_var=1)},
    ),
    ClassFound(
        name='ClassWithUnionField',
        fields={
            'cwufField1': TypeOR(
                a=str, b=int
            )
        },
        options={},
    ),
])


def a(ab: int):
    print(ab)


a('aa')
