class Vehicle:                                               # создаем класс автомобиль
    def __init__(self,owner,__model,__color,__engine_power):      # инициируем вводимые атрибуты автомобилей
        self.owner = str.title(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)

    __COLOR_VARIANTS = ["BLAcK","WHITE","YELLOW","GREEN"]    # атрибут возможных цветовых раскрасок

    def get_model(self):                                     #метод вывода модели автомобиля
        return f'Модель: {self.__model}'

    def get_horsepower(self):                                #метод вывода мощность автомобиля
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):                                     #метод вывода цвета автомобиля
        return f'Цвет: {self.__color}'

    def print_info(self):
        print (self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self,new_color):
        self.new_color = new_color
        if self.new_color.upper() in map(str.upper, self.__COLOR_VARIANTS) :
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
