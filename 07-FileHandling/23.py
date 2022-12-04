
import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

temperature = re.findall("\d{2}", message)

suma = 0
for temp in temperature:
    suma += int(temp)
avg = suma / len(temperature)

print(temperature)
print(avg)