number_str: str = input('Enter a number: ')

try:
  number: float = float(number_str)
  print('You\'ve entered a number')
except:
  print('You\'ve not entered a number')

