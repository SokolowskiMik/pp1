def f(password):
    if len(password) < 6:
        return False
    i = 0
    for letter in password:
        i += 1
        for num in range(i, (len(password))):
            if letter == password[num]:
                return False
    return True

print(f("ax15"))
print(f('mysmartphone'))
print(f("water5"))
print(f("1234567"))