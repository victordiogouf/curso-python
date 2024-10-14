from typing import LiteralString

phrase: str = 'Hello, World!'
tokens: list[LiteralString] = phrase.split(',')

for index, token in enumerate(tokens):
  print(f'{index}: {token.strip()}')

print(','.join(tokens))