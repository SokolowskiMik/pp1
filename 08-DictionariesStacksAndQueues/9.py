phone = {
    "marka": "samsung",
    "model": "s2ipol",
    "rok": 2023,
    "price": "2000zł",
    "size": [155,85,25],
    "color": "black"
}

for i in phone:
    print(i, phone[i])

print()
print(phone.items())
print()

for key,value in phone.items():
    print(key,":",value)