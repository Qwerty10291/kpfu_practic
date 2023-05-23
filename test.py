from faker import Faker
import random
f = Faker('ru-RU')
print(f.last_name())
# print(*sorted(list(set(random.randint(160, 190) for _ in range(20))), reverse=True), sep='\n')