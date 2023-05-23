# шейкерная сортировка
import random

def shaker_sort(data:list):
    # инициализируем индексы нижней и верхней границ
    li = 0
    ri = len(data) - 1
    itern = 0
    
    # пока нижняя граница меньше верхней 
    while li <= ri:
        # двигаемся от нижней до верхней границы
        for i in range(li, ri):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        # уменьшаем верхнюю границу
        ri -= 1
        
        itern += 1
        print(f"{itern})", *data)

        # двигаемся от верхней до нижней границы
        for i in range(ri, li, -1):
            if data[i - 1] > data[i]:
                data[i], data[i - 1] = data[i - 1], data[i]
        # увеличиваем нижнюю границу
        li += 1
        
        itern += 1
        print(f"{itern})", *data)
    
    return data

n = int(input("введите количество элементов:"))
n_c = random.randint(2, 3)
n -= n_c
otr_c = random.randint(n // 4, n // 2)
p_c = n - otr_c
sample_data = [random.randint(-100, -1) for _ in range(otr_c)] + [0] * n_c + [random.randint(1, 100) for _ in range(p_c)]
random.shuffle(sample_data)
print("sample data:", *sample_data)
print("sorted data:", *shaker_sort(sample_data))