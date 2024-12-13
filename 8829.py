def get_multiplied_digits(number):
    # Преобразуем число в строку для обработки цифр
    str_number = str(number)
    
    # Удаляем ведущие и промежуточные нули
    if '0' in str_number:
        str_number = str_number.replace('0', '')
    
    # Если строка пустая (например, если всё число было из нулей), возвращаем 1
    if not str_number:
        return 1
    
    # Преобразуем первую цифру в число
    first = int(str_number[0])
    
    # Если длина строки больше 1, рекурсивно вызываем функцию
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки равна 1, возвращаем эту цифру
        return first

# Примеры использования функции
result1 = get_multiplied_digits(40203)
print(result1)  # Ожидаемый вывод: 24

result2 = get_multiplied_digits(402030)
print(result2)  # Ожидаемый вывод: 24
