import stack
import re

userinp = input('Enter any number and a operator(+=*/): ')


userinp = re.sub(r'\s', '', userinp)
print(userinp)

for char in userinp:
    if re.match(r'[0-9]', char):
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

