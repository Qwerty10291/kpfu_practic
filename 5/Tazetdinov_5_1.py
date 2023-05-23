import random

def first(lst:list):
    print(*sorted(lst[::2], reverse=True))

def filter_up():
    max_val = -float('inf')
    def wrapper(value):
        nonlocal max_val
        if value > max_val:
            max_val = value
            return True
    return wrapper

def second(lst:list):
    print(*filter(filter_up(), lst))

def third(lst:list):
    max_val, min_val, max_ind, min_ind = lst[0], lst[0], 0, 0
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
            max_ind = i
        elif lst[i] < min_val:
            min_val = lst[i]
            min_ind = i
    lst[min_ind], lst[max_ind] = lst[max_ind], lst[min_ind]
    print(lst)


lst = [random.randint(-100, 100) for _ in range(10)]
print(lst)

first(lst)
second(lst)
third(lst)