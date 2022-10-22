pin = '0805'
i = 0
while i < 3:
    pin_typed = input('Enter the PIN code: ')
    if pin_typed == pin:
        print('Correct pin')
        break
    else:
        print('Incorrect...')
    i += 1
if i == 3:
    print('Sorry, your payment card has been blocked.')


