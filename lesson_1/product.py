class Product:
    def __init__(self,name, price,description,dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Name: {self.name}\nPrice: {self.price}\nDescription: {self.description}\nDimensions: {self.dimensions}"






        