# Declaring a Class
class Person():
    pass


'''
We did two things here:

We defined a class using the class keyword and gave it the name Person. This looks a lot like defining a function but with class instead of def.
We told Python to expect nothing else on this indentation level by using the pass keyword. We will later expand on what kinds of things you can put here.
'''

alice = Person()
bob = Person()
candice = Person()
print(bob)

# Instance Methods
'''
Attributes created in .__init__() are called instance attributes. An instance attribute’s value is specific to a particular instance of the class. All Dog objects have a name and an age, but the values for the name and age attributes will vary depending on the Dog instance.
'''


class Person():
    # Instance method
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Create instances of the class
alice = Person('Alice', 20)
bob = Person('Bob', 42)
candice = Person('Candice', 29)

print('Alcie:', alice.name)
print('Bob:', bob.age)
print('Candice:', candice.age)


# Class Attributes
'''
On the other hand, class attributes are attributes that have the same value for all class instances. You can define a class attribute by assigning a value to a variable name outside of .__init__().
'''


class Person():
    # Class attributes
    home_planet = 'earth'
    species = 'humanity'

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age


# Create new instance
alice = Person('Alice', 20)

# Access class and instance attributes
print(alice.home_planet)
print(alice.age)


'''
This Dog class has two instance methods:

.description() returns a string displaying the name and age of the dog.
.speak() has one parameter called sound and returns a string containing the dog’s name and the sound the dog makes.
'''


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)

print(miles.name, miles.age)

print(miles.description())

print(miles.speak("Woof Woof"))

# n the editor window, change the name of the Dog class’s .description() method to .__str__():


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)
print(miles)


# Parent Classes vs Child Classes
'''
Let’s create a child class for each of the three breeds mentioned above: Jack Russell Terrier, Dachshund, and Bulldog.

For reference, here’s the full definition of the Dog class:
'''


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


'''
Remember, to create a child class, you create new class with its own name and then put the name of the parent class in parentheses. Add the following to the dog.py file to create three new child classes of the Dog class:
'''


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    pass  # pass is ussed when the function does not have content, ir order to avoid erros in the system


class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
print('name:', miles.name)
print('buddy age:', buddy)
print('Jacks description:', jack)
print(miles.speak())


# What is getattr() exactly and how do I use it?
'''
For example you have an object person, that has several attributes: name, gender, etc.

You access these attributes (be it methods or data objects) usually writing: person.name, person.gender, person.the_method(), etc.

But what if you don't know the attribute's name at the time you write the program? For example you have attribute's name stored in a variable called attr_name.
'''
# if
attr_name = 'gender'
# then, instead of writing
'''gender = person.gender'''


class Person():
    name = 'Victor'

    def say(self, what):
        print(self.name, what)


print(getattr(Person, 'name'))

attr_name = 'name'
person = Person()
print(getattr(person, attr_name))
print(getattr(person, 'say')('Hello'))
