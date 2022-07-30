#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Number Increment
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def number_increment(numbers):
    def increase():
        return [x+1 for x in numbers]

    return increase()

print(number_increment([1, 2, 3]))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Vowel Filter 
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from functools import wraps


def vowel_filter(func):
    vowels = 'eyuioaa'

    @wraps(func)
    def wrapper():
        result = func()
        return [x for x in result if x.lower() in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ['a', 'b', 'c', 'd', 'e']

print(get_letters())

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Even Numbers
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from functools import wraps

def even_numbers(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        ll = [x for x in result if x % 2 == 0]
        return ll

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Multiply
#= = = = = = = = = = = = = = = = = = = = = = = = = = =

def multiply(times):
    def decorator(function):
        def wrapper(*args, **kwargs):
            num = args[0]
            result = (num + 10) * times
            return result
        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =