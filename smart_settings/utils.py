import collections

def removesuffix(self: str, suffix: str, /) -> str:
    # suffix='' should not call self[:-0].
    if suffix and self.endswith(suffix):
        return self[:-len(suffix)]
    else:
        return self[:]

def map_nested_dicts(ob, func):
    if isinstance(ob, collections.Mapping):
        return {func(k): map_nested_dicts(v, func) for k, v in ob.items()}
    else:
        return ob
