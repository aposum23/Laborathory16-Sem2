#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Man:

    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def sex(self):
        return self.__sex

    @property
    def weight(self):
        return self.__weight

    @name.setter
    def name(self, value):
        self.__name = value

    @age.setter
    def age(self, value):
        self.__age = value

    @sex.setter
    def sex(self, value):
        self.__sex = value

    @weight.setter
    def weight(self, value):
        self.__weight = value

    def set_name(self, name):
        self.name = name

    def set_weight(self, weight):
        self.weight = weight

    def set_age(self, age):
        self.age = age

    def display(self):
        print()
        print(f"Имя: {self.name}")
        print(f"Пол: {self.sex}")
        print(f"Возраст: {self.age}")
        print(f"Вес: {self.weight}")


class Student(Man):

    def __init__(self, name, age, sex, weight, grade):
        super().__init__(name, age, sex, weight)
        self.grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = value

    def set_grade(self, value):
        self.grade = value

    def increase_grade(self):
        self.grade += 1

    def display(self):
        super(Student, self).display()
        print(f"Год обучения: {self.grade}")


if __name__ == "__main__":
    m1 = Man(
        name="Ibragim",
        age=16,
        sex='Male',
        weight=62
    )
    m1.display()
    m1.set_age(17)
    m1.display()

    m2 = Student(
        name="Vladimir",
        age=18,
        sex="Male",
        weight=75,
        grade=2
    )
    m2.display()
    m2.increase_grade()
    m2.set_name("Dima")
    m2.set_age(19)
    m2.display()
