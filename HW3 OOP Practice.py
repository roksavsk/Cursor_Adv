# There is a Person whose characteristics are:
# 1. Name
# 2. Age
# 3. Availability of money
# 4. Having your own home
#
# Human can:
# 1. Provide information about yourself
# 2. Make money
# 3. Buy a house
#
# There is also a House, the properties of which include:
# 1. Area
# 2. Cost
#
# For Home you can:
# 1. Apply a purchase discount
#
# e.g.: There is also a Small Typical House with a required area of 40m2.
#
# *Realtor:
# 1. Name
# 2. Houses
# 3. Discount that he/she can give you.
#
# *There is only one realtor who handles small houses you wanna buy. (Singleton)
# Realtor is only one in your city and can:
# 1. Provide information about all the Houses
# 2. Give a discount
# 3. Steal your money with 10% chance

from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, money_avail, own_home=False):
        self.name = name
        self.age = age
        self.money_avail = money_avail
        self.own_home = own_home

    def info(self):
        print(f'Hi, my name is {self.name}. I am {self.age} years old. I have {self.money_avail} money.')

    def make_money(self):
        self.money_avail += random.randint(5000, 50000)
        print(f'{self.name} received payment and now has {self.money_avail} money.')

    def buy_house(self, house):
        if self.money_avail > house.cost:
            self.money_avail -= house.cost
            print(f'Congratulations! You just bought a house!')
            self.own_home = True
        else:
            print(f"Sorry, you don't have enough money.")


class House(ABC):
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    @abstractmethod
    def apply_discount(self):
        raise NotImplementedError


class Home(House):
    def __init__(self, area, cost):
        super().__init__(area, cost)

    def apply_discount(self, realtor):
        self.cost -= int(self.cost * realtor.discount/100)
        print(f"Discount was applied to house cost and now it costs {self.cost}.")


class SmallTypicalHouse(Home):
    def __init__(self, cost, area=40):
        super().__init__(area, cost)


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, houses: list, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info(self):
        print(f"Hi, my name is {self.name}. I'm realtor and have {len(self.houses)} houses to sell and can give {self.discount}% discount. I can offer you such options:")
        for house in self.houses:
            print(f"This house has {house.area} area and costs {house.cost}.")

    def give_discount(self):
        self.discount += random.randint(5, 50)
        print(f"Realtor agreed to give you {self.discount}% discount.")

    def steal_money(self, person, house):
        if random.randint(1, 10) == 10:
            person.money_avail -= house.cost
            print(f"Oh no, realtor stole your money.")
        else:
            print(f"You're lucky, realtor {self.name} was a good man, so you've made a great deal and now own a house.")


if __name__ == '__main__':
    person1 = Person('Percival', 25, 1000)
    house1 = Home(70, 30000)
    house2 = SmallTypicalHouse(15000)
    house3 = Home(50, 25000)
    realtor1 = Realtor('Lancelot', [house1, house2, house3], 3)
    person1.info()
    person1.make_money()
    realtor1.provide_info()
    realtor1.give_discount()
    house1.apply_discount(realtor1)
    person1.buy_house(house1)
    realtor1.steal_money(person1, house1)

