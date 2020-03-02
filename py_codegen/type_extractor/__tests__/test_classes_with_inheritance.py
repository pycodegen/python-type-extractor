from py_codegen.test_fixtures.classes_with_inheritance import ChildClass

from py_codegen.type_extractor.nodes.BaseNodeType import BaseOption
from py_codegen.type_extractor.nodes.ClassFound import ClassFound
from py_codegen.type_extractor.nodes.TypeOR import TypeOR
from py_codegen.type_extractor.__tests__.utils import traverse, cleanup
from py_codegen.type_extractor.type_extractor import TypeExtractor


def test_classes_with_inheritance():
    type_collector = TypeExtractor()

    type_collector.add(None)(ChildClass)

    print(type_collector)