Debugging

You wrote a program, but somewhere along the way there's an error, or worse: the end result just doesn't match your expectation and you have no idea why. Either way, you have a bug in your code. Legend has it this term comes from a literal bug messing with the electronics of one of the first computers. In any case: we want to get rid of these bugs.

There are in fact programs that can help you debug your code. In time you will learn to use these sorts of programs, but they don't change what is at the core of how debugging works:

Identify the direct cause of the crash.
Check your assumptions
Fix the bug.
Direct Cause

Take this code snippet:

'Example' + 42
It results in a TypeError. On looking up what a TypeError is we find this page with the following information:

Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
So the direct cause of the bug is that we are trying to add an int to a str, which doesn't make any sense and results in an error.

Now take this code snippet:

def example_function(a, b):
    return a + b

example_function('Example', 42)
Here the cause is more ambiguous. Is example_function at fault for not implementing the addition correctly, or should we modify the call to that function on the last line? This depends on various things: where else is example_function used, and what do we eventually want this program to do? In any case: the direct cause is still the same: we are adding an int to a str, and this does not make any sense.

It is always important to find the direct cause for a bug. Only then we can reason about the best way to fix it.

Checking Assumptions

In any moderately-sized program you will use a number of functions or classes that you didn't write, or you wrote them a long time ago. In this case your assumptions about what each piece of code does might not always be correct.

def chat(identifier, message):
    user = get_user(identifier)
    user.say(message)
Say you were part of a team working on a chat application and you were asked to work on this code snippet. The message sent should now start with the name of the person who sent it followed by a colon, and then the message. So 'Yeah, I agree.' should become: 'Bob: Yeah, I agree.'. Simple, right?

def chat(identifier, message):
    user = get_user(identifier)
    user.say(user.name + ": " + message)
But unfortunately that doesn't work: user.name was the user's last name, and message was not a string but a dictionary containing all sorts of information pertaining to the message. You can imagine this quick fix resulted in a lot of errors. The real fix was:

def chat(identifier, message):
    user = get_user(identifier)
    message['text'] = user.first_name + ": " + message['text']
    user.say(message)
The lesson learned? Check your assumptions! You can test the various moving parts of code using print statements (possibly combined with type) to find out what's happening. Python's way of doing types is very powerful and flexible, but mistakes such as these are easily made as well.