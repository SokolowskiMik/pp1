arr = [5,1,9,6,1]

def diff(array):
    minim = min(array)
    maxim = max(array)
    differ = maxim - minim
    return differ

print(f'Array: {arr}')
print(f'Result: {diff(arr)}')