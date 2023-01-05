Class Inheritance

Consider a jungle. There are many animals in the jungle, and they may have some things in common and some differences between them.

class Tiger():
    def attack(self):
        return 'Bwam!'

    def noise(self):
        return 'RAAAWR'

class Fly():
    def attack(self):
        return 'Bwam!'

    def noise(self):
        return ''

class Snake():
    def attack(self):
        return 'Bwam!'

    def noise(self):
        return 'Hissssss'

class Bear():
    def attack(self):
        return 'Bwam!'

    def noise(self):
        return 'RAAAWR'

baloo = Bear()
print(baloo.attack())
# 'Bwam!'
This gets quite repetitive to do for many animals, and it's a lot of work to modify the attack function for all of the animals if want to do so later. We can use class inheritance:

class Animal():
    def attack(self):
        return 'Bwam!'

class Tiger(Animal):
    def noise(self):
        return 'RAAAWR'

class Fly(Animal):
    def noise(self):
        return ''

class Snake(Animal):
    def noise(self):
        return 'Hissssss'

class Bear(Animal):
    def noise(self):
        return 'RAAAWR'

baloo = Bear()
print(baloo.attack())
# 'Bwam!'
Here Animal is the parent class, and the various types of animals are children. The children inherited the attack method from Animal, so any instance of such a child will carry that function in it.

To learn about the ins and outs of class inheritance, read this from 'Inherit From Other Classes in Python' to the end of the page:

Real Python -- Inherit From Other Classes in Python
https://realpython.com/python3-object-oriented-programming/#inherit-from-other-classes-in-python