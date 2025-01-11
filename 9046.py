class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read()
            return products
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        existing_names = [line.split(', ')[0] for line in existing_products if line]

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name not in existing_names:
                    file.write(str(product) + '\n')
                else:
                    print(f'Продукт {product.name} уже есть в магазине')
