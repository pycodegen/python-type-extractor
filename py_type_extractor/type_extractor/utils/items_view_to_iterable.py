from typing import Any, ItemsView, List, Tuple, TypeVar, cast


TKey = TypeVar('TKey')
TValue = TypeVar('TValue')

# PyCharm temporary hack...
def items_view_to_iterable(a: ItemsView[TKey, TValue]) -> List[Tuple[TKey, TValue]]:
    return cast(Any, a)