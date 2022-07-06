Classes and Objects - 01.07

= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Vet
= = = = = = = = = = = = = = = = = = = = = = = = =
class Vet:
    animals = list()
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = list()

    def register_animal(self, animal_name):
        if len(Vet.animals) >= Vet.space:
            return f'Not enough space'
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name):
        if animal_name not in self.animals:
            return f'{animal_name} not in the clinic'
        self.animals.remove(animal_name)
        Vet.animals.remove(animal_name)
        return f'{animal_name} unregistered successfully'

    def info(self):
        return f'{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic'

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Time
= = = = = = = = = = = = = = = = = = = = = = = = =
class Time():
    max_hours = 23
    max_minutes = 59
    max_seconds = 59
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0
        return self.get_time()
        
time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())

= = = = = = = = = = = = = = = = = = = = = = = = =
03. Account
= = = = = = = = = = = = = = = = = = = = = = = = =
class Account:
    def __init__(self, id, name, balance=0):
        self.id = id
        self.name = name
        self.balance = balance
    
    def credit(self, amount):
        self.balance += amount
        return self.balance
    
    def debit(self, amount):
        if amount > self.balance:
            return f'Amount exceeded balance'
        self.balance -= amount
        return self.balance

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'

print(f'- = - = - = - = - = - = - = - = - = - = - = - = ')
account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
print(f'- = - = - = - = - = - = - = - = - = - = - = - = ')
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
print(f'- = - = - = - = - = - = - = - = - = - = - = - = ')

= = = = = = = = = = = = = = = = = = = = = = = = =
04. Pizza Delivery
= = = = = = = = = = = = = = = = = = = = = = = = =
class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += (quantity * price_per_quantity)

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        elif self.ingredients[ingredient] < quantity:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= (quantity * price_per_quantity)

    def make_order(self):
        self.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])} and the price will be {self.price}lv."

margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

= = = = = = = = = = = = = = = = = = = = = = = = =
05. To-do List
= = = = = = = = = = = = = = = = = = = = = = = = =
#- - - - - - 
#section.py
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task):
        if new_task in self.tasks :
            return f'Task is already in the section {self.name}'
        self.tasks.append(new_task)
        return f'Task {new_task.details()} is added to the section'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task.name}'
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t.completed]
        return f'Cleared {initial_count - len(self.tasks)} tasks.'

    def view_section(self):
        result = ''
        result += f'Section {self.name}:'
        for task in self.tasks:
            result += f'\n{task.details()}'
        return result

#- - - - - - 
#task.py
class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = list()
        self.completed = False

    def change_name(self, new_name: str):
        if self.name == new_name:
            return 'Name cannot be the same.'
        self.name = new_name
        return f'{self.name}'

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return 'Date cannot be the same.'
        self.due_date = new_date
        return f'{self.due_date}'

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if len(self.comments) <= comment_number < 0:
            return 'Cannot find comment.'
        self.comments[comment_number] = new_comment
        return f'{", ".join(self.comments)}'

    def details(self):
        return f'Name: {self.name} - Due Date: {self.due_date}'

#- - - - - - - - - - - - - - -
#__init__.py

task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())

= = = = = = = = = = = = = = = = = = = = = = = = =
06. Guild System
= = = = = = = = = = = = = = = = = = = = = = = = =
# - - - - - - - - - - - - - - player.py - - - - - - - - - - - - - -
class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = dict()
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return 'Skill already added'
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        result = ''
        result += f'Name: {self.name}\n'
        result += f'Guild: {self.guild}\n'
        result += f'HP: {self.hp}\n'
        result += f'MP: {self.mp}\n'
        for key, value in self.skills.items():
            result += f'==={key} - {value}\n'
        return result.strip()

# - - - - - - - - - - - - - - guild.py - - - - - - - - - - - - - -
class Guild:
    def __init__(self, name):
        self.name = name
        self.players = list()

    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'
        if player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'
        player.guild = self.name
        self.players.append(player)
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name: str):
        if player in self.players:
            if player.name == player_name:
                player.guild = 'Unaffiliated'
                self.players.remove(player)
                return f'Player {player.name} has been removed from the guild.'
        return f'Player {player.name} is not in the guild.'

    def guild_info(self):
        result = ''
        result += f'Guild: {self.name}\n'
        for player in self.players:
            result += player.player_info() + '\n'
        return result.strip()

# - - - - - - - - - - - - - - main.py - - - - - - - - - - - - - -
player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

= = = = = = = = = = = = = = = = = = = = = = = = =
07. Spoopify
= = = = = = = = = = = = = = = = = = = = = = = = =
#song.py
class Song:
    def __init__(self, name, length, single):
        self.name = name
        self.length = length
        self.single = single

    def get_info(self):
        return f'{self.name} - {self.length}'

#album.py
class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song in self.songs:
            return f'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f'Removed song {song_name} from album {self.name}.'
        return f'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        result = ''
        result += f'Album {self.name}'
        for song in self.songs:
            result += f'\n== {song.get_info()}'
        return result

#band.py
class Band:
    def __init__(self, name):
        self.name = name
        self.albums = list()

    def add_album(self, album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name):
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return f'Album has been published. It cannot be removed.'
                self.albums.remove(album)
                return f'Album {album_name} has been removed.'
        return f'Album {album_name} is not found.'

    def details(self):
        result = f'Band {self.name}\n'
        for album in self.albums:
            result += album.details() + '\n'
        return result.strip()

#__init__.py
song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

= = = = = = = = = = = = = = = = = = = = = = = = =
08. Library
= = = = = = = = = = = = = = = = = = = = = = = = =

= = = = = = = = = = = = = = = = = = = = = = = = =