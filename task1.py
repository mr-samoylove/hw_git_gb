# Напишите функцию для транспонирования матрицы.

def transposition(matrix: tuple) -> tuple:
    return tuple(zip(*matrix))


matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print('old matrix: ', matrix)
print('new matrix: ', transposition(matrix))
