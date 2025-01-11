def custom_write(file_name, strings):
    strings_positions = {}  # Словарь для хранения позиций строк
    with open(file_name, 'w', encoding='utf-8') as file:  # Открываем файл для записи с кодировкой utf-8
        for i, string in enumerate(strings, start=1):  # Итерируемся по строкам с нумерацией с 1
            byte_position = file.tell()  # Получаем текущую позицию в файле в байтах
            file.write(string + '\n')  # Записываем строку и добавляем символ перевода строки
            strings_positions[(i, byte_position)] = string  # Сохраняем позицию и строку в словарь
    return strings_positions  # Возвращаем словарь с позициями строк

# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
