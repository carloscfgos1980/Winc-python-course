Booleans

The boolean is a (data)type in Python that can only have two values: True and False (notice the capitals).

is_raining = True
sun_is_shining = False
team_a_wins = True
team_b_wins = False
We can create boolean values ourselves, but certain operators in Python can also produce boolean values. You can learn more about those operators in the lesson on operators.

These are a few examples:

5 > 4 # True
5 < 4 # False
3 == 3 # True
Naming boolean variables

Naming variables can be hard. Because a boolean value can only be True or False a helpful trick is to think of a name that says something which can be true or not. For example:

is_raining = True
sun_is_shining = False
team_a_wins = True
team_b_wins = False
If you can: try not to use "negative" names like not_raining. If you use negative names it often becomes harder to reason about your code, because then your code can have "double negatives". In this code sample we say that not_raining is False which means it's not not(!) raining, so it is raining. To prevent your head from exploding: try not to use "negatives" in naming your boolean variables.

not_raining = False
Good variable names for boolean values:

game_is_over
user_is_active
engine_on
is_subscribed
has_friends
payment_done
Bad variable names for boolean values:

game_state
active_user
engine_not_running
subscription
friends
payment
Boolean context

Some statements in Python have a boolean context, which means the computer will try to cast (convert) a value into a boolean value.

One example is the if statement (more information on that in the lesson on conditions).

if some_kind_of_value:
    print("the expression results in a truthy value")
The if-statement here expects a boolean value. If it gets something that is not a boolean it will try to cast (convert) it to a boolean value. Internally it uses bool() to do this. So if you want to find out if (for example) an empty string is cast to True or False you can try it out yourself:

bool("") # False
bool("hi mom") # True
The rules for this conversion are logical but sometimes can be surprising. So for clarity it can often help to create the boolean value yourself.

For example:

string_a = ''
string_b = 'foo'

# Nothing is printed because an empty string is converted to False
if string_a:
    print("expression results in a truthy value")

# The print line is executed because a non-empty string is converted to True
if string_b:
    print("expression results in a truthy value")

# This is more clear
# The print line is not executed
if string_a != "":
    print('string_a != ""')

# This is more clear
# The print line is executed
if string_b != "":
    print('string_b != ""')
To summarize: in a boolean context (like an if statement) it's usually more clear to work with actual boolean values.

Now read this page until the "Functions can Return a Boolean" section.