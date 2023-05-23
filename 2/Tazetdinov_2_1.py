def first():
    values = (float(i) for i in input("Введите три числа через пробел:").split())
    print("Минимальное значение равно", min(values))

def third():
    """Чтобы работал match необходим python v3.10 или выше"""
    num1 = float(input())
    operand = input()
    num2 = float(input())
    try:
        match operand:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case "/":
                result = num1 / num2
            case 'mod':
                result = int(num1) % int(num2)
            case "pow":
                result = num1 ** num2
            case "div":
                result = num1 // num2
    except ZeroDivisionError:
        print("Деление на 0!")
        return
    print(result)

first()
third()