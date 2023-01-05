Classes

Declaring a Class

You know about various types already: int, float and str, for example. Now we introduce the way to define your own class of objects:

class Person():
    pass
We did two things here:

We defined a class using the class keyword and gave it the name Person. This looks a lot like defining a function but with class instead of def.
We told Python to expect nothing else on this indentation level by using the pass keyword. We will later expand on what kinds of things you can put here.
Declaring a class like this is similar to creating a blueprint for how to construct something in real life, like a chair or a cabinet, only we do it for computer objects. The next step is to create an actual construction of that blueprint, called an instance.

bob = Person()
print(bob)
# <__main__.Person object at 0x7f35dd5c9ac0>
Here we created an instance of the Person class. Because we only instructed Python that Person is now a class and nothing else, it didn't really know what tell us about bob when we said print(bob). So it just said: bob is a Person at memory
address so-and-so.

There is no limit to how many Person instances you can create (except for your computer's memory of course):

alice = Person()
bob = Person()
candice = Person()
Here we have multiple instances of Person, and if you were to check if they were different objects in memory (using a is b) you would find that they are indeed separate objects.

Instance Methods

Now let's make this Person class a little more useful by adding some information that is particular to each instance.

class Person():
    # Instance method
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances of the class
alice = Person('Alice', 20)
bob = Person('Bob', 42)
candice = Person('Candice', 29)
Here we added a function within the scope of the class declaration. This is called an instance method. This particular instance method is special because of its name; Python always calls __init__ whenever a new instance of the class is created using the arguments that were passed.

Self

Notice that when we defined __init__ we specified we expected to receive three arguments: self, name and age. But when we created a new instance of the class we only gave it two arguments. This is because self is a special argument that is always passed to methods.

Important

self is always passed to instance methods, and it is always the first argument. If you forget to include it in your function definition (def) this will result in an error. You always have to include self.

So what is this self thing? Look at this example:

class Person():
    # Instance method
    def __init__(self, name, age):
        # Assign instance attributes
        self.name = name
        self.age = age

# Create new instance
alice = Person('Alice', 20)

# Access instance attribute
print(alice.age)
We use a dot (.) to assign the value of name to self.name. What self actually represents here is the instance that we are creating itself. Using the dot (.) we can access and assign values to attributes of this instance. We can then, at any time, access these instance attributes again, like we do here when printing Alice's age.

Class Attributes

We could also have class attributes, which are shared between all instances of the class. These do not use self (check yourself if you can think of why this is) are defined directly inside the class definition, like so:

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


# Style Guide

Finally: the style guide for writing classes is universally agreed to be CamelCase:

# PEP8 -- Class Names
https://pep8.org/#class-names

# More

To read more about classes and see some more examples, see (up to and including Instantiate an Object in Python):

Real Python -- Object Oriented Programming
https://realpython.com/python3-object-oriented-programming/