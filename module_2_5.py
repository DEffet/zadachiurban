# Определение функции get_matrix
def get_matrix(n, m, value):
    # Проверка на неотрицательные размеры матрицы
    if n <= 0 or m <= 0:
        return []

    # Создаем пустую матрицу
    matrix = []

    # Заполняем матрицу
    for _ in range(n):  # Внешний цикл для строк
        row = []  # Создаем пустую строку
        for _ in range(m):  # Внутренний цикл для столбцов
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)  # Добавляем строку в матрицу

    return matrix  # Возвращаем готовую матрицу


# Примеры вызова функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов
print(result1)
print(result2)
print(result3)
