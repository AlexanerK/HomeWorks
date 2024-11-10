from random import  randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = int(speed)


    def move(self, dx, dy, dz):
        self.dx = int(dx)
        self.dy = int(dy)
        self.dz = int(dz)
        if dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [self.dx * self.speed, self.dy * self.speed, self.dz * self.speed]

    def get_cords(self):
        print(f'X: {int(self._cords[0])} Y: {int(self._cords[1])} Z: {int(self._cords[2])}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {randint (1,4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz = (abs(dz))/2 * self.speed
        self._cords[2] = self._cords[2] - self.dz



class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird,PoisonousAnimal, AquaticAnimal):
    def __init__(self,speed):
        super().__init__(speed)
    def speak(self):
        sound = "Click-click-click"
        print(sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
