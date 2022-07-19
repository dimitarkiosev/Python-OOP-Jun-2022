#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Vehicle
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if (self.fuel_consumption + 0.9) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + 0.9) * distance
        return

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        if (self.fuel_consumption + 1.6) * distance <= self.fuel_quantity:
            self.fuel_quantity -= (self.fuel_consumption + 1.6) * distance
        return

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
        return


print(' = = = = = = = = = = = = = = = = = = = = = = =')
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
print(' = = = = = = = = = = = = = = = = = = = = = = =')
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
print(' = = = = = = = = = = = = = = = = = = = = = = =')

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Groups
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        return Person(self.name, other.surname)

class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        name = f'{self.name} {other.name}'
        people = self.people + other.people
        return Group(name, people)

    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(p) for p in self.people])}"

    def __getitem__(self, idx):
        return f'Person {idx}: {str(self.people[idx])}'

p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Account
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = list()

    @staticmethod
    def validate_transaction(account, amount_to_add: int):
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount_to_add)
        return f'New balance: {account.balance}'

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __reversed__(self):
        return reversed(self._transactions)

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __getitem__(self, idx):
        return self._transactions[idx]

    def __add__(self, other):
        name = f'{self.owner}&{other.owner}'
        amount = self.amount + other.amount
        temp_acc = Account(name, amount)

        [temp_acc.add_transaction(t) for t in self]
        [temp_acc.add_transaction(t) for t in other]
        return temp_acc

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
# = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -
# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Wild Farm - от 35 минута започва
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#food.py
from abc import ABC, abstractmethod

class Food(ABC):
    def __init__(self, quantity: int):
        self.quantity = quantity

class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)

#animal.py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten = 0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


#birds.py
class Owl(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten=0)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super().__init__(name, weight, wing_size, food_eaten=0)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food: Food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity


#mammals.py
class Mouse(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Fruit' and food.__class__.__name__ != 'Vegetable':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * 0.10
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return 'Meow'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat' and food.__class__.__name__ != 'Vegetable':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super().__init__(name, weight, living_region, food_eaten=0)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food: Food):
        if food.__class__.__name__ != 'Meat':
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.weight += food.quantity * 1.00
        self.food_eaten += food.quantity


print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =')
owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =')
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =')
    




#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#05. Animals
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#animal.py
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f'This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}'

#dog.py
class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Woof!'

#cat.py
class Cat(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow meow!'

#tomcat.py
class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')

    def make_sound(self):
        return 'Hiss'

#kitten.py
class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')

    def make_sound(self):
        return 'Meow'

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
dog = Dog("Rocky", 3, "Male")
print(dog.make_sound())
print(dog)
tomcat = Tomcat("Tom", 6)
print(tomcat.make_sound())
print(tomcat)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
#= = = = = = = = = = = = = = = = = = = = = = = = = = =