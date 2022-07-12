= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Wild Cat Zoo
= = = = = = = = = = = = = = = = = = = = = = = = =
#animal.py
class Animal:
    def __init__(self, name, gender, age, money_for_care):
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

#lion.py
class Lion(Animal):
    MONEY_FOR_CARE = 50
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.MONEY_FOR_CARE)

#tiger.py
class Tiger(Animal):
    MONEY_FOR_CARE = 45
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.MONEY_FOR_CARE)

#cheetah.py
class Cheetah(Animal):
    MONEY_FOR_CARE = 60
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.MONEY_FOR_CARE)

#worker.py
class Worker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'

#keeper.py
class Keeper(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

#caretaker.py
class Caretaker(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

#vet.py
class Vet(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)

#zoo.py
class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        if self.__animal_capacity > len(self.animals):
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        all_salaries = 0
        for worker in self.workers:
            all_salaries += worker.salary
        if self.__budget >= all_salaries:
            self.__budget -= all_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        all_cares = 0
        for animal in self.animals:
            all_cares += animal.money_for_care
        if self.__budget >= all_cares:
            self.__budget -= all_cares
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals'
        lions = list()
        tigers = list()
        cheetahs = list()
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)
        result += f'\n----- {len(lions)} Lions:'
        for lion in lions:
            result += f'\n{lion}'
        result += f'\n----- {len(tigers)} Tigers:'
        for tiger in tigers:
            result += f'\n{tiger}'
        result += f'\n----- {len(cheetahs)} Cheetahs:'
        for cheetah in cheetahs:
            result += f'\n{cheetah}'
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers'
        keepers = list()
        caretakers = list()
        vets = list()
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)
        result += f'\n----- {len(keepers)} Keepers:'
        for keeper in keepers:
            result += f'\n{keeper}'
        result += f'\n----- {len(caretakers)} Caretakers:'
        for caretaker in caretakers:
            result += f'\n{caretaker}'
        result += f'\n----- {len(vets)} Vets:'
        for vet in vets:
            result += f'\n{vet}'
        return result

zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    print(zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    print(zoo.hire_worker(worker))

# Tending animals
print(zoo.tend_animals())

# Paying keepers
print(zoo.pay_workers())

# Fireing worker
print(zoo.fire_worker("Adam"))

# Printing statuses
print(zoo.animals_status())
print(zoo.workers_status())

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Pizza Maker
= = = = = = = = = = = = = = = = = = = = = = = = =
#topping.py
class Topping:
    def __init__(self, topping_type, weight):
        self.topping_type = topping_type
        self.weight = weight

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        if not value:
            raise ValueError('The topping type cannot be an empty string')
        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('The weight cannot be less or equal to zero')
        self.__weight = value

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
#dough.py
class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        if not value:
            raise ValueError('The flour type cannot be an empty string')
        self.__flour_type = value

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if not value:
            raise ValueError('The baking technique cannot be an empty string')
        self.__baking_technique = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError('The weight cannot be less or equal to zero')
        self.__weight = value

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - =
#pizza.py
class Pizza:
    def __init__(self, name, dough, toppings_capacity):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = dict()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('The name cannot be an empty string')
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError('You should add dough to the pizza')
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = value

    def add_topping(self, topping):
        if self.toppings_capacity > len(self.toppings):
            if topping.topping_type not in self.toppings:
                self.toppings[topping.topping_type] = 0
            self.toppings[topping.topping_type] += topping.weight
        else:
            raise ValueError('Not enough space for another topping')

    def calculate_total_weight(self):
        total_weight = 0
        total_weight += self.dough.weight
        for key, value in self.toppings.items():
            total_weight += value
        return total_weight

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -
tomato_topping = Topping("Tomato", 60)
print(tomato_topping.topping_type)
print(tomato_topping.weight)

mushrooms_topping = Topping("Mushroom", 75)
print(mushrooms_topping.topping_type)
print(mushrooms_topping.weight)

mozzarella_topping = Topping("Mozzarella", 80)
print(mozzarella_topping.topping_type)
print(mozzarella_topping.weight)

cheddar_topping = Topping("Cheddar", 150)

pepperoni_topping = Topping("Pepperoni", 120)

white_flour_dough = Dough("White Flour", "Mixing", 200)
print(white_flour_dough.flour_type)
print(white_flour_dough.weight)
print(white_flour_dough.baking_technique)

whole_wheat_dough = Dough("Whole Wheat Flour", "Mixing", 200)
print(whole_wheat_dough.weight)
print(whole_wheat_dough.flour_type)
print(whole_wheat_dough.baking_technique)

p = Pizza("Margherita", whole_wheat_dough, 2)

p.add_topping(tomato_topping)
print(p.calculate_total_weight())

p.add_topping(mozzarella_topping)
print(p.calculate_total_weight())

p.add_topping(mozzarella_topping)

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Football Team Generator
= = = = = = = = = = = = = = = = = = = = = = = = =
#player.py
class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        result = f'Player: {self.name}' + \
                 f'\nSprint: {self.__sprint}' + \
                 f'\nDribble: {self.__dribble}' + \
                 f'\nPassing: {self.__passing}' + \
                 f'\nShooting: {self.__shooting}'
        return result

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -
#team.py
class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = list()

    def add_player(self, player):
        if player in self.__players:
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name):
        for player in self.__players:
            if player.name == player_name:
                temp = player
                self.__players.remove(player)
                return temp
        return f'Player {player_name} not found'

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -
p = Player("Pall", 1, 3, 5, 7)

print("Player name:", p.name)
print("Points sprint:", p._Player__sprint)
print("Points dribble:", p._Player__dribble)
print("Points passing:", p._Player__passing)
print("Points shooting:", p._Player__shooting)

print("\ncalling the __str__ method")
print(p)

print("\nAbout the team")
t = Team("Best", 10)
print("Team name:", t._Team__name)
print("Teams points:", t._Team__rating)
print("Teams players:", len(t._Team__players))
print(t.add_player(p))
print(t.add_player(p))
print("Teams players:", len(t._Team__players))
print(t.remove_player("Pall"))
print(t.remove_player("Pall"))

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Restaurant
= = = = = = = = = = = = = = = = = = = = = = = = =
#product.py
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

#beverage.py
class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self):
        return self.__milliliters

#hot_beverage.py
class HotBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

#cold_beverage.py
class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

#coffee.py
class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    def __init__(self, name, caffeine):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

#tea.py
class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

#food.py
class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self):
        return self.__grams

#starter.py
class Starter(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

#main_dish.py
class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

#dessert.py
class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self):
        return self.__calories

#salmon.py
class Salmon(MainDish):
    GRAMS = 22
    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS)

#soup.py
class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

#cake.py
class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5
    def __init__(self, name):
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)

# - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -
product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
print('= = = = = = = = = = = = = = = = = = = = = =')
p2 = Coffee("Kafe", 350)
print(p2.__class__.__name__)
print(p2.name)
print(p2.price)
print(p2.milliliters)
print('= = = = = = = = = = = = = = = = = = = = = =')
tea1 = Tea('tea1', 25, 100)
print(tea1.__class__.__name__)
print(tea1.__class__.__bases__[0].__name__)
print(tea1.name)
print(tea1.price)
print(tea1.milliliters)
print('= = = = = = = = = = = = = = = = = = = = = =')
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
print('= = = = = = = = = = = = = = = = = = = = = =')
= = = = = = = = = = = = = = = = = = = = = = = = = 