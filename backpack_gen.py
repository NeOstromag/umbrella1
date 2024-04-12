import random


def backpack_task_generator(backpack_vector, num_tasks):
    n = len(backpack_vector)
    for _ in range(num_tasks):
        # Выбираем случайное количество предметов от 10% до 50%
        num_items = random.randint(n // 10, n // 2)

        # Выбираем случайные индексы предметов
        item_indices = random.sample(range(n), num_items)

        # Суммируем веса выбранных предметов
        target_weight = sum(backpack_vector[i] for i in item_indices)

        yield {"backpack_vector": backpack_vector, "target_weight": target_weight}


# Укажите номер варианта для определения значений n и amax
variant_number = 6
n = variant_number
amax = variant_number

backpack_vectors = backpack_vector_generator(n, amax)

for i, vector in enumerate(backpack_vectors):
    tasks = backpack_task_generator(vector, random.randint(10, 20))
    print(f"Backpack Vector {i + 1}: {vector}")
    for j, task in enumerate(tasks):
        print(f"Task {j + 1}: {task}")