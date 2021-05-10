# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class


class Animals:
    """
    Parent class, should have eat, sleep
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.__class__.__name__} is eating")

    def sleep(self):
        print(f"{self.__class__.__name__} is sleeping")


class Cat(Animals):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """
    def purr(self):
        print(f"{self.name} says: Purr")

    def scratch(self):
        print(f"{self.name} is scratching")


class Dog(Animals):
    def bark(self):
        print(f"{self.name} says: Bark")

    def dig(self):
        print(f"{self.name} is digging")


class Bird(Animals):
    def tweet(self):
        print(f"{self.name} says: Tweet")

    def fly(self):
        print(f"{self.name} is flying")


class Mouse(Animals):
    def squeak(self):
        print(f"{self.name} says: Squeak")

    def hide(self):
        print(f"{self.name} is hiding")


class Panther(Animals):
    def roar(self):
        print(f"{self.name} says: Roar")

    def hunt(self):
        print(f"{self.name} is hunting")


tom = Cat("Tom")
sirius = Dog("Sirius")
tweety = Bird("Tweety")
jerry = Mouse("Jerry")
bagheera = Panther("Bagheera")

tom.eat()
tom.sleep()
tom.purr()
tom.scratch()
print(isinstance(tom, Animals))

sirius.eat()
sirius.sleep()
sirius.bark()
sirius.dig()
print(isinstance(sirius, Animals))

tweety.tweet()
tweety.fly()
print(isinstance(tweety, Animals))

jerry.squeak()
jerry.hide()
print(isinstance(jerry, Animals))

bagheera.roar()
bagheera.hunt()
print(isinstance(bagheera, Animals))


# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    """
    Human class, should have eat, sleep, study, work
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def study(self):
        print(f"{self.name} is studying")

    def work(self):
        print(f"{self.name} is working")


class Centaur(Human, Animals):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
    def gallop(self):
        print(f"{self.name} is galloping")


oreius = Centaur("Oreius")
oreius.eat()
oreius.study()
oreius.gallop()


# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.
class Person:
    """
    Make the class with composition.
    """
    def __init__(self):
        arm1 = Arm('Right arm')
        arm2 = Arm('Left arm')
        self.arms = [arm1, arm2]


class Arm:
    """
    Make the class with composition.
    """
    def __init__(self, name):
        self.name = name


person = Person()
for arm in person.arms:
    print(arm.name)

# b.


class CellPhone:
    """
    Make the class with aggregation
    """
    def __init__(self, screen):
        self.screen = screen


class Screen:
    """
    Make the class with aggregation
    """
    def __init__(self, screen_type):
        self.screen_type = screen_type


screen1 = Screen("Touchscreen")
smartphone = CellPhone(screen1)
print(screen1.screen_type)
print(smartphone.screen.screen_type)


# 3.
class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.params = [name, last_name, phone_number, address, email, birthday, age, sex]

    def __str__(self):
        return str(self.params)


user = Profile('Jacob', 'McKenzie', '0335557799', 'Endless Summer Str.', 'jacob.l@mail.com', '09.02.1991', '30', 'male')
print(user)

# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def webcam(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def ports(self):
        raise NotImplementedError("Your method is not implemented")

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError("Your method is not implemented")


class HPLaptop(Laptop):
    def __init__(self, screen_laptop, keyboard_laptop, touchpad_laptop, webcam_laptop, ports_laptop, dynamics_laptop):
        self.screen_laptop = screen_laptop
        self.keyboard_laptop = keyboard_laptop
        self.touchpad_laptop = touchpad_laptop
        self.webcam_laptop = webcam_laptop
        self.ports_laptop = ports_laptop
        self.dynamics_laptop = dynamics_laptop

    def screen(self):
        print(f"{self.__class__.__name__} has {self.screen_laptop} screen")

    def keyboard(self):
        print(f"{self.__class__.__name__} has {self.keyboard_laptop} keyboard")

    def touchpad(self):
        print(f"{self.__class__.__name__} has {self.touchpad_laptop} touchpad")

    def webcam(self):
        print(f"{self.__class__.__name__} has {self.webcam_laptop} webcam")

    def ports(self):
        print(f"{self.__class__.__name__} has {self.ports_laptop} ports")

    def dynamics(self):
        print(f"{self.__class__.__name__} has {self.dynamics_laptop} dynamics")


laptop = HPLaptop('IPS', 'Gaming key', 'Multi-Touch', 'HD 720p 1280x720', 'HDMI, USB', 'Bang & Olufsen')

laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()
