def all_variants(text):
    n = len(text)
    for length in range(1, n + 1):  # Длина подпоследовательности
        for start in range(n - length + 1):  # Начальный индекс подпоследовательности
            yield text[start:start + length]

# Пример использования
a = all_variants("abc")

for i in a:
    print(i)
