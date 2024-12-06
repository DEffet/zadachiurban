def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Шаг 1: вызовы функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Шаг 2: распаковка списка и словаря
values_list = [42, 'Привет', False]
values_dict = {'a': 3.14, 'b': 'Python', 'c': None}
print_params(*values_list)
print_params(**values_dict)

# Шаг 3: распаковка + отдельный параметр
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
