import random
class T():

    def measure(self):
        temp = random.randrange(340,421)/10
        if temp >= 37:
            if temp >= 41:
                print(f'Temperature: {temp}C (fever) CRITICAL TEMPERATURE!!')
            else:
                print(f'Temperature: {temp}C (fever)')  
        else: print(f'Temperature: {temp}C')

t1 = T()
t1.measure()
print()
t1.measure()
print()
t1.measure()
print()
t1.measure()
print()
t1.measure()
print()
t1.measure()
