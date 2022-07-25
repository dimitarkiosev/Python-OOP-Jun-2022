#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Take skip
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.next_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 1:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += self.step
        self.count -= 1
        return value_to_return

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Dictionary Iterator
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class dictionary_iter:
    def __init__(self, dd):
        self.items = list(dd.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.items):
            raise StopIteration

        result = self.items[self.idx]
        self.idx += 1
        return result

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Countdown Iterator
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class countdown_iterator:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 0:
            raise StopIteration

        result = self.count
        self.count -= 1
        return result

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
print('\n- = - = - = - = - = - = - = - =')
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Sequence Repeat
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class sequence_repeat :
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.number:
            raise StopIteration

        result = self.sequence[self.count % len(self.sequence)]
        self.count += 1
        return result

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
print('\n- = - = - = - = - = - = - = - = - = - = - =')
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#05. Take Halves
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def solution():

    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
print('\n- = - = - = - = - = - = - = - = - = - = - =')
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#06. Fibonacci Generator
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def fibonacci():
    first = 0
    second = 1
    yield first
    yield second

    while True:
        result = first + second
        first, second = second, result
        yield result

generator = fibonacci()
for i in range(5):
    print(next(generator))
print('\n- = - = - = - = - = - = - = - = - = - = - =')
generator = fibonacci()
for i in range(1):
    print(next(generator))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#07. Reader
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def read_next(*args):
    dd = args
    for each in dd:
        for i in each:
            yield i

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
print('\n- = - = - = - = - = - = - = - = - = - = - =')
for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#08. Prime Numbers
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def is_prime(i):
    flag = 0
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                flag = 1
        if flag:
            return False
        else:
            return True

def get_primes(ll):
    for i in ll:
        if is_prime(i):
            yield i


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#09. Possible permutations
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def possible_permutations(ll):
    for _ in len(ll):
        for i in ll:

[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]

#= = = = = = = = = = = = = = = = = = = = = = = = = = =