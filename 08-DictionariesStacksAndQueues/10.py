arr = [
    {"Country": "Poland", "Population": 37812000},
    {"Country": "Germany", "Population": 83000000},
    {"Country": "USA", "Population": 329000000},
    {"Country": "England", "Population": 67000000},
    {"Country": "Slovakia", "Population": 5400000}
]

i = 0
while i < len(arr):
    # print(arr[i])
    print(arr[i].items())
    i += 1

j = 0
while j < len(arr):
    for key,value in arr[j].items():
        print(value, end=": ")
    print()
    j += 1