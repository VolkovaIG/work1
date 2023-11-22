# import math
import math
from math import pi
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, unique


# class Point(ABC):
    # color = None
# @unique
# class COLOR(Enum):
#     'желтый' = 1
#     'красные' = 2



class Figure(ABC):
    classname = None

    @abstractmethod
    def __init__(self, name=None):
        self.name = name
        self._x = 0
        self._y = 0
        self.__color = ''
        self._area = ()
    @property   #getter
    def x(self):
        return self._x
    @property  # getter
    def y(self):
        return self._y

    @property  # getter
    def color(self):
        return self._color


    @x.setter   #setter
    def x(self, value):
        return value

    @y.setter  # setter
    def y(self, value):
        return value

    @y.setter  # setter
    def color(self, value):
        return value

    def __str__(self):
        return f'{self.x}, {self.y}, {self.color}'




class Circle(Figure):
    classname = 'Круг'

    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self._r = r

    def __str__(self):
        return f'x = {self._x}, y = {self._y}, r = {self._r}, color: {self._color}'

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    def area(self):
        return math.pi * self._r ** 2
