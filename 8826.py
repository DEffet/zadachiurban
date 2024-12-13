def single_root_words(root_word, *other_words):
    # Приводим корневое слово к нижнему регистру для корректного сравнения
    root_word = root_word.lower()
    
    # Создаём пустой список для хранения слов, которые соответствуют условиям
    same_words = []

    # Перебираем каждое слово из *other_words
    for word in other_words:
        # Приводим слово к нижнему регистру и проверяем условие
        if root_word in word.lower() or word.lower() in root_word:
            same_words.append(word)

    # Возвращаем сформированный список
    return same_words

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на экран
print(result1)
print(result2)
