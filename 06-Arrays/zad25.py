def occurs(number,array):
    val = None
    for num in array:
        if number == num:
            val = True
            return True
            break
        else:
            continue
    if val == None:
        return False

def occurs2(numb, arra):
    if numb in arra:
        return True
    else:
        return False

input_num = int(input('enter a number from your keyboard to check: '))
arr = [15,38,7,23,14]

print(occurs(input_num,arr))
print(occurs2(input_num, arr))