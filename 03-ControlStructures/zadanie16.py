num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1 > num2:
    print(num2, num1)
elif num1 == num2:
    print(num1, '=', num2)
else:
    print(num1, num2)