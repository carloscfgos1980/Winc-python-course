# Strings

One of the most common datatypes to many programming languages is the string, which can contain sequences of characters. In Python the string is called str. You can declare it using single ('), double (") and triple double quotes.

example_one = 'I am a string.'
example_two = "Me too!"
example_three = """I too am a string.
                   I am, in fact, a multiline string!"""
What if the string itself should contain quotation marks? Here's how you do that:

example_one = 'I\'m a string.'
example_two = "I'm a string."
example_three = 'He said: "I\'m a string"'
This shows there are two ways to have quotation marks in strings:

Escape it using the backslash (\) character. Escaping characters instructs the interpreter to use the escaped character as-is, not as some special function (like terminating a string).
Use other quotation marks for the string. You can use ' in a "-string and " in a '-string.
Okay, now we have a new problem: how can we use the escape character (\) in strings? The answer is simple: just escape it -- \\.

There are more characters with special meanings:

\n produces a new line;
\t produces a tab.
Experiment with this in a REPL to learn what all of this means, and how it all works. Just save some strings in a bunch of variables and print them out to see what they do.

Now read the "Strings" part of this page, stop at "Boolean Type...":

Real Python -- Python Data Types: Strings
https://realpython.com/python-data-types/#strings