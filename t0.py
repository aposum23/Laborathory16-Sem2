#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint


class Unit:
    __number = 0

    def __init__(self, team):
        self.__identifier = self.__number
        self.team = team
        self.__class__.__number += 1

    @property
    def identifier(self):
        return self.__identifier

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        self.__team = value


class Hero(Unit):

    def __init__(self, team):
        super().__init__(team)
        self.level = 0

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    def increment_level(self):
        self.level += 1

    def display(self):
        print(f"Команда: {self.team}")
        print(f"ID: {self.identifier}")
        print(f"Уровень: {self.level}")


class Solider(Unit):

    def __init__(self, team):
        super().__init__(team)
        self.follows = False
        self.hero_id = -1

    def start_following(self, hero):
        if isinstance(hero, Hero):
            self.follows = True
            self.hero_id = hero.identifier
        else:
            raise ValueError

    @property
    def follows(self):
        return self.__follows

    @property
    def hero_id(self):
        return self.__hero_id

    @follows.setter
    def follows(self, value):
        self.__follows = value

    @hero_id.setter
    def hero_id(self, value):
        self.__hero_id = value

    def display(self):
        print(f"Команда: {self.team}")
        print(f"ID: {self.identifier}")
        print(f"Следует за героем: {self.follows}")
        if self.follows:
            print(f"ID героя: {self.hero_id}")


if __name__ == '__main__':
    h1 = Hero(1)
    h2 = Hero(2)
    team1 = []
    team2 = []
    for i in range(10):
        probability = randint(1, 2)
        if probability == 1:
            team1.append(Solider(1))
        else:
            team2.append(Solider(2))
    if len(team1) > len(team2):
        h1.increment_level()
    else:
        h2.increment_level()
    rand_unit = randint(0, len(team1) - 1)
    team1[rand_unit].start_following(h1)
    print("Герой №1:")
    h1.display()
    print("\nГерой №2:")
    h2.display()
    print("\nСолдат команды №2:")
    team2[0].display()
    print("\nСолдат, следующий за героем №1:")
    team1[rand_unit].display()
