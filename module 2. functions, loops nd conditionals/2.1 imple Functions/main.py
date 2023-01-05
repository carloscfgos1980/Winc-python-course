# Simple Functions

'''We previously told you about the function len -- you used it to get the length of some string.'''
len('Hey')


# Writing Your Own Functions

def double(x):
    doubled_x = x * 2
    return doubled_x


four_doubled = double(4)
print(four_doubled)
double(5)
double(21)
double(1.2)
double('Hey! ')  # error is not an inter or a float


def initials(name):
    # find the first letter of the name and turn it into capital letter
    first = name[0].upper()

    # find the first letter of the lastname and turn it into capital letter
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'


initials('Ex Ample')
initials('Bob Cat')
initials('Function Nice')

# Multiple Arguments


def multiply(a, b):
    return a * b


multiply(2, 2)
multiply(9, 2.3)
multiply(29, 'Hey! ')  # this is one return 'Hey' 29 times!
