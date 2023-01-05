## Types and Casting

Every value (or piece of information) in Python has a type. You can find out what the type of a value is by using the built-in function type. Try this in a an empty Python file (how to make a Python file in VSCode).

type(3)
type(3.14)
type('Pi')
If we assign a value to a variable we can ask Python what the type of the value in that variable is:

some_number = 5
type(some_number)
another_number = 9.81
type(another_number)
some_string = 'Hello world'
type(some_string)
In one way, Python is not too strict on types. When we define a variable, we don't have to specify what type we want it to be. Some languages do require this -- here's what declaring and initializing an integer looks like in C:

int answer = 42;
On the other hand, Python is strongly typed. This means that Python is strict in which values you can use with which operators. If you try to use the + operator on a string and a number value you will get an error:

'I like ' + 3.14
TypeError: can only concatenate str (not "float") to str
42 + ' is the answer'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
Both errors tell you that there's something not quite right with the types in the code.

The first error says "I'm trying to concatenate (glue strings together), but you've given me a string and a number (float) and I can't concatenate those together".

The second error says "I can't add a number (int) and a string (str)".

(Type)-casting

If you have a string with a number in it and you want to use it in a calculation, or if you have a number and want to use it in a sentence: that's possible. What you can do is "cast" the value to another type. In other words: casting means converting a value of one type to another type.

'I like ' + str(3.14)
Now, read this article on the details of casting:

w3schools.com -- Python Casting
https://www.w3schools.com/python/python_casting.asp