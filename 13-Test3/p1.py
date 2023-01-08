def f(n):
    lst = []
    if n > 0:
        whole = n//5
        rest = n - (whole*5)
        for i in range(whole):
            lst.append('/'*5)
        if rest > 0:
            lst.append('/'*rest)
        return '-'.join(lst)
    else:
        return ''

print(f(-4))
print(f(0))
print(f(5))
print(f(7))
print(f(10))
print(f(11))