= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Shop
= = = = = = = = = = = = = = = = = = = = = = = = =
class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)

shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Hero
= = = = = = = = = = = = = = = = = = = = = = = = =
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            return f'{self.name} was defeated'

    def heal(self, amount):
        self.health += amount

hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))

= = = = = = = = = = = = = = = = = = = = = = = = =
03. Employee
= = = = = = = = = = = = = = = = = = = = = = = = =
class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_annual_salary(self):
        return 12 * self.salary

    def raise_salary(self, amount):
        self.salary += amount
        return self.salary

employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

= = = = = = = = = = = = = = = = = = = = = = = = =
04. Cup
= = = = = = = = = = = = = = = = = = = = = = = = =
class Cup():
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, volume):
        if self.status() >= volume:
            self.quantity += volume

cup = Cup(100, 50)
print(cup.status())
cup.fill(50)
cup.fill(20)
print(cup.status())

= = = = = = = = = = = = = = = = = = = = = = = = =
05. Flower
= = = = = = = = = = = = = = = = = = = = = = = = =
class Flower:
    def __init__(self, name, water_requirements):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity):
        self.is_happy = self.water_requirements <= quantity

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        return f'{self.name} is not happy'

flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
        
= = = = = = = = = = = = = = = = = = = = = = = = =
06. Steam User
= = = = = = = = = = = = = = = = = = = = = = = = =
class SteamUser:
    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return f'{self.username} is playing {game}'
        else:
            return f'{game} is not in library'

    def buy_game(self, game):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        else:
            return f'{game} is already in your library'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())

= = = = = = = = = = = = = = = = = = = = = = = = =
07. Programmer
= = = = = = = = = = = = = = = = = = = = = = = = =
class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language != language:
            return f'{self.name} does not know {language}'
        self.skills += skills_earned
        return f'{self.name} watched {course_name}'

    def change_language(self, new_language, skills_needed):
        if self.skills < skills_needed:
            return f'{self.name} needs {skills_needed - self.skills} more skills'
        if new_language == self.language:
            return f'{self.name} already knows {self.language}'
        previous_language = self.language
        self.language = new_language
        return f'{self.name} switched from {previous_language} to {new_language}'

programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))

= = = = = = = = = = = = = = = = = = = = = = = = =
08. Pokemon Battle
= = = = = = = = = = = = = = = = = = = = = = = = =

= = = = = = = = = = = = = = = = = = = = = = = = =
