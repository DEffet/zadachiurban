def apply_all_func(int_list, *functions):
    results = {}  # Словарь для хранения результатов
    for func in functions:
        results[func.__name__] = func(int_list)  # Ключ - имя функции, значение - результат вызова
    return results

# Примеры использования
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
