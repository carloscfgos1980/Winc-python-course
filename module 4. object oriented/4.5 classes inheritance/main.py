# Class Inheritance
'''
Consider a jungle. There are many animals in the jungle, and they may have some things in common and some differences between them.
'''


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

'''
This gets quite repetitive to do for many animals, and it's a lot of work to modify the attack function for all of the animals if want to do so later. We can use class inheritance:
'''


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

'''
Here Animal is the parent class, and the various types of animals are children. The children inherited the attack method from Animal, so any instance of such a child will carry that function in it.
'''
