# задание 2c
from typing import Iterable, Callable


def max(iterable: Iterable):
    m = next(iterable)
    for e in iterable:
        if e > m:
            m = e
    return m


def sum(iterable: Iterable):
    s = next(iterable)
    for e in iterable:
        s += e
    return s


def map(func: Callable, iter: Iterable):
    for e in iter:
        yield func(e)

def fit_to_table(arr:list):
    for i in range(len(arr[0])):
        max_len = max(map(lambda x: len(x[i]), arr))
        for r in arr:
            r[i] = '| ' + r[i].center(max_len) + " "

def main():
    input_filename = input("введите название файла с данными:")
    try:
        data = [row.replace('|', ' ').split() for i, row in enumerate(
            open(input_filename, 'r', encoding='utf-8')) if i % 2]
    except FileNotFoundError:
        print('файл не найден')
        return

    output_filename = input("введите название файла с результатами:")
    try:
        out_file = open(output_filename, 'w', encoding='utf-8')
    except (FileNotFoundError, FileExistsError):
        print("такой папки нет или файл уже сущетсвует")
        return

    soname, height = input(
        "введите фамилию и рост нового ученика через пробел:").split()
    height = int(height)
    for i in range(1, len(data)):
        if int(data[i][2]) < height:
            data.insert(i, [str(i), soname, str(height)])
            for j in range(i + 1, len(data)):
                data[j][0] = str(int(data[j][0]) + 1)
            break
    
    fit_to_table(data)
    
    gap = '|' + '-' * (sum(map(lambda x: len(x), data[0])) - 1) + '|'
    print(gap, file=out_file)
    for row in data:
        print(*row, "|", sep="", file=out_file)
        print(gap, file=out_file)
    out_file.close()

main()
