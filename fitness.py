import math

class FitnessMax():
    def __init__(self):
        self.values = [0]

def my_func(x):
    return math.sin(2 * x) / x ** 2

def oneMaxFitness(individual):
    return my_func(individual.get_num()), individual.get_num()
