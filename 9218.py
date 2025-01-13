def personal_sum(numbers):
    """
    Подсчитывает сумму чисел в коллекции numbers и количество некорректных данных.
    """
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item  # Пробуем добавить значение
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {item}")
            incorrect_data += 1  # Увеличиваем счётчик некорректных данных
    return result, incorrect_data

def calculate_average(numbers):
    """
    Подсчитывает среднее арифметическое чисел в коллекции numbers.
    Обрабатывает исключения: ZeroDivisionError и TypeError.
    """
    try:
        # Используем функцию personal_sum для подсчёта суммы и обработки ошибок
        total_sum, incorrect_count = personal_sum(numbers)
        # Среднее арифметическое: сумма / количество чисел
        return total_sum / (len(numbers) - incorrect_count)
    except ZeroDivisionError:
        # Возвращаем 0, если количество чисел равно 0
        return 0
    except TypeError:
        # Выводим сообщение об ошибке, если передан некорректный тип данных
        print("В numbers записан некорректный тип данных")
        return None

# Примеры выполнения
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
