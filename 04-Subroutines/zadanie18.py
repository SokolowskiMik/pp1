def sum_digits(digits):
    suma = 0
    for i in digits:
        suma = suma + int(i)
    return suma

digits_input = input('Enter number: ')

print('Sum of digits in your number is:', sum_digits(digits_input))
