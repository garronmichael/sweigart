import random

guess = ''
guesses = 2
toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = 'heads' if toss == 1 else 'tails'

print('Guess the coin toss! Enter heads or tails:')
while guess not in ('heads', 'tails') and guesses > 0:
    guess = input()

    if toss == guess:
        print('You got it!')
    elif guesses > 1:
        print('Nope! Guess again!')
        guess = ''
        guesses -= 1
        continue
    else:
        print('You ran out of guesses!')