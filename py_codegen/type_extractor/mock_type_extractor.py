class MockTypeExtractor:
    def __init__(self):
        self.functions = dict()
        self.classes = dict()
        self.typed_dicts = dict()

    def add_function(self, options):
        def add_function_decoration(func):
            return func
        return add_function_decoration

    def add_class(self, options):
        def add_class_decoration(_class):
            return _class
        return add_class_decoration
