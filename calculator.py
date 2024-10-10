def get_operator() -> str:
  while True:
    operator: str = input('Enter the operator: ')
    if operator in ['*', '+', '-', '/', '**']:
      return operator
    print('Invalid operator')

def get_float(input_msg) -> float:
  while True:
    try:
      return float(input(input_msg))
    except ValueError:
      print('Invalid number')

def get_option() -> str:
  while True:
    option: str = input('[q]uit, [n]ew, [c]ontinue: ')
    if option in ['q', 'n', 'c']:
      return option
    print('Invalid option')

number: float = get_float('Enter the number: ')

while True:
  print(f'Number is {number:.2f}')
  operator: str = get_operator()
  operand: float = get_float('Enter the operand: ')
  
  if operator == '*':
    number *= operand
  elif operator == '+':
    number += operand
  elif operator == '-':
    number -= operand
  elif operator == '/':
    number /= operand
  elif operator == '**':
    number **= operand

  print(f'Result is {number:.2f}')

  option: str = get_option()

  if option == 'q':
    break
  elif option == 'n':
    number = get_float('Enter the number: ')
  elif option == 'c':
    continue

print('Goodbye!')
    