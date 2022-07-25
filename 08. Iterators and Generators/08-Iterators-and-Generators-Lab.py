#= = = = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Custom Range
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.next_value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value > self.end:
            raise StopIteration

        value_to_return = self.next_value
        self.next_value += 1
        return value_to_return

one_to_ten = custom_range(1, 10)
# one_to_ten = range(1, 10)
for num in one_to_ten:
    print(num)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#02. Reverse Iter
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class reverse_iter:
    def __init__(self, values):
        self.values = list(values)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < -len(self.values):
            raise StopIteration

        value_to_return = self.values[self.index]
        self.index -= 1
        return value_to_return

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#03. Vowels
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
class vowels:
    vowel_chars = 'eyuioa'

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].lower() not in self.vowel_chars:
                self.index += 1
                continue

            value_to_return = self.text[self.index]
            self.index += 1
            return value_to_return

        raise StopIteration

    def iter_with_gen(self):
        return (x for x in self.text if x.lower() in self.vowel_chars)


my_string = vowels('Abcedifuty0o')
for char in my_string:  # This work thanks to duck-typing
    print(char)

for char in my_string.iter_with_gen():
    print(char)

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#04. Squares
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def squares(n):
    value = 1
    while value < n + 1:
        yield value * value
        value += 1


print(list(squares(5)))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#05. Generator Range
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def genrange(start, end):
    value = start

    while value < end + 1:
        yield value
        value += 1


print(list(genrange(1, 10)))

#= = = = = = = = = = = = = = = = = = = = = = = = = = =
#06. Reverse String
#= = = = = = = = = = = = = = = = = = = = = = = = = = =
def reverse_text(text):
    index = 0
    n = len(text)
    while index < n:
        yield text[n - index - 1]
        index += 1


for char in reverse_text("step"):
    print(char, end='')

#= = = = = = = = = = = = = = = = = = = = = = = = = = =