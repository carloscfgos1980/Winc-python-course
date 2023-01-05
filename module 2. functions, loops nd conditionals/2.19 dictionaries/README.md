Dictionaries

A Python dictionary (dict) or "dict" for short is a collection of key-value pairs. Let's look at an example before we unpack that technical statement. Try out this code:

student_ages = {
    'bob': 10,
    'sharon': 9,
    'eli': 10,
    'preeti': 11
}

print(student_ages['bob'])
print(student_ages['eli'])
Here, a student's name is the key and their age is the value. We call a key and its corresponding value a key-value
pair, and dictionaries hold a collection of them. So: a dictionary (dict) is a collection of key-value pairs.

The fact that we access values in the dictionary by key has one great advantage over lists: if we're looking for a specific item in a list we have to loop over it until we find it, but with a dict we can get it in one-shot by specifying the key.

Possible values

You can put all kinds of values into dictionaries. Just like you can in lists by the way. You can put in:

booleans
numbers
strings
lists
other dictionaries (!)
functions
and more..
When you put a more complex data structure (like a list or dictionary) as a value into another data structure we call this "nesting". Here's a dictionary inside of another dictionary for example. Included is an example of how to access values inside nested data structures.

product = {
    "name": "tofu",
    "price": 2,
    "producer": {
        "name": "Tofu Company Limited",
        "country_of_origin": "France"
    },
}

print(product["producer"]["country_of_origin"]) # "France"
We can nest however deep we want. We could have a dict with a list in it, with multiple dicts in it that themselves contain other dicts. This makes data structures like this able to "model" information in the real world. Here's a more complicated example, including accessing these data structures:

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
Further reading

Read this page on dictionaries to learn when and how to use them:

Real Python -- Dictionaries in Python

https://realpython.com/python-dicts/