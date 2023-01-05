Exercise: For

wincpy start c545bc87620d4ced81cbddb8a90b4a51

Intro

After executing wincpy start you should find that the created directory for holds three files:

countries.json

This holds some data that you need to use in the exercise. It is good practice to separate data from logic, so we put it in its own file. You don't need to know how this works yet, but if you are interested you could Google for 'JSON file'.

helpers.py

Here we defined a function to help you on your way with getting the data from countries.json into your Python script.

main.py

We import the helper function get_countries from helpers.py into main.py. That means this function is available in the rest of the main.py. The function returns a list of country name strings. You do not need to call this function in the code you write, we've already put the single necessary call to this function inside of the if block at the bottom.

Danger

Do not modify countries.json or helpers.py. These files contain data and code that you need to complete the exercise and may break if changed.

Instructions

Implement these functions in main.py:

shortest_names: takes a list of country names and returns a list of country names that have the shortest length. If there is only one country with the shortest name the list will contain only that country name, otherwise multiple countries should be in the list. Use a for-loop and len!
most_vowels: takes a list of country names and returns a list with the top three countries that have the most vowels in their name. The country with the most vowels should be on position 0 in the list, the country with the second-most on position 1, and so on. If there are multiple countries with the same number of vowels the order does not matter. To sidestep the y-issue: we count aeiou as vowels.
alphabet_set: takes a list of country names and returns a list of country names whose letters can be combined to form the complete alphabet. How short can you get your list to be?
Letter case is not relevant, so 'a' is the same letter as 'A' with regards to the alphabet.
Solutions with 14 or fewer countries are accepted as correct.
You should write your functions before the if statement at the end of main.py. You can call these functions in the code block of that if statement.

Wincpy Check

Use wincpy check for to see if you met all of the requirements for this exercise. Did you pass the test?