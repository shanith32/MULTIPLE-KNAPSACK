import random
#Genetic algorithm to deal with the Knapsack problem

data = [[4, 2, 0], [5, 2, 1], [7, 11, 2],
        [7, 11, 3]]  # object set with the properties - [value, weight, id]

container = []  #the container to contain the objects in
capacity = 10  #weight capacity of the container

POP_SIZE = 5  #population size
# CHROMO = [] * 2  #structure of a chromosome with the soultion and the fitness(the total value of the selected objects)

# Initial Population
POPULATION = []  #The inital population array
count = 0
while (count != POP_SIZE):
    CHROMO = [] * 3  # [[binary soultion], fitness, total weight]
    solution = []
    for i in range(len(data)):
        select = random.randint(0, 1)
        solution.append(select)
    print(solution)
    fitness = 0
    totalWeight = 0
    for k in range(len(solution)):
        if (solution[k] == 1):
            fitness += data[k][0]
            totalWeight += data[k][1]
    print(fitness)
    CHROMO.append(solution)
    CHROMO.append(fitness)
    CHROMO.append(totalWeight)
    if (CHROMO[2] <= capacity):
        POPULATION.append(CHROMO)
        count += 1

print(POPULATION)
