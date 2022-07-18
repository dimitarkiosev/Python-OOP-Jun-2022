#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Photo Album
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
import math

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = list()
        for i in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for row, page in enumerate(self.photos):
            if len(page) < PhotoAlbum.PHOTOS_PER_PAGE:
                page.append(label)
                return f'{label} photo added successfully on page {row + 1} slot {len(page)}'
        return 'No more free slots'

    def display(self):
        result = '-----------\n'
        for page in self.photos:
            result += f"{' '.join(['[]' for _ in page])}\n"
            result += '-----------\n'
        return result.strip()

#- - - - - - - - - - - - - - - - - - -
album = PhotoAlbum(3)

print(album.add_photo("baby"))
print(album.photos)
print(album.add_photo("first grade"))
print(album.photos)
print(album.add_photo("eight grade"))
print(album.photos)
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.photos)
print(album.add_photo("wedding"))
print(album.photos)
print(album.add_photo("wedding2"))
print(album.add_photo("wedding3"))
print(album.add_photo("wedding4"))
print(album.display())
        
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Movie World
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#customer.py
class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = list()

    def __repr__(self):
        rented_dvd_names = ', '.join([d.name for d in self.rented_dvds])
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({rented_dvd_names})"

#dvd.py
class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        c_year = int(date.split('.')[2])
        temp_month = int(date.split('.')[1])
        month_to_int = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }
        c_month = month_to_int[temp_month]
        return cls(name, id, c_year, c_month, age_restriction)

    def __repr__(self):
        status = 'not rented'
        if self.is_rented:
            status = 'rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}'

#movie_world.py
class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name):
        self.name = name
        self.customers = list()
        self.dvds = list()

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) == MovieWorld.customer_capacity():
            return
        self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) == MovieWorld.dvd_capacity():
            return
        self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f'{customer.name} has successfully rented {dvd.name}'

    def __find_by_id(self, collection, obj_id):
        for obj in collection:
            if obj.id == obj_id:
                return obj

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_by_id(self.customers, customer_id)
        dvd = self.__find_by_id(self.dvds, dvd_id)

        if dvd not in customer.rented_dvds:
            return f'{customer.name} does not have that DVD'
        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f'{customer.name} has successfully returned {dvd.name}'

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(x) for x in self.dvds])

c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Document Management
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#topic.py
class Topic:
    def __init__(self, id: int, topic: str, storage_folder: str):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic: str, new_storage_folder: str):
        self.topic = new_topic
        self.storage_folder = new_storage_folder

    def __repr__(self):
        return f'Topic {self.id}: {self.topic} in {self.storage_folder}'

#category.py
class Category:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f'Category {self.id}: {self.name}'

#document.py
class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = list()

    @classmethod
    def from_instances(cls, id: int, category: Category, topic: Topic, file_name: str):
        return cls(id, category.id, topic.id, file_name)

    def add_tag(self, tag_content: str):
        if tag_content in self.tags:
            return
        self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content not in self.tags:
            return
        self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name

    def __repr__(self):
        tag_str = ', '.join(self.tags)
        return f"Document {self.id}: {self.file_name}; category {self.category_id}, topic {self.topic_id}, tags: {tag_str}"

from project.category import Category
from project.document import Document
from project.topic import Topic

#storage.py
class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def __find_by_id(self, collection, obj_id):
        for obj in collection:
            if obj.id == obj_id:
                return obj

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id: int):
        category = self.__find_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.__find_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.__find_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#= = = = = = = = = = = = = = = = = = = = = = = = = = =

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Gym
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#customer.py
class Customer:
    id = 1
    def __init__(self, name: str, address: str, email: str):
        self.id = self.get_next_id()
        self.name = name
        self.address = address
        self.email = email

    @staticmethod
    def get_next_id():
        result = Customer.id
        Customer.id += 1
        return result

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


#equipment.py
class Equipment:
    id = 1
    def __init__(self, name):
        self.id = self.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result = Equipment.id
        Equipment.id += 1
        return result

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"


#exercise_plan.py
class ExercisePlan:
    id = 1
    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.id = self.get_next_id()
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        minutes = hours * 60
        return cls(trainer_id, equipment_id, minutes)

    @staticmethod
    def get_next_id():
        result = ExercisePlan.id
        ExercisePlan.id += 1
        return result

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"


#subscription.py
class Subscription:
    id = 1
    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.id = self.get_next_id()
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id

    @staticmethod
    def get_next_id():
        result = Subscription.id
        Subscription.id += 1
        return result

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"


#trainer.py
class Trainer:
    id = 1
    def __init__(self, name: str):
        self.id = self.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result = Trainer.id
        Trainer.id += 1
        return result

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"

#gym.py
class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_by_id(self.subscriptions, subscription_id)
        customer = self.__find_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_by_id(self.equipment, plan.equipment_id)

        return repr(subscription) + '\n' + \
        repr(customer) + '\n' + \
        repr(trainer) + '\n' + \
        repr(equipment) + '\n' + \
        repr(plan)

    def __find_by_id(self, collection, obj_id):
        for obj in collection:
            if obj.id == obj_id:
                return obj


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))


#= = = = = = = = = = = = = = = = = = = = = = = = = = =