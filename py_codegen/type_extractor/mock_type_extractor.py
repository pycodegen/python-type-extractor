from py_codegen.type_extractor.__base__ import BaseTypeExtractor


class MockTypeExtractor(BaseTypeExtractor):
    def __init__(self):
        self.functions = dict()
        self.classes = dict()
        self.typed_dicts = dict()

    def add(self, options):
        def add_decoration(func):
            return func
        return add_decoration

