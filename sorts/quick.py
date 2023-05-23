def quick_part(values:list, l:int, r:int):
    x = values[r]
    less = l
    for i in range(l, r):
        if values[i] <= x:
            values[i], values[less] = values[less], values[i]
            less += 1
    values[less], values[r] = values[r], values[less]
    return less


def quick_sort(values):
    def impl(l, r):
        if l < r:
            q = quick_part(values, l, r)
            impl(l, q - 1)
            impl(q + 1, r)
    
    impl(0, len(values) - 1)

a = [1, 2, -1, 10, -150, 2, 2, 4, 50]
quick_sort(a)
print(a)