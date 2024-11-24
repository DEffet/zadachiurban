def find_password(n):
    # Список для хранения пар чисел
    pairs = []
    
    # Я здесь перебираю первое число пары от 1 до n-1
    for i in range(1, n):
        # А тут уже второе число пары, оно больше первого
        for j in range(i + 1, n + 1):
            # Проверяю, делится ли n на сумму этой пары
            if n % (i + j) == 0:
                pairs.append(f"{i}{j}")  # Если делится, добавляю пару в список

    # Склеиваю все пары в одну строку для результата
    return ''.join(pairs)


# Проверяем на примере всех чисел от 3 до 20
for number in range(3, 21):
    result = find_password(number)
    print(f"{number} - {result}")
