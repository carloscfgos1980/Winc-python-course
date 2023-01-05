import sys


def multiply_a(a, b):
    return a * b


def multiply_b(a, b):
    return multiply_a(a, b)


def multiply_c(a, b):
    return multiply_b(a, b)


print(multiply_c(3, 5))

'''
The followed  function call will cause an error coz the arguments are strings and not inters. This show us the error and where ocurred
'''

# print(multiply_c('incoming', 'error'))


'''
The followed method prevent our app to crash is there is an error
'''


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You tried to divide by zero. That's not possible in math.")
    return None


print(divide(4, 0))


# Handling Exceptions
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except D:
        print("D")
    except C:
        print("C")
'''
Note that if the except clauses were reversed (with except B first), it would have printed B, B, B — the first matching except clause is triggered.

When an exception occurs, it may have associated values, also known as the exception’s arguments. The presence and types of the arguments depend on the exception type.
'''


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)


'''
BaseException is the common base class of all exceptions. One of its subclasses, Exception, is the base class of all the non-fatal exceptions. Exceptions which are not subclasses of Exception are not typically handled, because they are used to indicate that the program should terminate. They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt the program.

Exception can be used as a wildcard that catches (almost) everything. However, it is good practice to be as specific as possible with the types of exceptions that we intend to handle, and to allow any unexpected exceptions to propagate on.

The most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):
'''


try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

'''
The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be executed if the try clause does not raise an exception. For example:
'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


'''
One of the many ongoing discussions within programming is Look Before You Leap (LBYL) versus Easier to Ask for Forgiveness than Permission (EAFP). The classic example to illustrate this discussion is a situation where you need to check a dictionary for the presence of a key.
'''
ages = {'Alice': 21, 'Bob': 42}
# Look before you leap (LBYL)
if 'Charlie' in ages:
    print("Charlie's age:", ages['Charlie'])
else:
    print("I don't know what Charlie's age is.")

# Easier to ask for forgiveness than permission (EAFP)
try:
    print("Charlie's age:", ages['Charlie'])
except KeyError:
    print("I don't know what Charlie's age is.")
