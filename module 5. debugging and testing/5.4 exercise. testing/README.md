Exercise: Testing

This is it! We are letting go of wincpy check. From now on, you will be writing your own tests. This exercise helps you on your way.

One popular method for writing good code is to first write the tests, and only then write the function that should pass those tests. This way of doing software development is called Test-Driven Development (TDD), and it's the way this exercise will be structured.

First, create a simple folder structure to work with, for example:

 testing
├── main.py
└── test_main.py
Part 1

In test_main.py, write a function test_get_none that tests if a function from main.py called get_none returns None.
In main.py, write the function get_none that should take no arguments and always return None.
This dummy example is a practical application of test-driven development; first we write the test, then the function that is being tested.

Part 2

In test_main.py, write a function test_flatten_dict that tests if a function flatten_dict, when given a dictionary (dict) as its argument, returns the values of that dictionary in a list (list). For example:

flatten_dict({'a': 42, 'b': 3.14})
# [42, 3.14]
flatten_dict({'a': [42, 350], 'b': 3.14})
# [[42, 350], 3.14]
Tip

Try to think about the tests you're writing as a tiered system. First you might test if the value returned by flatten_dict is a list at all. Then you could test the function with a very small (single element) dictionary, then more complex dictionaries. This way, if a test fails, you not only now that it fails, but also exactly where it fails. The more granular your testing tiers, the better you can trace the bug if the test fails.

In main.py, implement the function flatten_dict so that it passes the tests you wrote in test_flatten_dict. Another example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [{'inner_a': 42, 'inner_b': 350}, 3.14]
Run the tests you wrote with pytest as you are working on the implementation of the flatten_dict function.

Note

For an extra challenge, see if you can implement flatten_dict in such a way that the dictionary is flattened all the way down regardless of how many nested levels original dictionary contains. For example:

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
# [42, 350, 3.14]
flatten_dict({'a': [{'inner_inner_a': 42}]})
# [42]
To do this you may want to look into a technique that is called recursion.