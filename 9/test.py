import random
import csv
from faker import Faker

fake = Faker('ru_RU')


names = ["Абзалов","Багыманов","Билданов","Богданов","Вафин","Гареева","Иванова","Ихсанов","Ларионов","Лернер","Ляхов","Мальцева","Масагутов","Мифтахов","Можарова","Никитин","Петров","Сайфуллин","Синеев","Сулейманов"]
subjects = ['algeom', 'matan', "с++", 'english']


writer = csv.writer(open('sineev.csv', 'w'), dialect='excel')
for i in range(25):
    gender = bool(random.randint(0, 1))
    name = fake.last_name_male() if gender else fake.last_name_female()
    marks = [random.randint(2, 4) + (1 if random.randint(0, 100) > 10 else 0) for i in range(len(subjects))]
    writer.writerow([name, "male" if gender else "female"] + marks)