Inheritance
    - the super() method
    
    The 4 Basics Concepts of OOP
      *Inheritance
      *Encapsulation
      *Abstraction
      *Polymorphism
  
Forms of Inheritance
    - single
    - multiple
    - multilevel
    - hierarchical
Mixins
= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Food
= = = = = = = = = = = = = = = = = = = = = = = = =
# food.py
class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date 

#fruit.py        
class Fruit(Food):
    def __init__(self, name, expiration_date):
        super().__init__(expiration_date)
        self.name = name

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Single Inheritance
= = = = = = = = = = = = = = = = = = = = = = = = =
# animal.py
class Animal:
    def eat(self):
        return 'eating ...'

# dog.py
from project.animal import Animal

class Dog(Animal):
    def bark(self):
        return 'barking...'
= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Multiple Inheritance
= = = = = = = = = = = = = = = = = = = = = = = = =
#person.py - - - - - - - - - - - - - - - - - -
class Person:
    def sleep(self):
        return 'sleeping...'

#employee.py - - - - - - - - - - - - - - - - - -
class Employee:
    def get_fired(self):
        return 'fired...'

#teach - - - - - - - - - - - - - - - - - - - - -
from project.person import Person
from project.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Multilevel Inheritance
= = = = = = = = = = = = = = = = = = = = = = = = =
# vehicle.py - - - - - - - - - - - - - - - - - - 
class Vehicle:
    def move(self):
        return 'moving...'
        
#car.py - - - - - - - - - - - - - - - - - - - -
from project.venicle import Vehicle

class Car(Vehicle):
    def drive(self):
        return 'driving...'
        
#sports_car.py - - - - - - - - - - - - - - - - -
from project.car import Car

class SportsCar(Car):
    def race(self):
        return 'racing...'


= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Hierarchical Inheritance
= = = = = = = = = = = = = = = = = = = = = = = = =
# animal.py - - - - - - - - - - - - - - - - - - -
class Animal:
    def eat(self):
        return 'eating ...'

# dog.py - - - - - - - - - - - - - - - - - - - -
from project.animal import Animal

class Dog(Animal):
    def bark(self):
        return 'barking...'
        
# cat.py - - - - - - - - - - - - - - - - - - - -
from project.animal import Animal

class Cat(Animal):
    def meow(self):
        return 'meowing...'
= = = = = = = = = = = = = = = = = = = = = = = = = 
06. Stack of Strings
= = = = = = = = = = = = = = = = = = = = = = = = =
class Stack:
    def __init__(self):
        self.data = list()
        
    def push(self, value):
        self.data.append(value)
        
    def pop(self):
        return self.data.pop()
        
    def top(self):
        return self.data[-1]
        
    def is_empty(self):
        return len(self.data) == 0
        
    def __repr__(self):
        return f"[{', '.join(reversed(self.data))}]"
= = = = = = = = = = = = = = = = = = = = = = = = = 