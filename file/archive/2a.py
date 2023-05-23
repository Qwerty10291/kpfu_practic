def fit_to_table(arr:list):
    for i in range(len(arr[0])):
        max_len = max(map(lambda x: len(x[i]), arr))
        for r in arr:
            r[i] = '| ' + r[i].center(max_len) + " "



data = [row.replace('|', ' ').split() for i, row in enumerate(open(input('введите название файла с данными:'), 'r', encoding='utf-8')) if i % 2]

new_data = input('введите фамилию и оценки нового ученика через пробел:').split()
k = int(input('введите позицию на которою необходимо поставить ученика:'))
data.insert(k, [str(k)] + new_data)
for i in range(k + 1, len(data)):
    data[i][0] = str(int(data[i][0]) + 1)

fit_to_table(data)
out = open(input('введите название файла с результатом:'), 'w', encoding='utf-8')


for r in data:
    row = ''.join(r)
    print('|' + '-' * (len(row) - 1) + '|', file=out)
    print(row + '|', file=out)

print('|' + '-' * (len(''.join(data[-1])) - 1) + '|', file=out)