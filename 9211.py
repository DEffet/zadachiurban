def add_everything_up(a, b):
    try:
        # Попробуем сложить a и b стандартным способом
        return a + b
    except TypeError:
        # Если возникнет ошибка, значит a и b разных типов
        return f"{a}{b}"  # Возвращаем строковое представление

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))    # яблоко4215
print(add_everything_up(123.456, 7))        # 130.456
