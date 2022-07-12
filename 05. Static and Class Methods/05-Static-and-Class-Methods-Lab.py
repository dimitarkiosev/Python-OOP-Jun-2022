Class and Static Methods
1. Methods and Decorators

2. Static Methods - могат да съществуват като самостоятелни функции в класа, без да
се обвързва с класа
    @staticmethod
    
3. Class Methods - да променят неща в класа, но предимно се използват за контролирани
инстанции на класа
    @classmethod
    def method_name(cls):
        cls.var_name = 'value'

4. Overriding Using Class Methods

https://judge.softuni.org/Contests/Practice/Index/2430
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#01. Calculator
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Calculator:
    def __init__(self):
        pass
        
    @staticmethod
    def add(*args):
        result = 0
        for each in args:
            result += each
        return result
    
    @staticmethod
    def subtract(*args):
        result = args[0]
        for each in args[1:]:
            result -= each
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for each in args:
            result *= each
        return result
    
    @staticmethod
    def divide(*args):
        result = args[0]
        for each in args[1:]:
            result = result / each
        return result
        
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
#- = - = - = - = - = - = - = - = - = - = - = - =
#- = Инес ни показа reduce = - = - = - = - = - =
#- = - = - = - = - = - = - = - = - = - = - = - =
from functools import reduce

class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x+y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x-y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x*y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x/y, args)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Shop
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if self.capacity > sum(self.items.values()):
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            return f'{item_name} added to the shop'
        return 'Not enough capacity in the shop'

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                self.items.pop(item_name)
            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'

fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Integer
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return cls(int_val)

    @classmethod
    def from_string(cls, value):
        try:
            if not isinstance(value, str):
                raise ValueError
            return cls(int(value))
        except ValueError:
            return 'wrong type'

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Hotel Rooms
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#hotel.py
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = list()

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        result = f'Hotel {self.name} has {self.guests} total guests\n'
        result += f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
        return result

#room.py
class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.guests += people
            self.is_taken = True
            return
        return f'Room number {self.number} cannot be taken'

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
            return
        return f'Room number {self.number} is not taken'

hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
#= = = = = = = = = = = = = = = = = = = = = = = = = = =