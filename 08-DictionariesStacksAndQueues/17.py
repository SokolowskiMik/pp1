import json
with open('euro.json', 'r') as j:
    data = json.load(j)
nag = "Date            Buying Rate     Selling Rate"
print(nag)
print('='*len(nag))
for key in data:
    if key == 'rates':
        for i in range(len(data['rates'])):
            print(data['rates'][i]['effectiveDate'],end='      ')
            print(data['rates'][i]['bid'], end='          ')
            print(data['rates'][i]['ask'])