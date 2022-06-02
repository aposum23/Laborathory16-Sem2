#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import sqrt
from abc import ABC, abstractmethod


class Function(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate(self, x):
        pass

    def display(self, x):
        print(f"Вычисленное значение: {self.calculate(x)}")


class Ellipse(Function):

    def __init__(self, a, b):
        if a == 0 or b == 0:
            raise ValueError
        if a < b:
            raise ValueError
        self.__a = a
        self.__b = b

    def calculate(self, x):
        temp = (x ** 2) / (self.__a ** 2)
        y = sqrt((1 - temp) * (self.__b ** 2))
        return y


class Hyperbola(Function):

    def __init__(self, a, b):
        if a == 0 or b == 0:
            raise ValueError
        self.__a = a
        self.__b = b

    def calculate(self, x):
        temp = (x ** 2) / (self.__a ** 2)
        y = sqrt((1 + temp) * (self.__b ** 2))
        return y


if __name__ == '__main__':
    el = Ellipse(4, 2)
    print("Эллипс")
    print("Значение в точке x = 3: ")
    el.display(3)
    print()
    print("Гипербола")
    print("Значение в точке x = 2.5: ")
    hy = Hyperbola(1, 2)
    hy.display(2.5)
