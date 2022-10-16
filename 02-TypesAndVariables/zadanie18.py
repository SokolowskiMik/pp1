import math

a = float(input("first side length a=: "))
b = float(input("second side length b=: "))
c = float(input("third side length c=: "))

s = float((a + b + c) / 2)

z = float(s*(s-a)*(s-b)*(s-c))
area = math.sqrt(z)

print(area)
