For Loops

An important concept in programming is the loop, and particular type of loop is the for loop. In Python, the for loop is implemented in a very intuitive way. It almost looks like English:

names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
for name in names:
    print(f'Hello, {name}!')
This prints a greeting for each name in the names-list. Here's how that works: names is a list of strings. By writing for name in names: we specify that in the next (indented) part we want a new variable name to take on the values in the names list one-by-one. Then, in the indented block, we write whatever we want, knowing that it is done for each name in names. After the for loop, the name-variable no longer exists (it's out of scope).

We could also have done this:

names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
print(f'Hello, {names[0]}!')
print(f'Hello, {names[1]}!')
print(f'Hello, {names[2]}!')
print(f'Hello, {names[3]}!')
But this way produces more lines of code, is less readable, more prone to typing errors, less maintainable, and it requires that we know the length of names ahead of time. For loops solve all of these problems in one fell swoop.

Note

Some jargon: in this example we are 'looping over' names or 'iterating over' names. We are always iterating over an iterable, which is names in this example.

Iterables

In Python you can only loop over an iterable. That's pretty much the definition of an iterable, really. The idea is that there has to be some items inside the iterable for a variable to iteratively take the value of one-by-one in the loop, otherwise there's nothing to loop over.

Lists are one iterable object type, and there's one other type we have discussed so far that is an iterable. Try to guess what this will do before you try it in a REPL:

question = 'How many roads must one walk down?'
for c in question:
    print(c)
Range

A useful tool to know about is range. Try these statements in a REPL:

for i in range(10):
    print(i)

list(range(10))
We wrap the range in list to "cast" it to a List type. You will learn more about casting later on.

We can pass more than one argument to range to generate more specific ranges. The syntax is range(start, stop, step). See if you can figure out what the start, stop, step arguments mean exactly by playing around with it in a REPL. Hint: it's a lot like slicing! Bonus points for producing ranges that go from high to low.

for i in range(900,1000,5):
    print(i)
Break and Continue

It may not always be your intention to finish loops that you started. For that we have break. When this expression is reached, the loop that break is in will immediately stop and the code execution continues after the loop.

print('We have a long road ahead.')
for i in range(1000):
    print(i)
    if i == 10:
        break
    print('Almost there...')
print("That wasn't so bad after all.")
Another keyword like it is continue. Instead of breaking out of the loop completely it only skips to the next iteration.

print('We have a long road ahead.')
for i in range(1000):
    if i % 2 == 0:
        print(i)
        continue
    print('Almost there...')
print("That wasn't half bad.")
To read more and see more examples, see:

Real Python -- For Loop

https://realpython.com/python-for-loop/