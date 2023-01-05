Linting and formatting

Most code editors have some tools to help you write good code. VSCode is a popular editor that certainly has a lot built-in and lots more you can pull in from its extension marketplace. Here's a nice guide about writing Python in VSCode you can follow:

Getting Started with Python in VS Code
https://code.visualstudio.com/docs/python/python-tutorial

What follows is an explanation of some terms you will find in this tutorial and around the web regarding making it easier for yourself to write (Python) code.

Formatting

Code formatting specifies how your code (text) is laid out across a file. Python requires you to adhere to quite specific rules regarding whitespace, but there is still a lot left to preference. To improve readability of your code it is nice if a uniform style guide applies. To do that but not add a lot of manual work, formatters exist. For Python in VSCode we recommend:

https://black.readthedocs.io/en/stable/

Black -- The uncompromising code formatter
Black's creators call it opinionated. This essentially means there is not a lot to configure, so not a lot to think about, which means you have more time to think about the actual code you're trying to write.

Install this extension by Microsoft to install Black
https://marketplace.visualstudio.com/items?itemName=ms-python.python

# Linting

Linting goes beyond simply putting your code in another place and gives you hints like:

You declared a variable and then never used it.
You used a variable that is not declared anywhere.
You imported a module and never use it.
You wrote a syntax error, like print'hi').
You used return outside of a function.
You used break outside of a while or for loop.
And much, much more.
We recommend using flake8. Here are some useful resources to do so:
https://www.youtube.com/watch?v=TDUf93vqq3g


Flake8: Your Tool For Style Guide Enforcement
https://flake8.pycqa.org/en/latest/

Linting Python in Visual Studio Code
https://code.visualstudio.com/docs/python/linting