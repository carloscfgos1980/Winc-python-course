Sets and Tuples

This part is extra and serves just to inform you of the existence of the set and tuple. There is no exercise paired with this information.

Sets

Sets are a datatype that you can think of as unordered lists. Try this in REPL:

list_a = [1,2,3]
list_b = [3,2,1]
list_a == list_b
set(list_a) == set(list_b)
Sets only contain a particular object once.

set_a = set([1,2,3])
set_a.add(3)
print(set_a)
Because of this, they are particularly useful to do things that require looking at unique elements of a list (like len(set(example_list))) but especially for the common set operations:

set_a = set([1,2,3])
set_b = set([3,4,5])

# Union
# You can read this as 'set_a or set_b', so: 'any element that is in set a or set b'
set_a | set_b

# Difference
set_a - set_b

# Intersection
set_a.intersection(set_b)

# Checking if a set is a subset of another.
# In other words: if the other set includes all of its own elements.
small = set([2,3])
big = set([1,2,3,4])
small.issubset(big)
Real Python -- Sets in Python
Tuples

Tuples are much like lists, but immutable. Unlike lists, they are defined using parentheses (( )). They are used when you know for sure that the tuple never needs to be modified. Here's an example:

# Creating a tuple
alice = ('Alice', 5)

# Tuples can contain any number of elements
bob = ('Bob', 3, 9)

# A list of tuples
persons = [alice, bob]

Real Python -- Tuples in Python

https://realpython.com/python-lists-tuples/#python-tuples