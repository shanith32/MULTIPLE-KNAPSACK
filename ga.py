import random
import copy
#Genetic algorithm to deal with the Knapsack problem

data = [[4, 2, 0], [5, 2, 1], [7, 11, 2],
        [7, 11, 3]]  # object set with the properties - [value, weight, id]

container = []  #the container to contain the objects in
capacity = 10  #weight capacity of the container

POP_SIZE = 5  #population size
GEN_AMOUNT = 10  #how many generations to run

# Initial Population
INITIAL_POPULATION = []  #The inital population array
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
        INITIAL_POPULATION.append(CHROMO)
        initCount += 1

print(INITIAL_POPULATION)
print(
    "-------------------------------------------------------------------------------------------------------------"
)

# Generation GA loop
genCount = 0
while (genCount != GEN_AMOUNT):
    print("gen :", genCount)
    POPULATION_TWO = []  #Second population array
    popCount = 0
    # for i in range(2):
    while (popCount != POP_SIZE):
        print("Initial pop of gen:", genCount, "is:", INITIAL_POPULATION)
        POPULATION_ONE = copy.deepcopy(
            INITIAL_POPULATION)  #First population array
        sortedPop = sorted(POPULATION_ONE, key=lambda x: x[1], reverse=True)
        # Find Parent Chromosome
        print("sorted pop", sortedPop)
        parent = sortedPop[0]
        print("parent chrmo: ", parent)
        # mutation
        offspringSolution = parent[0]
        print("offspring sol before:", offspringSolution)
        randomIndex = random.randint(0, len(data) - 1)
        print("random index to mutate:", randomIndex)
        mutation = offspringSolution[randomIndex]
        print("value in the random index: ", mutation)
        sortedPop = sorted(POPULATION_ONE, key=lambda x: x[1], reverse=True)
        # Testing 50% chance of mutation to happen
        testing = random.randint(0, 1)
        if (testing == 1):
            if (mutation == 0):
                offspringSolution[randomIndex] = 1
            else:
                offspringSolution[randomIndex] = 0
        print("offspring sol after mutation:", offspringSolution)
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
        print("Chromosome with mutated offpring sol:", CHROMO)
        if (CHROMO[2] <= capacity):
            POPULATION_TWO.append(CHROMO)
            print("count increeeseddd+++++++")
            popCount += 1
        print("New population with the CHOMO:", POPULATION_TWO)
        print("for is done-----------------")
    print("Population after a GEN:", POPULATION_TWO)
    INITIAL_POPULATION = copy.deepcopy(POPULATION_TWO)
    genCount += 1
print("FINAL POPULATION:", INITIAL_POPULATION)
sortedFinalPop = sorted(INITIAL_POPULATION, key=lambda x: x[1], reverse=True)
result = sortedFinalPop[0]
print("!!result!!:", result)
print("Total value of the soultion:", result[1],
      "Total weight of the soultion:", result[2])
