class House:
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


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Тестирование __str__
print(h1)  # Ожидаемый вывод: "Название: ЖК Эльбрус, кол-во этажей: 10"
print(h2)  # Ожидаемый вывод: "Название: ЖК Акация, кол-во этажей: 20"

# Тестирование __len__
print(len(h1))  # Ожидаемый вывод: 10
print(len(h2))  # Ожидаемый вывод: 20
