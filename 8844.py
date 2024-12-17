def calculate_structure_sum(data):
    total_sum = 0  # Счётчик для суммы чисел и длин строк

    # Определяем тип текущего элемента
    if isinstance(data, (list, tuple, set)):  # Если список, кортеж или множество
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов
    elif isinstance(data, dict):  # Если словарь
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Обрабатываем ключи
            total_sum += calculate_structure_sum(value)  # Обрабатываем значения
    elif isinstance(data, int):  # Если целое число
        total_sum += data
    elif isinstance(data, str):  # Если строка
        total_sum += len(data)

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый вывод: 99
