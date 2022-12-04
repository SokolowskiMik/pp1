fname = input('Enter file name: ')
try:
    with open(fname, 'r', encoding='UTF-8') as f:
        count = 0
        for line in f:
            line = line.rstrip()
            count += 1
        print('number of lines: ', count)
            
except:
    print('wrong file name', fname)
    exit()

