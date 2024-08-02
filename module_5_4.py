class House:

    houses_history = []

    def __new__ (cls,*args, **kwargs):
        cls.houses_history.append (args[0])
        return object.__new__(cls)

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

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')

house1 = House("ЖК Романтики", 10)
print(House.houses_history)
house2 = House("ЖК АУРА", 24)
print(House.houses_history)
house3 = House("ЖК Урбан" , 30)
print(House.houses_history)
house4 = House("ЖК НСК", 21)
print(House.houses_history)

del (house1)
print(House.houses_history)
del (house2)
print(House.houses_history)
