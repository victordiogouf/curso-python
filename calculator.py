number: float = float(input('Enter a number: '))
while True:
  print(f'Number is {number:.4f}')
  operator: str = input('Enter the operator: ')
  operand: float = float(input('Enter the operand: '))
  
  if operator == '*':
    number *= operand
  elif operator == '+':
    number += operand

  print(f'Result is {number:.4f}')

  option: str = input('[q]uit, [n]ew, [c]ontinue: ')

  if option == 'q':
    break
  elif option == 'n':
    number = float(input('Enter the new number: '))
    