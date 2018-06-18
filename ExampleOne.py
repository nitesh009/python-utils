# This is a guess the number game.

import random

print("Hello. what is your name?")
name = input()

print('Well, ' + str(name) + ', I am thinking of a number between')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low..')
    elif guess > secretNumber:
        print('your guess is too high..')
    else:
        break;  # this condition is correct guess

if guess == secretNumber:
    print('Good Job' + name + '! your guessed my number in ' + str(guessesTaken) + 'guesses.')
else:
    print('Nope, the number i was thinking of' + str(secretNumber))


print('you took ' + str(guessesTaken) + ' guesses.')