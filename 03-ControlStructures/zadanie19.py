age = int(input("Enter the dog's age in human years: "))

if age > 2:
    x = age - 2
    dage = 2 * 10.5 + x * 4
else:
    dage = age * 10.5

print(f"The dog's age in dog’s years is {dage} years.")