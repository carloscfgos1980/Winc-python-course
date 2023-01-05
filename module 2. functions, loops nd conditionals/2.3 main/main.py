# (1) Python takes note of this function
def main():
    # (5) At this point greet() is known and we can run it.
    print(greet('Bob'))

# (2) Then this one


def greet(name):
    return f'Hi, {name}!'


# (3) Now this statement is read
if __name__ == '__main__':
    # (4) main is run
    main()

'''
Important

The if __name__ == '__main__'-block must be at the bottom of the file, otherwise main() is executed before Python learns about all the functions, and we may still get NameErrors.
'''
