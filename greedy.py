#Heuristic algorithem to deal with the Knapsack problem

data = [[4, 2, 1], [5, 2, 2],
        [7, 11, 3]]  # object set with the properties - [value, weight, id]

container = []  #the container to contain the objects in
capacity = 10  #weight capacity of the container

ratios = []  #an array to store the ratios of each object
count = 0  #a count to track the weights of objects before adding them to the container

# For loop to get the ratios of value/weight and add the ratios of each object to the container
for i in range(len(data)):
    ratio = data[i][0] / data[i][1]
    ratios.append([ratio, data[i][2]])

print(data)
print(ratios)
# Sort the resulting ratios in decending order
decreasing = sorted(ratios, key=lambda x: x[0], reverse=True)
print(decreasing)

# For loop to add the objects to the container without exceeding the capacity of the container
for i in range(len(decreasing)):
    print(decreasing[i][1])
    for j in range(len(data)):
        if (decreasing[i][1] == data[j][2]):
            if (data[j][1] <= capacity):
                if (count + data[j][1] <= capacity):
                    count = count + data[j][1]
                    container.append(data[j])

print("Weights", count)
print(" Here's the resulting container: ", container)
