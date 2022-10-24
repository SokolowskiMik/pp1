def is_in_range(number, begin_range, end_range):
    if number >= begin_range and number <= end_range:
        return True
    else:
        return False

numer_input = int(input('Enter a number: '))
begin_input = int(input('Enter where to start: '))
end_input = int(input('Enter where to end: '))

print(is_in_range(numer_input, begin_input, end_input))