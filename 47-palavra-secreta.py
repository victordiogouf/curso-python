secret: str = 'welcome'
hint: str = '*' * len(secret)
tries: int = 0
max_tries: int = len(secret) * 2

print('Welcome! Guess the secret word by typing one letter at a time')
print(f'The secret word has {len(secret)} letters')
print(f'You have {max_tries} tries')

while True:
  tries += 1

  guess: str = input(f'#{tries} Guess one letter: ').lower()

  if len(guess) != 1:
    continue

  if guess in secret:
    print('Correct!')
    for index, letter in enumerate(secret):
      if letter == guess:
        hint = hint[:index] + guess + hint[index + 1:]
  else:
    print('Wrong!')

  print(hint)

  if hint == secret:
    print('You win!')
    print(f'You took {tries} tries')
    break

  if tries == max_tries:
    print('You lose!')
    break

print('Game over!')
  

  