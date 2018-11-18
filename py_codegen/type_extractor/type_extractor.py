import builtins
import inspect
from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, Dict, Union

from .ClassFound import ClassFound
from .DuplicateNameFound import DuplicateNameFound
from .FunctionFound import FunctionFound
from .TypeOR import TypeOR

def is_builtin(something):
    return inspect.getmodule(something) is builtins

class TypeExtractor:
    functions: Dict[str, FunctionFound]
    classes: Dict[str, ClassFound]

    def __init__(self):
        self.functions = dict()
        self.classes = dict()

    def add_function(self, options):
        def add_function_decoration(func: Callable):
            signature = inspect.getfullargspec(func)
            self.__process_params(signature.annotations)
            function_found = self.__to_function_found(func)
            if function_found.name in self.functions:
                raise DuplicateNameFound(
                    self.functions.get(
                        function_found.name
                    ),
                    function_found
                )
            self.functions[function_found.name] = function_found
            return func
        return add_function_decoration

    def __process_params(self, params: OrderedDict):
        processed_params = {
            key: self.__process_param(value)
            for key, value in params.items()
        }
        return processed_params

    def __process_param(self, value):

        if is_builtin(value):
            return value

        elif inspect.isfunction(value):
            function_found = self.__to_function_found(value)
            return function_found

        elif inspect.isclass(value):
            class_found = self.__to_class_found(value)
            self.__add_class_found(class_found)
            return class_found

        try:
            if value.__origin__ is Union:
                return self.__process_union(value)
        except:
            # FIXME: think what to do here...
            pass

    def __process_union(self, union):
        assert(union.__origin__ is Union)
        types = union.__args__
        type_a = self.__process_param(types[0])
        type_b = self.__process_param(types[1])
        return TypeOR(
            a = type_a,
            b = type_b,
        )

    def __to_class_found(self, _class):
        _data_class = dataclass(_class)
        argspec = inspect.getfullargspec(_data_class)
        module = inspect.getmodule(_class)
        filename = module.__file__
        fields = self.__process_params(argspec.annotations)
        class_found = ClassFound(
            name=_class.__name__,
            filePath=filename,
            raw_fields=argspec.annotations,
            fields=fields,
            doc=_class.__doc__
        )
        return class_found

    def __to_function_found(self, func: Callable) -> FunctionFound:
        argspec = inspect.getfullargspec(func)
        signature = inspect.signature(func)
        module = inspect.getmodule(func)
        filename = module.__file__
        params = self.__process_params(argspec.annotations)
        return_type = self.__process_param(signature.return_annotation)
        func_found = FunctionFound(
            name=func.__name__,
            filePath=filename,
            raw_params=argspec.annotations,
            params=params,
            doc=func.__doc__,
            func=func,
            return_type=return_type,
        )
        return func_found

    def __add_class_found(self, class_found: ClassFound):
        if class_found.name == 'ParentClass':
            print("!!!")
        self.classes[class_found.name] = class_found

    def add_class(self, options):
        def add_class_decoration(_class):
            if is_builtin(_class):
                return
            class_found = self.__to_class_found(_class)
            self.__add_class_found(class_found)
        return add_class_decoration
