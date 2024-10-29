import random
import matplotlib.pyplot as plt

# Кількість симуляцій (кількість кидків двох кубиків)
num_rolls = 1_000_000

# Словник для підрахунку появи кожної суми
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидання двох кубиків num_rolls разів
for _ in range(num_rolls):
    dice1 = random.randint(1, 6)  # Перший кубик (випадкове число від 1 до 6)
    dice2 = random.randint(1, 6)  # Другий кубик (випадкове число від 1 до 6)
    dice_sum = dice1 + dice2      # Сума чисел на обох кубиках
    sum_counts[dice_sum] += 1     # Збільшуємо лічильник для цієї суми

# Розрахунок ймовірностей на основі симуляцій
sum_probabilities = {k: (v / num_rolls) * 100 for k, v in sum_counts.items()}

# Виведення результатів у форматі таблиці
print("Сума\tЕкспериментальна ймовірність (%)\tАналітична ймовірність (%)")
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}
for sum_val in range(2, 13):
    print(f"{sum_val}\t{sum_probabilities[sum_val]:.2f}\t\t\t{analytical_probabilities[sum_val]}")

# Побудова графіку для візуалізації ймовірностей
sums = list(sum_probabilities.keys())             # Список можливих сум
experimental_probs = list(sum_probabilities.values())  # Ймовірності на основі симуляцій
analytical_probs = list(analytical_probabilities.values())  # Аналітичні ймовірності

plt.plot(sums, experimental_probs, label='Ймовірність Монте-Карло', marker='o')
plt.plot(sums, analytical_probs, label='Аналітична ймовірність', marker='x')
plt.xlabel('Сума')
plt.ylabel('Ймовірність (%)')
plt.title('Ймовірність кожної суми при киданні двох кубиків')
plt.legend()
plt.show()
