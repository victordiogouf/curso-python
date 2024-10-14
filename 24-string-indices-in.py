# Index:  0  1  2  3  4  5
# String: V  i  c  t  o  r
# Index: -6 -5 -4 -3 -2 -1

name: str = 'Victor'
print(name[0]) # V
print(name[-1]) # r

if 'i' in name:
  print(f'"{name}" has "i"')

if 'ra' not in name:
  print(f'"{name}" has\'nt "ra"')