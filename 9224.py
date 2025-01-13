# Исключение для некорректного VIN-номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

# Исключение для некорректных номеров автомобиля
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

# Класс автомобиля
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # Название модели автомобиля
        self.__vin = None  # Инициализация приватного атрибута VIN
        self.__numbers = None  # Инициализация приватного атрибута номера
        # Проверяем VIN и номера через валидирующие методы
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        """
        Проверяет корректность VIN-номера.
        """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers):
        """
        Проверяет корректность номера автомобиля.
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Неверная длина номера")
        return True

# Пример использования
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
