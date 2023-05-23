def first():
    s = 0
    while (n := int(input())) != 0:
        s += n ** 2
    print(s)

def second():
    while (n := int(input())) < 100:
        if n > 10:
            print(n)

def third():
    nums = [int(line) for line in input("введите значения через пробел:").split()]
    avg = sum(nums) / len(nums)
    filtered = [n for n in nums if n >= avg]
    print("Среднее арифметическое равно", int(avg))
    print("всего значений больше среднего арифметического", len(filtered))
    print("Список значений:", *filtered)

first()
second()
third()