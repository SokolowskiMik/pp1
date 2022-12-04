fhand = open('loremipsum.txt', 'r', encoding='UTF-8')

val = True
while val:
    x = input('Press ENTER to continue')
    if x == 'done':
        print('done')
        break
    else:
        i = 0
        for line in fhand:
            line = line.rstrip()
            if i < 5:
                print(line)
                i += 1
            else:
                break
        
    