# string interpolation
name: str = 'Victor'
price: float = 239.49
print('%s, the price is %.2f' % (name, price))

integer: int = 16 ** 2 + 16 + 15
print('hex(%i) = %04x' % (integer, integer))