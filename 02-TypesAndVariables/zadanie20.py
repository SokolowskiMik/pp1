import random

print('result of 3 dice rolls: ', '\n')

roll1 = random.randrange(6) + 1
print(roll1)
roll2 = random.randrange(6) + 1
print(roll2)
roll3 = random.randrange(6) + 1
print(roll3)

x = roll1 + roll2 + roll3

print('sum of those 3 dice rolls =', x)