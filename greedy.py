a = [[4, 2], [5, 6], [7, 8]]
ratios = []

for i in range(len(a)):
    ratio = a[i][0] / a[i][1]
    ratios.append(ratio)

print(ratios)
decresing = sorted(ratios)
print(decresing)
