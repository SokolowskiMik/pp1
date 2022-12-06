import stack

number = int(input('Enter a number you want to convert to binary: '))
def convert(n):
    while n >= 1:
        if n % 2 == 0:
            stack.push(0)
        else:
            stack.push(1)
        n //= 2
    stack.display()


convert(number)
    
