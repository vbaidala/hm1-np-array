import numpy as np


# створюємо двовимірний масив 3x3 з випадкових чисел від 1 до 100
arr = np.random.randint(1, 101, size=(3, 3))

print("Початковий масив:")
print(arr)

# обчислюємо суму всіх елементів масиву
total_sum = np.sum(arr)

print("\nСума всіх елементів масиву:")
print(total_sum)

# знаходимо індекс максимального елемента у розгорнутому масиві
max_index = np.argmax(arr)

# знаходимо індекс мінімального елемента у розгорнутому масиві
min_index = np.argmin(arr)


# перетворюємо індекси у формат рядок-стовпець
max_position = np.unravel_index(max_index, arr.shape)
min_position = np.unravel_index(min_index, arr.shape)

print("\nМаксимальне значення:")
print(arr[max_position])

print("Індекс максимального значення:")
print(max_position)

print("\nМінімальне значення:")
print(arr[min_position])

print("Індекс мінімального значення:")
print(min_position)