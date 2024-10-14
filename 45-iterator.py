# Iterável -> str, range, (__iter__)
# Iterator -> quem entrega um valor por vez
# next     -> me entregue o próximo valor
# iter     -> me entregue o iterador

iterator = iter('Iterable')

print(next(iterator) + next(iterator) + next(iterator) + next(iterator))

iterator = iter('Iterable')

while True:
  try:
    value = next(iterator)
    print(value)
  except StopIteration:
    break