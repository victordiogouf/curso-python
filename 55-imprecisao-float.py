from decimal import Decimal

n1: float = 0.1
n2: float = 0.7
n3: float = n1 + n2

print(n3)  # 0.7999999999999999
print(f'{n3:.2f}')  # 0.80
print(round(n3, 2)) # 0.8

n4: Decimal = Decimal('0.1')
n5: Decimal = Decimal('0.7')
n6: Decimal = n4 + n5

print(n6)  # 0.8