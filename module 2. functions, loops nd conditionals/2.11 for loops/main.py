# For Loops
names = ['Bob', 'Shaun', 'Preeti', 'Jeff']
for name in names:
    print(f'Hello, {name}!')

# Range
for i in range(10):
    print(i)

list(range(10))

for i in range(900, 1000, 5):  # this print numbers between 900 and 1000 with a jump of 5 steps
    print(i)


# Break and Continue
'''
It may not always be your intention to finish loops that you started. For that we have break. When this expression is reached, the loop that break is in will immediately stop and the code execution continues after the loop
'''

print('We have a long road ahead.')
for i in range(1000):
    print(i)
    if i == 10:
        break
    print('Almost there...')
print("That wasn't so bad after all.")

# better examples than Winc
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print('fruits', x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print('break febore banana', x)
'''
Another keyword like it is continue. Instead of breaking out of the loop completely it only skips to the next iteration.
'''

print('We have a long road ahead.')
for i in range(1000):
    if i % 2 == 0:
        print(i)
        continue
    print('Almost there...')
print("That wasn't half bad.")

# better example of continue than Winc
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print('Do not print banana:', x)

# iterating a list print "Printing List Elements"
mylist = ['alpha', 'bravo', 'charlie']
for i in range(0, 2):  # len function calculates the length of the list
    print('testing', mylist[i])

# iterating a list print "Printing List Elements"
mylist = ['alpha', 'bravo', 'charlie']
for i in range(0, len(mylist)):  # len function calculates the length of the list
    print(mylist[i])

# A function that returns the length of the value:


def myFunc(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True | False, key=myFunc)

print(cars[:2])
