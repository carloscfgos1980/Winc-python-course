Exercise: Dictionaries

wincpy start 00a4ab32f1024f5da525307a1959958e

As you may know, governments are often strapped for programming talent. But you're coming to the rescue! You are going to write a tool that creates and checks passport information.

We already supplied a list of countries in countries.json and a function get_countries in helpers.py that fetches and returns this list.

Part 1: Create Passport

Write in main.py a function create_passport that takes as its arguments, in this order:

A name (str)
A date of birth (str in ISO 8601 format, for example: 2002-12-31)
A place of birth (str)
A height in meters (float)
A nationality (str)
And returns a passport dict containing this information with the keys:

name
date_of_birth
place_of_birth
height
nationality
Note:

We express a nationality as a country (str) from the list returned by get_countries.
Part 2: Add Stamp

Whenever a person travels to another country, they get a stamp in their passport that shows that they have been there. Implement add_stamp in main.py, which takes as its arguments, in this order:

A passport (dict) like the one returned by create_passport
A country (str)
And:

Adds or updates a key-value pair:
(key) 'stamps'
(value) a list of countries (str) that the person has been to.
Finally: add_stamp returns the (possibly) stamped passport.
Note:

Any stamp may be a person's first stamp, in which case the 'stamps' key in their passport dict is not present yet. You will have to create it in that case. But beware not to overwrite people's existing stamps list!
Travellers don't need stamps of their home country.
No duplicate stamps! If a traveler already has a stamp for a country, don't give them another stamp.
Part 3: Add biometric data

Passport technology advances and security has become more of a concern for a lot of countries. Quite a few countries have added "biometric data" to passports. See this Wikipedia article for more information (you won't need that for this exercise).

Because the software you're writing will be used by different countries that want to add different kinds of biometric data your code needs to be able to handle all kinds of different biometric data.

Write a function add_biometric_data in main.py that takes as its arguments, in this order:

A passport (dict) like the one returned by create_passport
A name (str) for the type of biometric data that will be added.
The value, or values of the to-be-added biometric data.
A date in ISO format YYYY-MM-DD (str) for when the biometric data was recorded.
The biometric data should live in a dictionary inside of the passport. In other words: a nested dictionary. The key for the biometric data dictionary is biometric.

The function should return:

If the passport did not yet have any biometric data: add the key for it, you can assume you'll only get passports with a chip to save biometric data.
If the type of biometric data was not yet in the passport: add it to the passport.
The value for the specific type of biometric data should again be a dictionary (so nested again). This dictionary should have two keys: date and value. See examples below for specific examples.
If the type of biometric data was already in the passport: update the biometric data in the passport, overwriting the previous value and date.
Examples:

omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
print(omari)
```
{
  'name': 'Omari Muchumba', 
  'date_of_birth': '1995-07-16', 
  'place_of_birth': 'Kampala', 
  'height': 184.31, 
  'nationality': 'Uganda', 
  'biometric': {
    'eye_color_left': {
      'date': '2020-05-05',
      'value': 'blue'
    },
    'eye_color_right': {
      'date': '2020-05-05',
      'value': 'blue'
    }
  }
}
```

# Omari gets a new left eye because of an accident
omari = add_biometric_data(omari, "eye_color_left", "brown", "2022-01-10")
print(omari)
```
{
  'name': 'Omari Muchumba', 
  'date_of_birth': '1995-07-16', 
  'place_of_birth': 'Kampala', 
  'height': 184.31, 
  'nationality': 'Uganda', 
  'biometric': {
    'eye_color_left': {
      'date': '2022-01-10', 
      'value': 'brown'
    },
    'eye_color_right': {
      'date': '2020-05-05',
      'value': 'blue'
    }
  }
}
```

# Add fingerprints too: just another value, but this is also a dict.
fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}
omari = add_biometric_data(omari, "finger_prints", fingerprint_data, "2022-01-12")
print(omari)
```
{
  'name': 'Omari Muchumba', 
  'date_of_birth': '1995-07-16',
  'place_of_birth': 'Kampala', 
  'height': 184.31, 
  'nationality': 'Uganda', 
  'biometric': {
    'eye_color_left': {
      'date': '2022-01-10', 
      'value': 'brown'
    },
    'eye_color_right': {
      'date': '2020-05-05',
      'value': 'blue'
    },
    'finger_prints': {
      'date': '2022-01-12',
      'value': {
        'left_pinky': '2378945', 
        'left_ring': '2349081', 
        'left_middle': '132890', 
        'left_index': '9823234', 
        'left_thumb': '0924131', 
        'right_thumb': '6234923', 
        'right_index': '13249734', 
        'right_middle': '34023784', 
        'right_ring': '12332538', 
        'right_pinky': '32458970'
      }
    }
  }
}
```
Wincpy Check

Use wincpy check dictionariesv2 to see if you met all of the requirements for this exercise. Did you pass the test?