## Main

Now that you know about functions, we want to quickly introduce a pattern that you will start seeing. We have a file called foo.py with the following code.

def main():
    print('Do things here.')
    # ...
    print('End of the program.')

if __name__ == '__main__':
    main()
Here's what you need to know to interpret this code snippet: __name__ is a special variable that will be equal to __main__ whenever the file it's in is the entrypoint. This is the case when we run python foo.py, and it's not the case when we import it as a module.

Note

If you don't know about importing modules yet -- don't worry about it. Just think of if __name__ == '__main__' as a check to see if a person is running your code deliberately or as part of a larger project.

Now that we know about __name__, we can understand what's happening here. Instead of writing our instructions at the top indentation level of a file, we write it in a function called main() and tell the Python interpreter to run main() only if this file is the entrypoint.

Why?

Why should we do this? There are two reasons. The first one is that we may want our code to do different things based on whether or not it is the entrypoint. Perhaps we want to print (or log) fewer things if the file is not the entrypoint, or we may want to do some I/O if it is. Checking __name__ is how we can make that happen.

The other reason to use this pattern has to do with execution order. Take a look at this code snippet.

print(greet('Bob'))

def greet(name):
    return f'Hi, {name}!'
If you try to run this, you'll get a NameError on line 1 saying that 'greet' is not defined. It's true that we defined it later in the file, but when the Python interpreter ran line 1, it was not defined yet. So we would have to swap the two statements.

def greet(name):
    return f'Hi, {name}!'

print(greet('Bob'))
This runs fine, but the code is less readable for someone who opens it up for the first time. Ideally we would like the main flow right at the top, and the functions that branch off of this following it. We can do this by wrapping our main logic in the function main() and then call that function only after we've read the rest of the file.

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
Now we have a nicely structured file with the main logic at the top, and all the functions that call it below it.

Important

The if __name__ == '__main__'-block must be at the bottom of the file, otherwise main() is executed before Python learns about all the functions, and we may still get NameErrors.