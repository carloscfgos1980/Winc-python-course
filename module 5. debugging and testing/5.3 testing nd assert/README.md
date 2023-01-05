## Testing

Testing is an important part of programming. How else would you know for sure if your code works? You've probably been testing a lot while doing exercises for this course, too. We are now going to upgrade our testing situation from running code manually and observing the results, to writing programs that test our code extensively and report the result back to us.

Assert

We will now introduce a new Python keyword: assert. It's much like an if statement; whatever follows assert should be an expression that evaluates to True or False. But there's one difference: if the expression fails, you get an error.

Important

If what comes after assert evaluates to True, nothing happens. -If what comes after assert evaluates to False, an AssertionError is raised.
These two examples are effectively different ways to do the same:

# Using an if-statement
if 1 == 1:
    pass
else:
    raise AssertionError

# Using assert
assert 1 == 1
You can add extra information to your assert statements to help you debug if the assertion fails. The text will be added to the error.

assert 1 == 2, 'Need a calculator..'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AssertionError: Need a calculator..
Pytest
https://docs.pytest.org/en/latest/

A popular tool that makes it easy to write tests using assertions is pytest.

pytest
You can install it using pip. In the following command, -U is an option that tells pip to upgrade pytest to the latest version if you happened to already have a version installed.

pip install -U pytest

You can now run pytest from the command line by typing pytest. It will search for .py files that start with test in the current working directory, and then search for functions that start with test within those files. It probably won't find any if you do it now, though.

Try putting this in a file test_example.py:

def test_example_0():
    assert 1 == 1

def test_example_1():
    assert 1 == 2
Now run pytest. It should report back that one of these tests failed.

In larger codebases there may be hundreds or perhaps even thousands of different tests. You can run them when you modified existing code to test if you didn't inadvertently break anything, and it would be wise to write new tests for newly written code. The higher the test coverage you have in your project, the more confident you (or your company) can be that there are no critical bugs in the program.

To learn more about the many things pytest can do, you could follow pytest's own 'Getting Started' series:

pytest -- getting started
https://docs.pytest.org/en/latest/getting-started.html

# Test Cases

When writing tests, you should always think in terms of test cases. Here's an example:

def initials(name):
    first, last = name.split(' ')
    f, l = first[0], last[0]
    return f'{f}. {l}.'

def test_initials_common_name():
    assert initials('Daniel Radcliffe') == 'D. R.'

def test_intials_double_barrelled():
    assert initials('Helena Bonham Carter') == 'H. B. C.'
Do

It's a good rule of thumb to start with the most common case and work your way down to the least common case. For this example function (initials), most names are probably not that complex -- we can cover a lot of ground with test_initials_common_name But there are double-barrelled names, and then you have your von
Braun s and even international names. As you encounter bugs you didn't think of previously you also write new tests to cover those cases.

The questions to ask yourself are:

What is the testing area? In this case: names.
What are all the unique cases within this area? In this case: different kinds of names.
Don't

Never write logic pertaining to the function you're trying to test in the test case. So don't do something like this:

def test_initials():
    name = 'Daniel Radcliffe'
    first, last = name.split(' ')
    f, l = first[0], last[0]
    assert initials(name) == f'{f}. {l}.'
This makes no sense. Now we have duplicate code and we're not really testing anything; we're only running the same code twice.

Important

Always test logic using cases, not with more logic.