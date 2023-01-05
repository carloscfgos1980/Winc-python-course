Simple Functions

We previously told you about the function len -- you used it to get the length of some string.

len('Hey')
What is really happening here is that we make use of some code that the people that made Python wrote for us. They conveniently packaged it in a function that we can use whenever we want.

The function's name is len;
It takes one variable as input;
If not stopped by any sort of error, it returns the length of that variable.
Writing Your Own Functions

When writing code yourself, you may at some point find that you're repeating yourself in your program. That's a good sign that you need to write a function yourself! Here's how:

def double(x):
    doubled_x = x * 2
    return doubled_x

four_doubled = double(4)
print(four_doubled)
Copy-paste this code snippet and paste it in your REPL of choice (remember: Thonny, REPL.it or python) or run it as a standalone file. The result should be 8. Let's walk through what it does exactly:

On the first line we start defining a function, hence that line starts with the keyword def.
We name this function double
It takes a single input variable that we name x
On the second line we start writing what the function should do. We use the input variable x as though we declared the variable ourselves previously. We write doubled_x = x * 2, which is nothing special in itself.
The third line states: return doubled_x. This concludes the function and returns doubled_x.
On the second-to-last line we can understand what "returning a variable" means; you can visualize the value 4 entering into the function, where it's multiplied by two and stored in the variable doubled_x, which is the value that the function comes back with. So now we might imagine double(4) being replaced by 8.
The return value from double(4) -- which is 8 -- is assigned to four_doubled.
The end result is printed out.
Important

This may seem like a lot of information, but the only special words used here are def and return.

def starts a function definition;
We write what we want the function to do one indentation level higher than where def is;
We end the function with return, which defines what should be returned.
Reusing Functions

The beauty of functions is this: now that we defined the function once, we can use it forever!

double(5)
double(21)
double(1.2)
double('Hey! ')
Our function double doesn't do a lot of interesting stuff, but think back to when you were manipulating strings. A function like this is very handy:

def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'

initials('Ex Ample')
initials('Bob Cat')
initials('Function Nice')
To do this without functions would have been a giant hassle with us rewriting or copy-pasting the same code over and over.

Multiple Arguments

The final thing you should know about functions for now is that we are not limited to one argument per function.

def multiply(a, b):
    return a * b

multiply(2, 2)
multiply(9, 2.3)
multiply(29, 'Hey! ')
As shown here, the way to define functions with multiple arguments is to simply add them in between the round brackets:

def func_with_multiple_args(arg_0, arg_1):
    print('I received the arguments:', arg_0, arg_1)