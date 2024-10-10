list_a: list[int] = [10, 20, 30, 40]

del list_a[0] # caution: moving elements can be slow

list_a.append(60)

list_a.insert(4, 50)

last: int = list_a.pop()

list_a.clear()

list_a.append(1)
list_a.append(2)

list_a.extend([3, 4, 5])

list_b: list[int] = [6, 7, 8]
list_c: list[int] = list_a + list_b

print(list_c)

list_d: list[int] = list_a * 3

print(list_d)

list_e = list_a.copy()
list_e.pop()

print(list_e)
