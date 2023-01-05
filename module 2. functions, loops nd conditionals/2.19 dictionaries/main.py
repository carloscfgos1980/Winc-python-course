# Dictionary

student_ages = {
    'bob': 10,
    'sharon': 9,
    'eli': 10,
    'preeti': 11
}

print(student_ages['bob'])
print(student_ages['eli'])

product = {
    "name": "tofu",
    "price": 2,
    "producer": {
        "name": "Tofu Company Limited",
        "country_of_origin": "France"
    },
}

print(product["producer"]["country_of_origin"])

students = [
    {
        "name": "Ali",
        "family_name": "Khan",
        "skills": {
            "Python": "beginner",
            "JavaScript": "expert",
        },
        "certificates": [
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "",
            },
        ],
    },
    {
        "name": "Jessica",
        "family_name": "van Alphen",
        "skills": {
            "Python": "advanced beginner",
            "JavaScript": "beginner",
        },
        "certificates": [
            {
                "name": "Front-end Development",
                "date_of_completion": "",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "2020-01-17",
            },
        ],
    },
]

print(students[1]["skills"]["Python"])  # "advanced beginner"
print(students[0]["certificates"][1]["name"])  # "Back-end Development"
print(students[0]["certificates"][1]["date_of_completion"])


# Building a Dictionary Incrementally
person = {}
print(type(person))

person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

# Once the dictionary is created in this way, its values are accessed the same way as any other dictionary
print(person)
print(person['fname'])
print(person['age'])
print(person['children'])

# Retrieving the values in the sublist or subdictionary requires an additional index or key:
print('last children:', person['children'][-1])
print('Cats name:', person['pets']['cat'])

'''
This example exhibits another feature of dictionaries: the values contained in the dictionary don’t need to be the same type. In person, some of the values are strings, one is an integer, one is a list, and one is another dictionary.

Just as the values in a dictionary don’t need to be of the same type, the keys don’t either:
'''
foo = {42: 'aaa', 2.78: 'bbb', True: 'ccc'}
print('whole dictionary', foo)
print('first element', foo[42])
print('second element', foo[2.78])
print('third element', foo[True])

# Restrictions on Dictionary Keys
'''
First, a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once.

You saw above that when you assign a value to an already existing dictionary key, it does not add the key a second time, but replaces the existing value:
'''

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
MLB_team['Minnesota'] = 'Timberwolves'

print(MLB_team)

# Built-in Dictionary Methods

# d.clear() empties dictionary d of all key-value pairs:

d = {'a': 10, 'b': 20, 'c': 30}
print(d)
d.clear()
print(d)

# Get
'''
The Python dictionary .get() method provides a convenient way of getting the value of a key from a dictionary without checking ahead of time whether the key exists, and without raising an error.

d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found. If <key> is not found, it returns None:
'''

d = {'a': 10, 'b': 20, 'c': 30}
print(d.get('b'))
print(d.get('z'))

'''
If <key> is not found and the optional <default> argument is specified, that value is returned instead of None:
'''
print(d.get('z', -1))

# d.items

'''
Returns a list of key-value pairs in a dictionary.
d.items() returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the key’s value:
'''

d = {'a': 10, 'b': 20, 'c': 30}
print('d', d)
print('list d:', list(d.items()))
print('print b:', list(d.items())[1][0])
print('print 20:', list(d.items())[1][1])

# d.keys

'''
Returns a list of keys in a dictionary.
d.keys() returns a list of all keys in d:
'''
d = {'a': 10, 'b': 20, 'c': 30}
print('keys in d-dictionary', list(d.keys()))

'''
Any duplicate values in d will be returned as many times as they occur:
'''
d = {'a': 10, 'b': 10, 'c': 10}
print('values:', list(d.values()))

# d.pop(<key>[, <default>])

'''
Removes a key from a dictionary, if it is present, and returns its value.
If <key> is present in d, d.pop(<key>) removes <key> and returns its associated value:
'''
d = {'a': 10, 'b': 20, 'c': 30}

print('pop value of b', d.pop('b'))
print('checkking that b has been remove from the dictionary', d)

'''
If <key> is not in d, and the optional <default> argument is specified, then that value is returned, and no exception is raised:
'''
d = {'a': 10, 'b': 20, 'c': 30}
print('return -1 when the key is not in the dictionary', d.pop('z', -1))

# d.popitem()

'''
Removes a key-value pair from a dictionary.
d.popitem() removes the last key-value pair added from d and returns it as a tuple:
'''
d = {'a': 10, 'b': 20, 'c': 30}
print('dictinary', d)
print('last key and value from the dictionary', d.popitem())
print('dictinary without last key and value', d)

# d.update(<obj>)

'''
Merges a dictionary with another dictionary or with an iterable of key-value pairs.
If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:

If the key is not present in d, the key-value pair from <obj> is added to d.
If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.
Here is an example showing two dictionaries merged together:
'''
d1 = {'a': 10, 'b': 20, 'c': 30, 'z': {'ttt': {'x': 50, 'y': 60}}}
d2 = {'b': 200, 'd': 400, 'z': {'ttt': {'x': 50, 'y': 60}},
      'o': {'ppp': {'x': 50, 'y': 60}}}
print('dictionary without update', d1)
d1.update(d2)
print('updated dictionary:', d1)

'''
Or the values to merge can be specified as a list of keyword arguments:
'''
d1 = {'a': 10, 'b': 20, 'c': 30}
print('dictionary without update', d1)
d1.update(b=200, d=400)
print('updated dictionary:', d1)


def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end=" ")
        print("value =", dic[key])
    else:
        print("Not present")


# Driver Code
dic = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
checkKey(dic, key)

key = 'w'
checkKey(dic, key)
