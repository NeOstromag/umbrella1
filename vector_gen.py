import random

def backpack_vector_generator(n, amax):
    for _ in range(50):
        backpack_vector = [random.randint(1, amax) for _ in range(n)]
        yield backpack_vector

# Укажите номер варианта для определения значений n и amax
variant_number = 6
n = variant_number
amax = variant_number

backpack_vectors = backpack_vector_generator(n, amax)

for i, vector in enumerate(backpack_vectors):
    print(f"Backpack Vector {i+1}: {vector}")