first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# 2. Список кортежей из пар слов одинаковой длины
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# 3. Словарь, где ключ - строка, значение - длина строки (длина строки должна быть чётной)
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
