# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Функція жадібного алгоритму
def greedy_algorithm(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_cost = 0
    total_calories = 0
    selected_items = []
    
    for name, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(name)
            total_cost += info['cost']
            total_calories += info['calories']
    
    return selected_items, total_calories, total_cost

# Функція динамічного програмування
def dynamic_programming(items, budget):
    # Перетворюємо словник в списки для зручності
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    n = len(item_names)
    
    # Ініціалізуємо таблицю DP
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Відновлюємо вибрані страви
    w = budget
    selected_items = []
    total_cost = 0
    total_calories = dp[n][budget]
    
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            total_cost += costs[i - 1]
            w -= costs[i - 1]
    
    selected_items.reverse()  # Відновлюємо порядок
    return selected_items, total_calories, total_cost

# Приклад використання функцій
if __name__ == "__main__":
    budget = 100  # Заданий бюджет
    
    # Використання жадібного алгоритму
    greedy_selection, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
    print("Жадібний алгоритм:")
    print(f"Вибрані страви: {greedy_selection}")
    print(f"Загальна калорійність: {greedy_calories}")
    print(f"Загальна вартість: {greedy_cost}")
    print()
    
    # Використання алгоритму динамічного програмування
    dp_selection, dp_calories, dp_cost = dynamic_programming(items, budget)
    print("Алгоритм динамічного програмування:")
    print(f"Вибрані страви: {dp_selection}")
    print(f"Загальна калорійність: {dp_calories}")
    print(f"Загальна вартість: {dp_cost}")
