import random

print('I rolled a dice 1-6: ')
roll = random.randrange(6) + 1
guess = ""
guess_count = 0
guess_limit = 2
out_of_guesses = False

while roll != guess and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input('guess what number i got: '))
        guess_count += 1
        print('you have guessed', guess_count, 'times')
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You lose!")
else:
    print(True)
    print('You win!')