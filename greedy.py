capacity = 10
data = [[4, 2, 1], [4, 2, 2], [7, 8, 3]]  # [value, weight, id]
ratios = []
container = []
count = 0

for i in range(len(data)):
    ratio = data[i][0] / data[i][1]
    ratios.append([ratio, data[i][2]])

print(data)
print(ratios)
decreasing = sorted(ratios, key=lambda x: x[0])
print(decreasing)

for i in range(len(decreasing)):
    print(decreasing[i][1])
    for j in range(len(data)):
        if (decreasing[i][1] == data[j][2]):
            count = count + data[j][1]
            if (count <= capacity):
                container.append(data[j])

print("    ", container)
