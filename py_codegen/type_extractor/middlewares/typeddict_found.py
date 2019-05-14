from mypy_extensions import _TypedDictMeta  # type: ignore

from py_codegen.type_extractor.__base__ import BaseTypeExtractor
from py_codegen.type_extractor.nodes.TypedDictFound import TypedDictFound


def typeddict_found_middleware(typ, type_extractor: BaseTypeExtractor):
    if not isinstance(typ, _TypedDictMeta):
        return
    annotations = {
        key: type_extractor.rawtype_to_node(value)
        for key, value in typ.__annotations__.items()
    }
    typed_dict_found = TypedDictFound(
        annotations=annotations,
        name=typ.__qualname__,
        raw=typ,
    )
    type_extractor.collected_types[
        f"{typ.__qualname__}_{hash(typ)}"
    ] = typed_dict_found

    return typed_dict_found