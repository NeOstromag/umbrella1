import random
import copy
import time


def fitness_function(backpack_vector, items_weights, target_weight):
    total_weight = sum([backpack_vector[i] * items_weights[i] for i in range(len(backpack_vector)])
    if total_weight <= target_weight:
        return total_weight
    else:
    return 0


def genetic_algorithm(backpack_vector, items_weights, target_weight):
    population_size = 10
    mutation_rate = 0.1
    max_generations = 1000

    population = [[random.randint(0, 1) for _ in range(len(backpack_vector))] for _ in range(population_size)]

    best_fitness = 0
    generations_without_improvement = 0

    start_time = time.time()

    for generation in range(max_generations):
        new_population = []

        # Evaluate fitness of each individual
        fitness_scores = [fitness_function(individual, items_weights, target_weight) for individual in population]

        # Select parents for crossover
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population), reverse=True)]
        parents = sorted_population[:2]

        # Crossover
        child = []
        for i in range(len(backpack_vector)):
            parent_idx = random.randint(0, 1)
            child.append(parents[parent_idx][i])

        # Mutation
        for i in range(len(child)):
            if random.random() < mutation_rate:
                child[i] = 1 - child[i]

        new_population.append(child)

        # Update best fitness and check conditions for termination
        new_fitness = fitness_function(child, items_weights, target_weight)
        if new_fitness > best_fitness:
            best_fitness = new_fitness
            generations_without_improvement = 0
        else:
            generations_without_improvement += 1

        if best_fitness == 0 or generations_without_improvement == 2 or time.time() - start_time > 2 * max_generations:
            break

        population = copy.deepcopy(new_population)

    return population


# Пример использования
backpack_vector = [3, 5, 2, 8, 6]
items_weights = [10, 20, 15, 25, 30]
target_weight = 11

result = genetic_algorithm(backpack_vector, items_weights, target_weight)
print("Best solution found:", result)