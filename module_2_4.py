# Исходные данные
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебор чисел в списке numbers
for num in numbers:
    if num == 1:  # Число 1 не является простым или составным
        continue
    
    is_prime = True  # Изначально предполагаем, что число простое

    # Проверка на простоту: делители от 2 до num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # Если нашли делитель, число не простое
            break  # Прерываем цикл, так как число не простое

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Вывод списков
print("Primes:", primes)
print("Not Primes:", not_primes)
