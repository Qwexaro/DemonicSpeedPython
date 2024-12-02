import numpy as np
from numba import njit

@njit
def bubble_sort(arr):
    N = len(arr)
    # Сортировка методом "пузырька"
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

@njit
def generate_random_array(N):
    return np.random.randint(0, 11, size=N)  

@njit
def speed():
    N = 100000
    a = generate_random_array(N)
    bubble_sort(a)
    return a

sorted_array = speed()

for i in sorted_array:
    print(i, end='')
