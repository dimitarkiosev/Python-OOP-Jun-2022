#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Logged
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from functools import wraps

def logged(function):

    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f'you called {function.__name__}{args}\nit returned {result}'

    return wrapper

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Even Parameters
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from functools import wraps

def even_parameters(function):
    @wraps(function)
    def wrapper(*args):
        for x in args:
            if not isinstance(x, int) or x % 2 != 0:
                return 'Please use only even numbers!'
        result = function(*args)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result
print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Bold, Italic, Underline
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from functools import wraps

def make_bold(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f'<b>{result}</b>'
    return wrapper

def make_italic(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f'<i>{result}</i>'
    return wrapper

def make_underline(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f'<u>{result}</u>'
    return wrapper

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"
print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"
print(greet_all("Peter", "George"))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Type Check
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def type_check(type):
    def decorator(function):
        def wrapper(*args):
            if not isinstance(args[0], type):
                return 'Bad Type'
            return function(*args)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#05. Cache
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from functools import wraps

def cache(function):
    log = dict()

    @wraps(function)
    def wrapper(n):
        if n in log:
            return log[n]
        result = function(n)
        log[n] = result
        return result

    wrapper.log = log
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
print(fibonacci.log)
print(fibonacci(4))
print(fibonacci.log)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#06. HTML Tags
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def tags(tag):
    def decorator(function):
        def wrapper(*args):
            result = function(*args)
            return f'<{tag}>{result}</{tag}>'
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#07. Store Results
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def store_results(function):
    def wrapper(*args):
        result = function(*args)
        with open('./results.txt', 'a') as file:
            file.write(f"Function '{function.__name__}' was add called. Result: {result}")
            file.write('\n')
        return result

    return wrapper

@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

print(add(2, 2))
print(mult(6, 4))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#08. Execution Time
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
from time import time

def exec_time(function):
    def wrapper(*args):
        start_time = time()
        function(*args)
        end_time = time()
        return end_time - start_time
    return wrapper

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))

@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())

#= = = = = = = = = = = = = = = = = = = = = = = = = = =