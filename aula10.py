concatenacao = 'Hello' + ' ' + 'world!'
print(concatenacao)

print('<->' * 10)

# Type hints

name: str = 'Riemman'
age: int = 30 

def welcome(name: str) -> str:
  return f'Hello {name}'

list_a: list[int] = [1, 2, 3]
tuple_a: tuple[int, int, int] = (1, 2, 3)
set_a: set[int] = {1, 2, 3}
dict_a: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}