from pprint import pprint

from unicodedata import category


class Product:

    def __init__(self, name:str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        get_file = file.read()
        file.close
        return get_file

    def add(self, *products):
        new_file = ''
        for i in products:
            get_file = self.get_products()




            if i.name in get_file and i.category in get_file:
                    weight = str(get_file.replace('\n', ','))
                    weight = weight.replace(' ', ',').split(',')
                    index = weight.index(i.name)
                    weight = str(float(weight[index+2])+i.weight)
                    file = open(self.__file_name,"a", encoding='utf-8')
                    new_file = str(f'Продукт {i.name} уже был в магазине, его общий вес равен {weight}')
                    file.write(new_file + '\n')
                    file.close


            else:
                    file = open(self.__file_name, 'a')
                    file.write(Product.__str__(i)+'\n')
                    file.close









s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
