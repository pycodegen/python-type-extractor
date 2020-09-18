from typing import Optional, Union, List, Set, Dict

from py_type_extractor.type_extractor.nodes.BaseNodeType import NodeType
from py_type_extractor.type_extractor.nodes.ClassFound import ClassFound
from py_type_extractor.type_extractor.nodes.FixedGenericFound import FixedGenericFound
from py_type_extractor.type_extractor.nodes.TypeVarFound import TypeVarFound


def flatten_generics_inheritance_to(
        from_typ: ClassFound,
        to_typ: ClassFound,
        given_types: List[NodeType] = [],
) -> List[FixedGenericFound]:

    if from_typ == to_typ:
        return [
            FixedGenericFound(
                type_vars=given_types,
                origin=from_typ,
            ),
        ]
    # given_types --> from_typ.type_vars
    typevar_overrides: Dict[TypeVarFound, NodeType] = {}
    for nth, type_var in enumerate(from_typ.type_vars):
        # python doesn't have list.get(nth, fallback)  -_-
        try:
            typevar_overrides[type_var] = given_types[nth]
        except IndexError:
            typevar_overrides[type_var] = type_var

    results: List[FixedGenericFound] = []
    for parent_cls in from_typ.base_classes:
        if isinstance(parent_cls, FixedGenericFound) \
                and isinstance(parent_cls.origin, ClassFound):
            override_types = [
                typevar_overrides[type_var] if isinstance(type_var, TypeVarFound)
                else type_var
                for type_var in parent_cls.type_vars
            ]
            results = results + flatten_generics_inheritance_to(
                from_typ=parent_cls.origin,
                to_typ=to_typ,
                given_types=override_types,
            )
    return results

