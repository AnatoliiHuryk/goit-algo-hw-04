import random
import timeit

# Cортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Cортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для тестування та заміру часу виконання
def measure_time(sort_func, data):
    data_copy = data[:]
    return timeit.timeit(lambda: sort_func(data_copy), number=1)

# Набори даних для тестування
small_data = random.sample(range(100), 10)            # Невеликий масив з 10 елементів
medium_data = random.sample(range(1000), 100)         # Середній масив з 100 елементів
large_data = random.sample(range(10000), 1000)        # Великий масив з 1000 елементів

# Тестування та замір часу
print("Алгоритми сортування на різних наборах даних:\n")

for data, label in [(small_data, "Невеликий масив"), (medium_data, "Середній масив"), (large_data, "Великий масив")]:
    print(f"{label} ({len(data)} елементів):")

    # Сортування злиттям
    merge_time = measure_time(merge_sort, data)
    print(f"Сортування злиттям: {merge_time:.6f} секунд")

    # Сортування вставками
    insertion_time = measure_time(insertion_sort, data)
    print(f"Сортування вставками: {insertion_time:.6f} секунд")

    # Timsort (вбудована функція sorted)
    timsort_time = measure_time(sorted, data)
    print(f"Timsort (sorted): {timsort_time:.6f} секунд")

    print()

