class Animal:
    def __init__ (self,name):
        self.name = name
    alive = True
    fed = False
    def eat(self, food):
        if food.edible == False:
            print(f'{self.name} съел {food.name} и умер')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name} ')
            self.fed = True
            
class Plant:
    edible = False
    def __init__ (self,name):
        self.name = name

class Mammal (Animal):
    pass

class Predator (Animal):
    pass

class Flower (Plant):
    pass

class Fruit (Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Ядовитый цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


