arr = [1,2,3,4,5,6,7,8,9]
li = []

number = int(input("enter a number: "))

for num in arr:
    if number < num:
        li.append(num)
    else:
        pass

print(arr)
print(number)
print(li)
