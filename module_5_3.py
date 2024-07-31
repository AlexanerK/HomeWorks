class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __len__(self):
        return self.floor


    def __eq__(self, other):
        if isinstance(other.floor,int):
            return self.floor == other.floor
        else:
            print("значение не типа int")


    def __lt__(self, other):
        return self.floor < other.floor


    def __le__(self, other):
        return self.floor <= other.floor

    def __gt__(self, other):
        return self.floor > other.floor

    def __ge__(self, other):
        return self.floor >= other.floor

    def __ne__(self, other):
        return self.floor != other.floor

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.floor + value)
        else:
            print("значение value не типа int")
            return NotImplemented
    def __radd__(self, value):
        return   self + value

    def __iadd__(self, value):
        if isinstance(value, int):
         self.floor += value
         return self

    def __str__(self):
        return f'Название: {self.name}, количество этажей - {self.floor}'



house1 = House("ЖК Романтики", 10)
house2 = House("ЖК АУРА", 24)
print(house1)
print(house2)
print(len(house1))
print(len(house2))
print(house1 == house2)
print(house1 < house2)
print(house1 <= house2)
print(house1 > house2)
print(house1 >= house2)
print(house1 != house2)
house1 = house1 + 10
print(house1)
house1 += 15
print(house1)
house1 = 13 + house1
print(house1)
house2 = house2 +10
print(house2)
house2 += 15
print(house2)
house2 = 13 + house2
print(house2)

