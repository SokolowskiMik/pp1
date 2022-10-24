
def how_many(text, letter):
    counter = 0
    for i in text:
        if i == letter:
            counter = counter + 1
    return counter

input_letter = input('Enter a letter: ')
input_text = input('Enter text: ')

count = how_many(input_text.lower(), input_letter.lower())

print('your letter has occured: ', count, 'times in', input_text)