# from itertools import count
from math import ceil, sqrt

users_prime = int(input("How many primes do you want to find? "))
primes = [2]

def check_prime(candidate):
    mx = ceil(sqrt(candidate))  # need only check up to mx
    for prime in primes:
        if candidate % prime == 0:
            return False
        if prime >= mx:
            return True

# for candidate in count(start=3, step=2):
candidate = 1
while True:
    candidate += 2  # checking 3, 5, 7, 9, ... only
    if check_prime(candidate):
        primes.append(candidate)
    if len(primes) >= users_prime:
        break

print("The prime numbers are:", primes)