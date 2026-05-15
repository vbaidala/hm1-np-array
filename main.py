import numpy as np


# створюємо двовимірний масив 3x3 з випадкових чисел від 1 до 100
arr = np.random.randint(1, 101, size=(3, 3))

print("Початковий масив:")
print(arr)

# обчислюємо суму всіх елементів масиву
total_sum = np.sum(arr)

print("\nСума всіх елементів масиву:")
print(total_sum)