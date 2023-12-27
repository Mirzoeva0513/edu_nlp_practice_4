"""
Реализуйте абстрактный класс Animal. Экземпляры класса Animal должны иметь
строковые поля name и info, значения которых запрашиваются при инициализации и содержат значения по умолчанию.

Реализуйте классы Zebra и Dolphin, наследующие от класса Animal. Оба класса
должны иметь строковые поля name и info, а так же целочисленное поле age.
Значения полей запрашиваются при инициализации.
"""
from abc import ABC


### ваше решение: ###
class Animal(ABC):
class Animal(ABC):
    ["22:44"]
from abc import ABC, abstractmethod
 
class Animal(ABC):
    def __init__(self, name="Unknown", info="Generic animal"):
        self.name = name
        self.info = info
 
class Zebra(Animal):
    def __init__(self, name, info, age=0):
        super().__init__(name, info)
        self.age = age
 
class Dolphin(Animal):
    def __init__(self, name, info, age=0):
        super().__init__(name, info)
        self.age = age
    ["22:45"]
zebra = Zebra("Zebra", "Striped mammal", age=5)
dolphin = Dolphin("Dolphin", "Smart marine mammal", age=10)
 
print(zebra.name, zebra.info, zebra.age)  # Вывод: Zebra Striped mammal 5
print(dolphin.name, dolphin.info, dolphin.age)  # Вывод: Dolphin Smart marine mammal 10
