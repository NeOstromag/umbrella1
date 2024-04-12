import random
import time
from individual import Individual, individualCreator
from fitness import oneMaxFitness
from selection import selTournament
from crossover import cxOnePoint
from mutation import mutFlipBit

POPULATION_SIZE = 30
P_CROSSOVER = 0.9
P_MUTATION = 0.1
MAX_GENERATIONS = 50

def run_genetic_algorithm(population_size, p_crossover, p_mutation):
    global POPULATION_SIZE
    POPULATION_SIZE = population_size
    global P_CROSSOVER
    P_CROSSOVER = p_crossover
    global P_MUTATION
    P_MUTATION = p_mutation

    start_time = time.time()
    population = [individualCreator() for _ in range(POPULATION_SIZE)]
    generationCounter = 0
    fitnessValues = [oneMaxFitness(individual) for individual in population]

    for individual, fitnessValue in zip(population, fitnessValues):
        individual.fitness.values = fitnessValue

    while generationCounter < MAX_GENERATIONS:
        generationCounter += 1
        offspring = selTournament(population, len(population))
        offspring = [Individual(ind) for ind in offspring]

        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < P_CROSSOVER:
                cxOnePoint(child1, child2)

        for mutant in offspring:
            if random.random() < P_MUTATION:
                mutFlipBit(mutant, indpb=1.0 / len(mutant))

        freshFitnessValues = [oneMaxFitness(individual) for individual in offspring]
        for individual, fitnessValue in zip(offspring, freshFitnessValues):
            individual.fitness.values = fitnessValue

        population[:] = offspring
        fitnessValues = [ind.fitness.values[0] for ind in population]

        maxFitness = max(fitnessValues)
        meanFitness = sum(fitnessValues) / len(population)
        print(f"Generation {generationCounter}: Max Fitness = {maxFitness}, Mean Fitness = {meanFitness}")

        best_index = fitnessValues.index(max(fitnessValues))
        print("Best Individual = ", *population[best_index], "\n")
        elapsed_time = time.time() - start_time

    return maxFitnessValues, meanFitnessValues, elapsed_time
