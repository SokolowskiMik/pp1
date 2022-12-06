import stack
import re

userinp = input('Enter any number and a operator(+=*/): ')


userinp = re.sub(' ', '', userinp)
print(userinp)

for char in userinp:
    if char == '0' or char == '1' or char == '2' or char == '3' or char == '4' or char == '5' or char == '6' or char == '7' or char == '8' or char == '9' :
        stack.push(int(char))
    elif char == '+':
        calculation = stack.pop() + stack.pop()
        stack.push(calculation)
    elif char == '-':
        calculation = stack.pop() - stack.pop()
        stack.push(calculation)
    elif char == '*':
        calculation = stack.pop() * stack.pop()
        stack.push(calculation)
    elif char == '/':
        calculation = stack.pop() / stack.pop()
        stack.push(calculation)
    elif char == '=':
        result = stack.pop()
        print(result)
    else: continue

