def get_delims(num:int) -> set[int]:
    dels = set()
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            dels.add(n)
            dels.add(num // n)
    return dels

def first():
    a = int(input("введите a:"))
    b = int(input('введите b:'))
    print(min(get_delims(a) & get_delims(b)))

def second():
    n = int(input("введите n:"))
    c = 0
    i = 0
    while True:
        i += 1
        for _ in range(i):
            print(i, end=" ")
            c += 1
            if c >= n:
                print()
                return

def third():
    nums = (int(el) for el in input("введите список чисел:").split())
    n = int(input('введите число для поиска'))
    flt = [i for i, num in enumerate(nums) if num == n]
    if len(flt) == 0:
        print("Отсутствует")
    else:
        print("Позиции:", *flt)

first()
second()
third()