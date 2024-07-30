class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __len__(self):
        return self.floor

    def __str__(self):
        return f'Название: {self.name}, количество этажей - {self.floor}'


house1 = House("ЖК Романтики", 10)
house2 = House("ЖК АУРА", 24)
print(house1)
print(house2)
print(len(house1))
print(len(house2))
