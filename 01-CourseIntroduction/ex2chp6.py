
def count(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)

input_word = input('Enter a word: ')
input_letter = input('Enter a letter: ')
count(input_word.lower(), input_letter.lower())