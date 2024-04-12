import random

ONE_MAX_LENGTH = 15
LEFT_POINT = -20
RIGHT_POINT = -3.1

class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = FitnessMax()

    def to_decimal(self):
        return int(''.join(map(str, self)), 2)

    def get_num(self):
        x = self.to_decimal()
        return LEFT_POINT + x * (RIGHT_POINT - LEFT_POINT) / (2 ** ONE_MAX_LENGTH - 1)

def individualCreator():
    return Individual([random.randint(0, 1) for _ in range(ONE_MAX_LENGTH)])
