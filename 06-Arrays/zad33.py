li = [1,23,5,382,1,17,4,906]

print("-"*len(li)*4+"-")
for item in li:
    space = ' '*(3-(len(str(item))))
    print(f'|{space}{item}',end="")
print('|')
print("-"*len(li)*4+"-")


        