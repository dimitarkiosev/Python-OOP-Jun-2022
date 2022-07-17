#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Robots
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def sensors_amount():
        return 1

class MedicalRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 6

class ChefRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 4

class WarRobot(Robot):
    @staticmethod
    def sensors_amount():
        return 12

def number_of_robot_sensors(robot):
    print(robot.sensors_amount())

basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')
number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. ImageArea
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def __gt__(self, other):
        return self.get_area() > other.get_area():
        
    def __ge__(self, other):
        return self.get_area() >= other.get_area():
        
    def __lt__(self, other):
        return self.get_area() < other.get_area():
        
    def __le__(self, other):
        return self.get_area() <= other.get_area():
    
    def __eq__(self, other):
        return self.get_area() == other.get_area():
        
    def __nq__(self, other):
        return self.get_area() != other.get_area():

print('= = = = = = = = = = = = = =')     
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
print('= = = = = = = = = = = = = =')
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)
print('= = = = = = = = = = = = = =')
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Playing
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def start_playing(obd):
    return obd.play()


class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))

class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Shapes
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")

#= = = = = = = = = = = = = = = = = = = = = = = = = = =