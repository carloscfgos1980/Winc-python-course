String Operations

An operator is a character (or combination of characters) that signifies an operation should be done on a number of operands. For example, in Python (and every other major programming language) we can do addition with the +-operator, which adds up the operands to its left and right.

1 + 1 == 2
2 + 2 == 4
So the operator here is the +. The two numbers on the left and right of the + are the operands. We can say "the operator performs a certain operation on the operands".

So these operations with numbers are not too complex, but what would happen if we do this?

'Hey!' + 1
It's not immediately obvious what should happen here. There are a number of ways the designers of Python could have decided to handle this. One way would be to let Python say: "Error: you asked us to add a string and a number, but this is just not a thing." In fact, that's exactly what they did:

'Hey!' + 1
TypeError: unsupported operand type(s) for +: 'int' and 'str'
Adding a str and an int is something you cannot do in Python. Fortunately, most operations that intuitively have a meaning are supported. Try these lines in a REPL and see what you get:

'Hello, ' + 'world!'
'Jump! ' * 5
The + operator does something different because the operands are strings and not numbers. The same goes for the * operator.

One very useful operator is the membership operator: in. Try these lines in a REPL to see what they do. Can you see why in is well-chosen syntax for the membership operator?

'Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.'
'Shane' in 'We went out for dinner with with Anne, Samuel and Bob.'
5 in 'We were lucky that they had a table for 5.'
str(5) in 'We were lucky that they had a table for 5.'
To compare values we have the ==-operator, which works for numbers, but also for strings:

'Me' == 'Me'
'You' == 'Me'
'Me' == 'me'
What if we don't want the whole string, but just one character from it? The solution is to index into the string. Here's how (try to predict what letter will be printed before you let Python tell you):

letter_grades = 'ABCDF'
letter_grades[0]
letter_grades[3]
Remember: Python indices start at 0!

One handy feature is indexing with negative numbers. This works in exactly the same way as indexing with positive ones, only it starts at the end and works its way back:

letter_grades = 'ABCDF'
letter_grades[-1]
letter_grades[-2]
letter_grades[-2] == letter_grades[3]
An expansion on indexing is slicing. It's exactly what you would expect given the name: taking a slice of something, in this case a string. Try these examples:

waltz = 'onetwothree'
waltz[0:3]
# We don't need to specify the 0 if we start at the beginning
waltz[:3]
waltz[3:6]
waltz[6:11]
# Same goes for the end -- we can leave it empty
waltz[6:]
# We can specify a step size if we don't want a continuous slice
waltz[0:11:2]
The pattern here is waltz[start:stop:step]. Note that the stopping point itself is not included in the slice. Experiment in the REPL to see what we mean by that.

When we need the length of a string we have the len-function:

sentence = 'The length of this string is:'
print(sentence, len(sentence))
print('Wait.. You just made it longer!')
If we want to insert a variable into a string we do it like this:

Write f in front of the string.
Use curly braces ({}) to insert the variable into the string.
answer = 42
qa = f'The answer is.. {answer}'
The general idea of inserting variables into strings is called string interpolation, and here we are using f-strings to do it. There are other ways of doing string interpolation which you might come across online, but f-strings are the most convenient for short and simple cases.

For more explanation and examples, see:

Real Python -- Python Strings: String Interpolation

https://realpython.com/python-strings/#string-operators