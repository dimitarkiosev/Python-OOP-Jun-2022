#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Workers
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from abc import ABC, abstractmethod

class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass

class Worker(BaseWorker):
    def work(self):
        print("I'm working!!")

class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")

class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(Worker)
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()

print('- = - = - = - = - = - = - = - = - = -')
worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Workers - Updated
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from abc import ABC, abstractmethod
import time

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(Workable, Eatable):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)

class SuperWorker(Workable, Eatable):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)

class Robot(Workable):
    def work(self):
        print("I'm a robot. I'm working....")

class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass

class WorkManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)
        self.worker = worker

    def manage(self):
        self.worker.work()

class BreakManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), "`worker` must be of type {}".format(Eatable)
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()

work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Prisoner
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
import copy

class Person:
    def __init__(self, position):
        self.position = position


class FreePerson(Person):
    def __init__(self, position):
        self.position = position

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist

class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False



prisoner = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Shapes
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return (self.width * self.height) / 2

class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total

shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#05. Emails
#= = = = = = = = = = = = = = = = = = = = = = = = = = =

from abc import ABC, abstractmethod

class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass

class MyContent(IContent):
    def __init__(self, text):
        super().__init__(text)

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])

class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender = self.__sender, receiver = self.__receiver, content = self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =