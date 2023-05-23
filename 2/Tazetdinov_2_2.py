def first():
    a, b, n = [int(input()) for _ in range(3)]
    if n < a:
        print("Недосып")
    elif n > b:
        print("Пересып")
    else:
        print("Это нормально")

def second():
    year = int(input("введите год:"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
       print("високосный")
    else:
        print("Не високосный")  

def third():
    amount = int(input("введите количество товара:")) 
    discount = int(input("введите размер скидки:"))
    price = 1500 * (1 - discount / 100)
    k = price * amount
    print(f"Стоимость {amount} товаров составит {k}, с учетом скидки {discount}%")

first()
second()
third()

