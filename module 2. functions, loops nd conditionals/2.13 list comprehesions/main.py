example_names = ['Anna Ansville', 'Bob Bobsville', 'Carla Carlsville']

example_last_names = []
for name in example_names:
    example_last_names.append(name.split(' ')[-1])


# List comprehesion

example_last_names = [n.split(' ')[-1] for n in example_names]
