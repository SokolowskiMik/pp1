import random

def read_number():
    return int(input('Enter a number <1, 9>: '))

def generate_number():
    return(random.randrange(1, 10))