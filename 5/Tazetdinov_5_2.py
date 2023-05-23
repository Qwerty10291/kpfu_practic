def first():
    arr = [int(e) for e in input().split()]
    target = int(input())
    print(*filter(lambda x: arr[x] == target, range(len(arr))))


def second():
    matrix = []
    while (row := input()) != "end":
        matrix.append([int(e) for e in row.split()])

    matrix_result = [[0 for _ in range(len(matrix[i]))] for i in range(len(matrix))]
    for i in range(len(matrix_result)):
        for j in range(len(matrix_result[i])):
            matrix_result[i][j] = matrix[i - 1][j] + matrix[i + 1 if i < len(matrix) - 1 else 0][j] \
                 + matrix[i][j - 1] + matrix[i][j + 1 if j < len(matrix[i]) - 1 else 0]

    for row in matrix_result:
        print(*row)

first()
second()