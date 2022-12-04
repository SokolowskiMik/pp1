import csv
with open('students.csv', 'r', encoding='UTF-8') as csf:
    info = csv.reader(csf)
    for row in info:
        if not row[0] == 'first_name':
            if int(row[2]) < 30:
                print(row[0], row[1], row[4], end='\n')
            else: continue
        else: continue