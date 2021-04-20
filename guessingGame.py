import random
number = random.randint(1,9)
chances = 0
print('Number Guessing Game')
print('Guess a number between(1 to 9)')
while chances<5:
    guess = int(input('Enter your guess'))
    if guess == number:
        print('you win!')
        break
    elif guess<number:
        print('your guess is too low,guess a number higher than',guess)
    else:
        print('your guess is too high,guess a number lower than',guess)
    chances = chances+1

if not chances<5:
    print('you lose')
    print('the number is',number)
