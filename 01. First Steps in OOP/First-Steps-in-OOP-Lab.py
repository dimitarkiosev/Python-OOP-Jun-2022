#= = = = = = = = = = = = = = = = = = = = = = = = = 
#01. Rhombus of Stars
#= = = = = = = = = = = = = = = = = = = = = = = = =
def get_line(i, n):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + ('* ' * stars_count).strip()

def print_line(n):
    print(get_line(n-1, n-1))

def print_rhombus(n):
    for i in range(0, n, 1):
        print(get_line(i, n))
    for i in range(n-2, -1, -1):
        print(get_line(i, n))

n = int(input())
print_rhombus(n)

#= = = = = = = = = = = = = = = = = = = = = = = = = 
#02. Scope Mess
#= = = = = = = = = = = = = = = = = = = = = = = = =
x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)

#= = = = = = = = = = = = = = = = = = = = = = = = =
#03. Class Book
#= = = = = = = = = = = = = = = = = = = = = = = = =
class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

#= = = = = = = = = = = = = = = = = = = = = = = = =
#04. Car
#= = = = = = = = = = = = = = = = = = = = = = = = =
class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'

car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

#= = = = = = = = = = = = = = = = = = = = = = = = =
#05. Music
#= = = = = = = = = = = = = = = = = = = = = = = = =
class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics
        
song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())

#= = = = = = = = = = = = = = = = = = = = = = = = =
