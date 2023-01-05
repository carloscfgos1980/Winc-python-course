Ternary Operator

This one is short and neat. In Python, you can use conditions in any expression. For example, try this in a REPL:

nice_weather = False
going_outside = True if nice_weather else False
print(going_outside)
You are not limited to booleans.

nice_weather_odds = .7
party_location = 'inside' if nice_weather_odds < .6 else 'in the yard'
It's a nice way to improve readability of your code if used the right way.

This syntax allows us to quickly test a condition instead of a multiline if-statement. Often times it can be immensely helpful and can make your code compact but still maintainable.

Danger

Constructs like these are very powerful, but with great power comes great responsibility. Don't overuse it! Even though this statement is valid Python code, it clearly went overboard with ternary operators:

party_location = 'inside' if 1 + 2 == 5 or 3 ** 3 == 9\
                  else 'yard' if bool(2//5) is True else\
                  False if True else 'restaurant'