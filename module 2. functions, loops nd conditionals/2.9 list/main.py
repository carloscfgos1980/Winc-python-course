bob = 'Bob'
shaun = 'Shaun'
preeti = 'Preeti'
jeff = 'Jeff'


names = ['Bob', 'Shaun', 'Preeti', 'Jeff']

'''
A list is an object just like any other you've encountered so far, like str, int and float. They can hold a mix of objects, even other lists:
'''
example_list = ['Bob', 3.14, 42]
example_list_of_lists = [['Bob', 3.14, 42], ['Preeti', 3.14, 42]]

# Indexing and slicing
example_list = ['zeroth', 'first', 'second', 'third']
# Get the zeroth item.
example_list[0]
# Get the second item.
example_list[2]
# Get a slice of the list
example_list[0::2]


# Mutability
'''
Unlike strings, you can modify parts of lists after creating them. In official terms: lists are mutable.
'''
example_string = 'Gi!'
# The next line results in an error
example_string[0] = 'H'

# But this works fine
example_list = ['zeroth', 1, 2, 3]
example_list[0] = 0
print(example_list)
# Output: [0, 1, 2, 3]


# Comparison and order
'''
A list can be compared with another list. Note that lists are ordered, so two lists that contain the same values in different orders are not equal.
'''
example_list_a = [1, 2, 3]
example_list_b = [3, 2, 1]
example_list_a == example_list_b  # False

# Casting
'''
Some types of objects can be cast into lists using the built in list function, and vice versa. It doesn't come up often in practice for the types that we've discussed so far, but keep this one in your back pocket for later. One case you may find entertaining to look at now is list-to-string casting:
'''
example_list = ['this', 'is', 'fun']
str(example_list)
list(str(example_list))
str(list(str(example_list)))
list(str(list(str(example_list))))
str(list(str(list(str(example_list)))))
# Et cetera :-)


# Common operations
example_list = [42.0, 3.50, 3.14, 42.0]
len(example_list)  # outcome: 4
min(example_list)  # outcome: 3.14
max(example_list)  # outcome: 42.0
# outcome: [42.0, 3.5, 3.14, 42.0, 'another one']
example_list + ['another one']
42.0 in example_list  # outcome: True
