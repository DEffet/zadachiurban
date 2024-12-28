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


# Пример использования
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Тестирование метода go_to
h1.go_to(5)  # Ожидаемый вывод: 1, 2, 3, 4, 5
h2.go_to(10)  # Ожидаемый вывод: "Такого этажа не существует"
