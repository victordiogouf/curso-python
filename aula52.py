# Tuple is an immutable list

names: tuple[str, str, str] = ('Ana', 'Beatriz', 'Carlos') # with or without parentheses

list_names: list[str] = list(names)

tuple_names: tuple[str, ...] = tuple(list_names)
