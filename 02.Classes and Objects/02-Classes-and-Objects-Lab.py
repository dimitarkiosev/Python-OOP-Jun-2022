Classes and Objects - 30.06
- Classes and Instances
- Attributes
- Methods
- Data Attributes
- Special Data Attributes

= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Venicle
= = = = = = = = = = = = = = = = = = = = = = = = =
class Vehicle():
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = list()

car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Point
= = = = = = = = = = = = = = = = = = = = = = = = =
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'The point has coordinates ({self.x},{self.y})'

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y
        
p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)

= = = = = = = = = = = = = = = = = = = = = = = = =
03. Circle
= = = = = = = = = = = = = = = = = = = = = = = = =
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        return self.pi * self.radius * self.radius

    def get_circumference(self):
        return 2 * self.pi * self.radius

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

= = = = = = = = = = = = = = = = = = = = = = = = =
04. Glass
= = = = = = = = = = = = = = = = = = = = = = = = =
class Glass:
    capacity = 250
    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if ml < (self.capacity - self.content):
            self.content += ml
            return f'Glass filled with {ml} ml'
        else:
            return f'Cannot add {ml} ml'

    def empty(self):
        self.content = 0
        return f'Glass is now empty'

    def info(self):
        return f'{self.capacity - self.content} ml left'

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

= = = = = = = = = = = = = = = = = = = = = = = = =
05. Smartphone
= = = = = = = = = = = = = = = = = = = = = = = = =
class Smartphone:
    
    def __init__(self, memory):
        self.memory = memory
        self.apps = list()
        self.is_on = False
        
    def power(self):
        self.is_on = not self.is_on

    def install(self, app, app_memory):
        if not self.is_on:
            return f'Turn on your phone to install {app}'

        if self.memory >= app_memory:
            return f'Not enough memory to install {app}'

        self.apps.append(app)
        self.memory -= app_memory
        return f'Installing {app}'

    def status(self):
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'

smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())

= = = = = = = = = = = = = = = = = = = = = = = = =