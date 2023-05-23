import string
import re

def check(pswd:str):
    return len(pswd) >= 8 and re.match(f"[a-z]+[A-Z]+[{string.punctuation}]+\d+", pswd) is not None

# while True:
#     email = input("введите адрес электронной почты:")
#     if email.endswith("@kpfu.ru"):
#         break
#     else:
#         print('Требуется указать адрес в доменной зоне kpfu.ru')

while True:
    password = input("введите пароль:")
    if check(password):
        break
    print("пароль не соответсвует требованиям")

for i in range(3):
    if input("введите пароль еще раз:") == password:
        print("вы успешно прошли регистрацию")
        break
    else:
        print("Пароли не совпадают")
else:
    print("вы неправильно повторно введи пароль 3 раза. Попробуйте придумать другой пароль")