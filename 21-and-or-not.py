a: bool = True
b: bool = False
c: bool = True

if (a and b) or (a and c):
  print('(a and b) or (a and c)')

# type None
def welcome(name: str) -> None:
  print(f'Welcome, {name}')

if True and False and True:
  print('Stopped at first False')

# [0, 0.0, '']
if bool('') or bool(0) or bool(0.0):
  print('Not executed')

print(False or 0 or 'abc') # prints 'abc'

password: str = input('Password: ') or 'Empty'
if password == 'Empty':
  print('Empty password')

name: str = input('Name: ')
if not name:
  print(f'{name=} is not valid')