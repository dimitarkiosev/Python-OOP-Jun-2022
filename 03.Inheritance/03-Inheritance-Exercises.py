= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Person
= = = = = = = = = = = = = = = = = = = = = = = = =
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
print(child.name)
print(child.age)

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Zoo
= = = = = = = = = = = = = = = = = = = = = = = = =
#animal.py - - - - - -
class Animal:
    def __init__(self, name):
        self.name = name

#mammal.py - - - - - -
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

#reptile.py - - - - - -
class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
    
#bear.py - - - - - -
class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
#gorilla.py - - - - - -
class Gorilla(Mammal):
    def __init__(self, name):
        super().__init__(name)
    
#lizard.py - - - - - -
class Lizard(Reptile):
    def __init__(self, name):
        super().__init__(name)

#snake.py - - - - - -
class Snake(Reptile):
    def __init__(self, name):
        super().__init__(name)
    
#main.py - - - - - -
mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Players and Monsters
= = = = = = = = = = = = = = = = = = = = = = = = =
# hero.py - - - - - - - - - - -
class Hero:
    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level
    def __str__(self):
        return f'{self.username} of type {self.__class__.__name__} has level {self.level}'

# elf.py - - - - - - - - - - -
class Elf(Hero):
    pass

# wizard.py - - - - - - - - - - -
class Wizard(Hero):
    pass

# knight.py - - - - - - - - - - -
class Knight(Hero):
    pass

# muse_elf.py
class MuseElf(Elf):
    pass

# dark_wizard.py - - - - - - - - - - -
class DarkWizard(Wizard):
    pass

# soul_master.py - - - - - - - - - - -
class SoulMaster(DarkWizard):
    pass

# dark_knight.py - - - - - - - - - - -
class DarkKnight(Knight):
    pass

# blade_knight.py - - - - - - - - - - -
class BladeKnight(DarkKnight):
    pass

# main.py - - - - - - - - - - -
hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Need for speed
= = = = = = = = = = = = = = = = = = = = = = = = =
# vehicle.py
class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25
    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        needed_fuel = kilometers * self.fuel_consumption
        if self.fuel >= needed_fuel:
            self.fuel -= needed_fuel

# motorcycle.py
class Motorcycle(Vehicle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

# race_motorcycle.py
class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

# cross_motorcycle.py
class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

# car.py
class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

# family_car.py
class FamilyCar(Car):
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

# sport_car.py
class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10
    def __init__(self, fuel: float, horse_power: int):
        super().__init__(fuel, horse_power)

#main.py
vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(FamilyCar.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Shop
= = = = = = = = = = = = = = = = = = = = = = = = =
#product.py
class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int):
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return f'{self.name}'

#drink.py
class Drink(Product):
    def __init__(self, name: str):
        super().__init__(name, 10)

#food.py
class Food(Product):
    def __init__(self, name: str):
        super().__init__(name, 15)

#product_repository.py
class ProductRepository:
    def __init__(self):
        self.products = list()

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f'{product.name}: {product.quantity}' + '\n'
        return result.strip()

#main.py
food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

= = = = = = = = = = = = = = = = = = = = = = = = =