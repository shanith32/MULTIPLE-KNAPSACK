import json

data = {
    "set": [{
        "weight": 1,
        "value": 2
    }, {
        "weight": 3,
        "value": 4
    }, {
        "weight": 5,
        "value": 6
    }]
}

a = [[1, 2], [5, 6], [7, 8]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()