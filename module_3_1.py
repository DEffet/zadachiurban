# Глобальная переменная для отслеживания количества вызовов
calls = 0

# Функция для подсчёта вызовов
def count_calls():
    global calls
    calls += 1

# Функция для обработки строки: возвращает длину, верхний и нижний регистры
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    return (len(string), string.upper(), string.lower())

# Функция для проверки, содержится ли строка в списке (без учета регистра)
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    # Приводим все строки к нижнему регистру для сравнения
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Пример вызова функций
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')

# Проверки на вхождение строки в список
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Выводим количество вызовов функций
print(calls)  # 4
