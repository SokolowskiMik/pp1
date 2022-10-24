def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print(power(5, 3))

def power_v2(a, b):
    return a**b

print(power_v2(5, 3))