# Example 1: Checking if a variable is None
a = None
if a is None:
  print("a is None")

# Example 2: Checking if a variable is not None
b = 5
if b is not None:
  print("b is not None")

# Example 3: Using is with other objects
c = []
d = c
if c is d:
  print("c and d are the same object")

# Example 4: Using is with different objects
e = []
f = []
if e is not f:
  print("e and f are different objects")

# Example 5: Function returning None
def do_nothing():
  return None

result = do_nothing()
if result is None:
  print("The function returned None")