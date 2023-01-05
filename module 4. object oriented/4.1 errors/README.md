## Errors

Whenever programming, you should be very happy to run into each and every possible error, firstly because you will learn from them, but also because all the errors you fix now won't jump to bite you in the rear after you've deployed it to the world.

Traceback

Whenever Python runs into an error, it prints this line first:

Traceback (most recent call last):
This announces what's coming next: a traceback of what went wrong. This is also known as a stack trace. What 'stack' are we tracing, then? Consider the following code:

def multiply_a(a, b):
    return a * b

def multiply_b(a, b):
    return multiply_a(a, b)

def multiply_c(a, b):
    return multiply_b(a, b)

print(multiply_c(3, 5))
Here we define three functions. On the last line we call multiply_c, which returns the result of calling multiply_b, which calls multiply_a. You can think of this sequence as a stack, each function calling into the next. The last one finally returns something concrete, so the whole stack resolves and 15 is printed.

Should an error occur in multiply_a, it would be useful to know where we came from. For example:

print(multiply_c('incoming', 'error'))
This line would cause an error, but it would only show up in multiply_a. Fortunately, the traceback will show the true culprit.

Traceback (most recent call last):
  File "main.py", line 13, in <module>
print(multiply_c('incoming', 'error'))
  File "main.py", line 10, in multiply_c
return multiply_b(a, b)
  File "main.py", line 6, in multiply_b
return multiply_a(a, b)
  File "main.py", line 2, in multiply_a
return a * b
  TypeError: can't multiply sequence by non-int of type 'str'
Error Types

Note that in the example above the last line starts with TypeError. This is Python telling us about what kind of error it encountered. In this case we tried to multiply two strings, which makes no sense to Python, resulting in a TypeError. Some more common errors you will encounter are:

SyntaxError: when you made a typo or indentation mistake.
ImportError: when you're trying to import a module that does not exist.
IndexError: when you try to access a spot in a list that does not exist.
ValueError: when you try to call a function with arguments of the wrong type.

You can read a little more about errors here in the official Python tutorial.
https://docs.python.org/3/tutorial/errors.html

The official Python documentation has a list of the many built-in exceptions.
https://docs.python.org/3/library/exceptions.html#concrete-exceptions
You don't need to memorize these exceptions or what causes them, just remember the list exists and that you can use it to look up what a specific exception means.

Try.. Except

Whenever your program runs into an error, it simply crashes and that's that. But there's a way to handle errors so that your program may retry, log or report the error to the user in another way and continue.

Here's a function that doesn't crash if it is called with b=0.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You tried to divide by zero. That's not possible in math.")
    return None
To learn more about how try..catch blocks work, read:

Python.org -- Errors and Exceptions
https://docs.python.org/3/tutorial/errors.html
