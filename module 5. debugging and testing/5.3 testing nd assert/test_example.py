# Assert

'''
We will now introduce a new Python keyword: assert. It's much like an if statement; whatever follows assert should be an expression that evaluates to True or False. But there's one difference: if the expression fails, you get an error.
'''
# These two examples are effectively different ways to do the same:

# Using an if-statement
if 1 == 1:
    pass
else:
    raise AssertionError

# Using assert
assert 1 == 1


def test_example_0():
    assert 1 == 1


def test_example_1():
    assert 1 == 2

# Test Cases
# When writing tests, you should always think in terms of test cases. Here's an example:


def initials(name):
    name_length = len(name.split())
    if name_length < 2:
        raise ValueError
    elif name_length > 2:
        splitted_name = name.split(' ')
        first = splitted_name[0]
        last = splitted_name[2]
        f, l = first[0], last[0]
        return f'{f}. {l}.'
    else:
        first, last = name.split(' ')
        f, l = first[0], last[0]
        return f'{f}. {l}.'


def test_initials_common_name():
    assert initials('Daniel Radcliffe') == 'D. R.'


def test_intials_double_barrelled():
    assert initials('Helena Bonham Carter') == 'H. C.'


'''
Do

It's a good rule of thumb to start with the most common case and work your way down to the least common case. For this example function (initials), most names are probably not that complex -- we can cover a lot of ground with test_initials_common_name But there are double-barrelled names, and then you have your von
Braun s and even international names. As you encounter bugs you didn't think of previously you also write new tests to cover those cases.

The questions to ask yourself are:

What is the testing area? In this case: names.
What are all the unique cases within this area? In this case: different kinds of names.
'''
######
'''
Don't

Never write logic pertaining to the function you're trying to test in the test case. So don't do something like this:
'''


def test_initials():
    name = 'Daniel Radcliffe'
    first, last = name.split(' ')
    f, l = first[0], last[0]
    assert initials(name) == f'{f}. {l}.'


'''
This makes no sense. Now we have duplicate code and we're not really testing anything; we're only running the same code twice.
'''


# Group multiple tests in a class
'''
Once you develop multiple tests, you may want to group them into a class. pytest makes it easy to create a class containing more than one test:
'''
# content of test_class.py


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
