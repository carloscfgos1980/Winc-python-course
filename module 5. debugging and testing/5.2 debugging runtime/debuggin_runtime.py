# Debugging at Runtime

'''
At times you may run into a bug that does not originate from a mistake you made, but rather from some external state that does not match expectations. It is possible to debug such problems with print statements, however it is also possible to use logical breakpoints in the application and to debug the issue at runtime.'''


def fetch_user_snippets():
    user = requests.get(
        'https://run.mocky.io/v3/3b7fdcfc-53b9-43e7-9042-53d1870c8693').json()  # fetch user
    snippets = requests.get(
        'https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json()  # fetch snippets
    snippets = [s['snippet']
                for s in snippets if s['user_id'] == user['meta']['user_id']]
    return snippets


'''
In this case you are dealing with data from an external API; it is possible that the API has changed or just isn't available. For instance, it is possible that the API now stores the id property directly on the user object rather than the meta object as you have assumed. This would raise a KeyError. You could print the response you get to inspect what the API is giving you to figure out a fix. Alternatively you could use a breakpoint:
'''


def fetch_user_snippets():
    user = requests.get(
        'https://run.mocky.io/v3/3b7fdcfc-53b9-43e7-9042-53d1870c8693').json()
    breakpoint()  # halt execution and open a shell
    snippets = requests.get(
        'https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json()
    snippets = [s['snippet']
                for s in snippets if s['user_id'] == user['meta']['user_id']]
    return snippets


'''
Now the execution will halt right after assigning a value to user, in your terminal you will see an interactive Python prompt. This shell, for the most part functions as any other Python shell. At this point in the program you could inspect the user (which is a dict of values) by simply typing the variable name in the shell. snippets is not available yet; the breakpoint is instantiated before that assignment is made. However, from the shell you could manually execute the API request to inspect how the snippets would look.

If we execute the second code block, our pompt whould look something like this:
'''

snippets = requests.get(
    'https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json()
(Pdb)

''' At the prompt we can type user to inspect how the user object looks.'''

snippets = requests.get(
    'https://run.mocky.io/v3/7f76961a-58b0-4ee2-b6a0-3c4faf90f4ed').json()
(Pdb) user
{'user_id': 'uu_87456'}


'''
The shell spawned by breakpoint has a number of special commands. A list of them can be found here. 

The two you will use most frequently are b for break. This halts the execution of the code and terminates the script. Alternatively you could type c for continue, this will resume the execution until the next breakpoint.
https://docs.python.org/3/library/pdb.html

The key benefit of using breakpoint is that it allows you to interactively inspect what is going on at runtime, this is especially useful when dealing with data from external sources.
'''
