first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка, вычисляющая разницу длин строк, если длины не равны
first_result = (len(word1) - len(word2) for word1, word2 in zip(first, second) if len(word1) != len(word2))

# 2. Генераторная сборка, сравнивающая длины строк в одинаковых позициях без использования zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))
print(list(second_result))
