Naming Conventions

As we are sure you would agree by now, there are a fair number of things that are hard about writing good code. One of the things that are canonically tricky is naming things.

Does cat stand for 'cat' or 'category'?
Which is better: enabled, is_on or activated? And what is enabled, activated, or on here anyway? Is the variable a string that gives us this information or a boolean that signifies whether the mystery object is 'on' or 'off'?
What do you name a variable that holds the current time but with tomorrow's date? Perhaps datetime_tomorrow. What if you're also working with different timezones? datetime_tomorrow_utc_plusone, dt_tomorrow_utc_plusone or utc_1_datetime_tomorrow?
While in many cases there may be some options that are clearly wrong, it is not always obvious which name is the best. The thing to keep in mind that is that the variable, function (and later: class) names are for yourself and your colleagues to read and understand. Often times the names don't seem to matter a lot at the time, but consider:

The code needs to be readable so that your future self -- who surely won't remember writing it -- and colleagues can easily and quickly understand it.
The code needs to be maintainable so that future updates can be made effectively without names quickly clashing or becoming outdated.
Famous computer scientist Donald Knuth put it nicely:

Programs are meant to be read by humans and only incidentally for computers to execute.
Style Guides

The Python Software Foundation, the non-profit that supports the Python programming language, has an official style guide that is useful to read when you have the time.

PEP 8 -- Style Guide for Python Code
Here are two of the most important points we recommend you adhere to:

Use snake case for variable and function names. Snake case means: lowercase variables where would-be spaces are replaced by underscores (_).
winc_academy
question
answer_options
Separate variables and operators with spaces, except in function calls.
answer = 2 * 21
answer = get_answer(question='What time is it?')
Note

Not all words are available for use in your code. Some words are reserved, they are keywords claimed by Python itself. Try this in a REPL:

False = 'test'
for = 'test'
pass = 'test'
For a list of all reserved keywords, type this in a REPL:

import keyword
keyword.kwlist
You can also find the keywords here:

Python Docs -- 2.3.1. Keywords

https://docs.python.org/3.8/reference/lexical_analysis.html#keywords