a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(*a, sep=", ")  # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

b: list[list[str]] = [
  ["Maria", "João", "Pedro"],
  ["Ana", "José", "Carlos"],
  ["Marta", "Paulo", "Fernando"]
]

print(*b, sep="\n")