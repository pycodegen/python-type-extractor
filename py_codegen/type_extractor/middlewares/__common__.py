def get_typ_origin(typ):
    return getattr(typ, '__origin__', getattr(typ, '__class__', None))


def get_typ_args(typ):
    return getattr(typ, '__args__', getattr(typ, '__values__', None))
