def knapsack_solver(backpack_vector, target_weight):
    n = len(backpack_vector)
    dp = [[0 for _ in range(target_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, target_weight + 1):
            if backpack_vector[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - backpack_vector[i - 1]] + backpack_vector[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = target_weight
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= backpack_vector[i - 1]

    return selected_items


# Пример использования
backpack_vector = [3, 5, 2, 8, 6]
target_weight = 11

selected_items = knapsack_solver(backpack_vector, target_weight)
print("Selected items indices:", selected_items)
print("Selected items weights:", [backpack_vector[i] for i in selected_items])