Function Arguments

Default Parameters

Say we define a function to get the weather report:

def weather_report(day):
    print(f'Here is the weather for {day}')
    # get the weather report from somewhere
    # ...
    return info

weather_report('today')
It might be the case that we usually want the weather for today. In this case we can define a default for the date parameter. The day-parameter is now optional. It's not required when calling the function.

def weather_report(day='today'):
    print(f'Here is the weather for {day}')
    # get the weather report from somewhere
    # ...
    return info

weather_report()
If we then want tomorrows weather we can override the default by supplying the optional argument.

def weather_report(day='today'):
    print(f'Here is the weather for {day}')
    # get the weather report from somewhere
    # ...
    return info

weather_report('tomorrow')
Keyword Arguments

You can improve readability of your code in cases where you do a function call from which it is not immediately clear what each argument means by specifying the parameters as keyword arguments.

# Without keyword arguments.
send_email('bob@example.com',
           'preeti@example.com',
           'eric@example.com',
           'Thanks for the cake!')

# With keyword arguments. Much clearer.
send_email(sender='bob@example.com',
           to='preeti@example.com',
           cc='eric@example.com',
           msg='Thanks for the birthday cake!')
Read more:

Real Python -- Keyword Arguments

https://realpython.com/defining-your-own-python-function/#keyword-arguments