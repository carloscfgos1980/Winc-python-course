# The while Loop

i = 3  # starting point of looping
while i <= 10:  # last point of looping
    print(i)
    i += 2  # steps
# Note: remember to increment i, or else the loop will continue forever.

# The break Statement.
# With the break statement we can stop the loop even if the while condition is true:
i = 0
while i < 10:
    print(i)
    if (i == 6):
        break
    i += 1


# The continue Statement.
# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Note that number 3 is missing in the result

# The else Statement.
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("i is no longer than 5")


a = ['foo', 'bar', 'baz', 'shoes', 'testing']
while a:
    print(a.pop(0))  # iterate thru the list in the original order

a = ['foo', 'bar', 'baz', 'shoes', 'testing']
while a:
    print(a.pop(-1))  # iterate thru the list in the backward order


# while break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

# while continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

# Example of while and else
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

# Stoping the itiration in certain element
a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
    if a[i] == s:
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')


a = ['foo', 'bar', 'baz', 'qux']
s = 'baz'

i = 0
while i < len(a):
    print('stop itiration', a[i])
    if a[i] == s:
        print(s, 'founded')
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')

a = ['foo', 'bar', 'baz next', 'qux']
i = 0
while i < len(a):
    print('stop itiration', a[i])
    if 'baz' in a[i]:
        print(s, 'founded')
        # Processing for item found
        break
    i += 1
else:
    # Processing for item not found
    print(s, 'not found in list.')


# Nested while Loops

a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))

# One-Line while Loops
n = 5
while n > 0:
    n -= 1
    print(n)

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Counting in a While loop

count = 0

max_count = 5

while count < max_count:
    count += 1
    print(count)  # 👉️ 1 2 3 4 5

count = 0

my_list = ['bobby', 'hadz', 'com']

while len(my_list) > 0:
    my_list.pop()

    count += 1
    print(count)
