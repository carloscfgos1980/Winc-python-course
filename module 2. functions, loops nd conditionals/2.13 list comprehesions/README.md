List Comprehensions

You know about the for-loop.

example_names = ['Anna Ansville', 'Bob Bobsville', 'Carla Carlsville']

example_last_names = []
for name in example_names:
    example_last_names.append(name.split(' ')[-1])
If a for-loop does not contain a lot of instructions, you may be able to simplify it using a list
comprehension.

example_names = ['Anna Ansville', 'Bob Bobsville', 'Carla Carlsville']
example_last_names = [n.split(' ')[-1] for n in example_names]
To learn more about how list comprehensions work, read this page up to (so excluding) 'Using Set and Dictionary Comprehensions':

Real Python -- Using List Comprehensions
https://realpython.com/list-comprehension-python/