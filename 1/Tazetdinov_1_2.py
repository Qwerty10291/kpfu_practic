
def first():
    var1 = None
    var2 = True
    var3 = 1
    var4 = 5.7
    var5 = 5 + 4j
    print("\n".join(map(lambda x:x.__class__.__name__, (var1, var2, var3, var4, var5))))

def second():
    revenue = 48000
    users_count = 3500
    print(f"Значение ARPU пользователей Санкт-Петербурга равно {revenue / users_count:.4f}, что выше в сравнении с предыдущими показателями")

def third():
    cost_per_item = 230.0
    number = 50
    print("The total cost of" + str(number) + "item is" + str(cost_per_item))

first()
second()
third()