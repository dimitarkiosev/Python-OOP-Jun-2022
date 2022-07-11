Encapsulation
1. Definition
    - packing of data
    - restrictions
    
    A. Encapsulation in Python - public by default
        private - _ _ - doble underscore
        protected - _ - single underscore
        
2. Name Mangling a Variable
    A. getter - @property
    B. setter - @xxx.setter
    
3. Name Mangling a Method
    def __name(self):
        pass

4. Built-in attributes
    getattr()
    hasattr()
    setattr()
    delattr()

= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Person
= = = = = = = = = = = = = = = = = = = = = = = = =
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Mammal
= = = = = = = = = = = = = = = = = = = = = = = = =
class Mammal:
    __kingdom = 'animals'
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Profile
= = = = = = = = = = = = = = = = = = = = = = = = =
class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not (5 <= len(value) <= 15):
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_lenght_valid = len(value) >= 8
        is_upper_case = [char for char in value if char.isupper()]
        is_digit = [char for char in value if char.isdigit()]

        if not is_lenght_valid or not is_upper_case or not is_digit:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Email Validator
= = = = = = = = = = = = = = = = = = = = = = = = =
class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        username = email.split('@')[0]
        mail, domain = email.split('@')[1].split('.')

        is_valid = self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)

        return is_valid
        
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Account
= = = = = = = = = = = = = = = = = = = = = = = = =
class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return 'Pin changed'
        return 'Wrong pin'

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

= = = = = = = = = = = = = = = = = = = = = = = = =