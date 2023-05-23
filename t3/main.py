# Сортировка Шелла
import random


def shellSort(arr):
    n = len(arr)
    # устанавливаем отступ величиной равной половине длины массива
    gap = n//2
    itern = 0
    # пока отступ больше нуля
    while gap > 0:
        itern += 1
        # сортируем подсписки из элементов, отстающих друг от друга на gap позиций
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        print(f"{itern} итерация)", *arr)
        gap //= 2

    return arr

n = int(input("введите количество элементов:"))
n_c = random.randint(2, 3)
n -= n_c
otr_c = random.randint(n // 4, n // 2)
p_c = n - otr_c
sample_data = [random.randint(-100, -1) for _ in range(otr_c)] + [0] * n_c + [random.randint(1, 100) for _ in range(p_c)]
random.shuffle(sample_data)
print("sample data:", *sample_data)
shellSort(sample_data)
print("result:", *sample_data)