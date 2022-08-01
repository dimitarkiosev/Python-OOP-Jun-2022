#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Mammal
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from project.mammal import Mammal

import unittest

class TestMammal(unittest.TestCase):
    NAME = 'TestMammal'
    MAMMAL_TYPE = 'TYPEA'
    SOUND = 'uhahaha'
    def setUp(self):
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test__init__when_initialize__shoul_create_proper_obj:
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)
        
    def test__make_sound(self):
        result = self.mammal.make_sound()
        expected_result = f'{self.NAME} makes {self.SOUND}'
        self.assertEqual(result, expected_result)

    def test__get_kingdom(self):
        result = self.mammal.get_kingdom()
        expected_result = 'animals'
        self.assertEqual(result, expected_result)

    def test__info(self):
        result = self.mammal.info()
        expected_result = f'{self.NAME} is of type {self.MAMMAL_TYPE}'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Vehicle
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25
    FUEL = 100
    HORSE_POWER = 150

    def setUp(self):
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test__drive__when_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertIsNotNone(ex)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test__drive__when_fuel_is_enough(self):
        distance = 50
        result = self.FUEL - (distance * self.DEFAULT_FUEL_CONSUMPTION)
        self.vehicle.drive(distance)
        self.assertEqual(result, self.vehicle.fuel)

    def test__drive__when_distance_is_maximum(self):
        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION
        self.vehicle.drive(distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test__refuel__when_over_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertIsNotNone(ex)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test__refuel__when_have_capacity(self):
        self.vehicle.drive(40)
        self.vehicle.refuel(30)
        result = self.FUEL - (40 * self.DEFAULT_FUEL_CONSUMPTION) + 30
        self.assertEqual(result, self.vehicle.fuel)

    def test__str__return_proper_mess(self):
        result = str(self.vehicle)
        excpected = f"The vehicle has {self.vehicle.horse_power} horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(result, excpected)


if __name__ == '__main__':
    unittest.main()

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Hero
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from project.hero import Hero
import unittest


class TestHero(unittest.TestCase):
    HERO_USERNAME = 'StarWars'
    HERO_LEVEL = 10
    HERO_HEALTH = 100
    HERO_DAMAGE = 75

    def setUp(self):
        self.attacker = Hero(self.HERO_USERNAME, self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)

    def test__init(self):
        self.assertEqual(self.HERO_USERNAME, self.attacker.username)
        self.assertEqual(self.HERO_LEVEL, self.attacker.level)
        self.assertEqual(self.HERO_HEALTH, self.attacker.health)
        self.assertEqual(self.HERO_DAMAGE, self.attacker.damage)

    def test__battle__when_using_same_names(self):
        enemy = Hero(self.HERO_USERNAME, self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)
        with self.assertRaises(Exception) as ex:
            self.attacker.battle(enemy)
        self.assertIsNotNone(ex)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test__battle_when_attacker_is_death(self):
        enemy = Hero('Enemy', 5, 75, 40)
        self.attacker.health = 0
        with self.assertRaises(ValueError) as ex:
            self.attacker.battle(enemy)
        self.assertIsNotNone(ex)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test__battle_when_enemy_is_death(self):
        enemy = Hero('Enemy', 5, -2, 40)
        with self.assertRaises(ValueError) as ex:
            self.attacker.battle(enemy)
        self.assertIsNotNone(ex)
        result = f'You cannot fight {enemy.username}. He needs to rest'
        self.assertEqual(result, str(ex.exception))

    def test__battle_when_result_is_draw(self):
        enemy = Hero('Enemy', self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)
        result = self.attacker.battle(enemy)

        expected_health = self.HERO_HEALTH - (self.HERO_LEVEL * self.HERO_DAMAGE)

        self.assertEqual('Draw', result)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_health, enemy.health)

    def test__battle_when_result_is_win(self):
        enemy_damage = self.attacker.health / 5
        enemy_level = 4
        enemy_health = (self.HERO_DAMAGE * self.HERO_LEVEL) - 1

        enemy = Hero('Enemy', enemy_level, enemy_health, enemy_damage)
        expected_level = self.HERO_LEVEL + 1
        expected_health = self.HERO_HEALTH - (enemy_level * enemy_damage) + 5
        expected_damage = self.HERO_DAMAGE + 5

        result = self.attacker.battle(enemy)

        self.assertEqual('You win', result)
        self.assertEqual(expected_level, self.attacker.level)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_damage, self.attacker.damage)

    def test__battle_when_result_is_lose(self):
        enemy_damage = self.attacker.health / 5
        enemy_level = 6
        enemy_health = (self.HERO_DAMAGE * self.HERO_LEVEL) + 10

        enemy = Hero('Enemy', enemy_level, enemy_health, enemy_damage)
        expected_level = enemy_level + 1
        expected_health = enemy.health - (self.HERO_LEVEL * self.HERO_DAMAGE) + 5
        expected_damage = enemy.damage + 5

        result = self.attacker.battle(enemy)

        self.assertEqual('You lose', result)
        self.assertEqual(expected_level, enemy.level)
        self.assertEqual(expected_health, enemy.health)
        self.assertEqual(expected_damage, enemy.damage)

    def test__str(self):
        expected= f'Hero {self.HERO_USERNAME}: {self.HERO_LEVEL} lvl\nHealth: {self.HERO_HEALTH}\nDamage: {self.HERO_DAMAGE}\n'
        result = str(self.attacker)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Student
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from project.student import Student
import unittest


class TestStudent(unittest.TestCase):
    NAME = 'Student_test'
    def setUp(self):
        self.student = Student(self.NAME)

    def test__init_when_none_courses(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test__init_when_courses(self):
        courses = {"PythonAds": ['note1', 'note2', 'notes'],}
        self.student = Student(self.NAME, courses)
        self.assertEqual(courses, self.student.courses)
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(courses, self.student.courses)

    def test__enroll_when_update_notes(self):
        course_name = 'Python OOP'
        courses = {course_name: ['note_1', 'note_2']}
        student = Student(self.NAME, courses)

        result = student.enroll(course_name, ['note_3', 'note_4'])

        self.assertEqual('Course already added. Notes have been updated.', result)
        self.assertEqual(['note_1', 'note_2', 'note_3', 'note_4'], student.courses[course_name])

    def test__enroll_when_add_course(self):
        course_name = 'Python OOP'
        result = self.student.enroll(course_name, ['note_1', 'note_2'])
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(['note_1', 'note_2'], self.student.courses[course_name])

        course_name = 'Python WEB'
        result = self.student.enroll(course_name, ['note_1web', 'note_2web'], 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertEqual(['note_1web', 'note_2web'], self.student.courses[course_name])

    def test__enroll_when_add_course_with_no_instruction(self):
        course_name = 'Python WEB'
        result = self.student.enroll(course_name, ['note_1web', 'note_2web'], 'N')
        self.assertEqual('Course has been added.', result)
        self.assertEqual([], self.student.courses[course_name])

    def test__add_notes__when_course_is_not_added(self):
        notes = ['notes_10']
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Python_Djange', notes)
        self.assertIsNotNone(ex)
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test__add_notes__when_course_is_added(self):
        courses = {"PythonAds": ['note1', 'note2', 'notes3'],}
        student = Student(self.NAME, courses)
        notes = 'notes_10'
        result = student.add_notes('PythonAds', notes)
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['note1', 'note2', 'notes3', 'notes_10'], student.courses['PythonAds'])

    def test__leave_course__when_course_is_not_in_list(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Python_Django')
        self.assertIsNotNone(ex)
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))

    def test__leave_course__when_course_is_in_list(self):
        courses = {"PythonAds": ['note1', 'note2', 'notes3'],}
        student = Student(self.NAME, courses)
        result = student.leave_course('PythonAds')
        self.assertEqual('Course has been removed', result)
        self.assertTrue('PythonAds' not in student.courses)

if __name__ == '__main__':
    unittest.main()


#= = = = = = = = = = = = = = = = = = = = = = = = = = =