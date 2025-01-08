class House:
    houses_history = []  # Общий атрибут для всех объектов, список с названиями домов

    def __new__(cls, *args, **kwargs):
        """Создает объект и добавляет его название в историю."""
        if len(args) > 0:  # Проверяем наличие имени дома в args
            cls.houses_history.append(args[0])  # Добавляем имя дома в историю
        return super().__new__(cls)  # Создаем объект с помощью базового метода

    def __init__(self, name, number_of_floors):
        """Инициализирует объект класса House."""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """Выводит номера этажей от 1 до new_floor или сообщение об ошибке."""
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """Возвращает количество этажей в здании."""
        return self.number_of_floors

    def __str__(self):
        """Возвращает строку с информацией о здании."""
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        """Выводит сообщение при удалении объекта."""
        print(f"{self.name} снесён, но он останется в истории")


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # Вывод: ЖК Акация снесён, но он останется в истории
del h3  # Вывод: ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаляем последний объект
del h1  # Вывод: ЖК Эльбрус снесён, но он останется в истории
