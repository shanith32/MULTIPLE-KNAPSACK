import random
#Genetic algorithm to deal with the Knapsack problem

data = [[4, 2, 0], [5, 2, 1], [7, 11, 2],
        [7, 11, 3]]  # object set with the properties - [value, weight, id]

container = []  #the container to contain the objects in
capacity = 10  #weight capacity of the container

POP_SIZE = 5  #population size
GEN_AMOUNT = 3  #how many generations to run

# Initial Population
POPULATION_ONE = []  #The inital population array
initCount = 0
while (initCount != POP_SIZE):
    CHROMO = [] * 3  # [[binary soultion], fitness, total weight]
    solution = []
    for i in range(len(data)):
        select = random.randint(0, 1)
        solution.append(select)
    # print(solution)
    fitness = 0
    totalWeight = 0
    for k in range(len(solution)):
        if (solution[k] == 1):
            fitness += data[k][0]
            totalWeight += data[k][1]
    # print(fitness)
    CHROMO.append(solution)
    CHROMO.append(fitness)
    CHROMO.append(totalWeight)
    if (CHROMO[2] <= capacity):
        POPULATION_ONE.append(CHROMO)
        initCount += 1

print(POPULATION_ONE)
print("------------------------------------------------------------")

# Generation GA loop
genCount = 0
while (genCount != GEN_AMOUNT):
    print("gen :", genCount)
    POPULATION_TWO = []  #Second population array
    for i in range(1):
        # Find Parent Chromosome
        sortedPop = sorted(POPULATION_ONE, key=lambda x: x[1], reverse=True)
        parent = sortedPop[0]
        # mutation
        offspringSolution = parent[0]
        randomIndex = random.randint(0, len(data) - 1)
        mutation = offspringSolution[randomIndex]
        if (mutation == 0):
            offspringSolution[randomIndex] = 1
        else:
            offspringSolution[randomIndex] = 0
        # create offspring Chromosome
        CHROMO = [] * 3  # [[binary soultion], fitness, total weight]
        fitness = 0
        totalWeight = 0
        for j in range(len(offspringSolution)):
            if (offspringSolution[j] == 1):
                fitness += data[j][0]
                totalWeight += data[j][1]
        CHROMO.append(offspringSolution)
        CHROMO.append(fitness)
        CHROMO.append(totalWeight)
        # if (CHROMO[2] <= capacity):
        POPULATION_TWO.append(CHROMO)
        # initCount += 1
    POPULATION_ONE = POPULATION_TWO
    print(POPULATION_TWO)

    genCount += 1
