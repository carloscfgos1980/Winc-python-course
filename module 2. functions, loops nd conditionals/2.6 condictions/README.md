## Conditions

It's time to make our code a little smarter. So far, we've only written programs where each statement is always executed unless it was a comment. We also had reusable instruction sequences in functions, but now we also want to execute code based on some conditions.

Imagine we are writing code to help in the process of an election that is coming up. We want to let everyone who is eligible to vote know that an election is coming up. Our task is to write the function eligible_to_vote, which takes an age and nationality and returns a boolean that signifies whether a person is eligible to vote or not. Here's the empty function:

def eligible_to_vote(age, nationality):
    return True
Well, this is clearly wrong. It's always going to return True. We can add some conditions by using the keywords if and else:

def eligible_to_vote(age, nationality):
    if age >= 18:
        return True
    else:
        return False
This is better. But we haven't verified their nationality yet. We are writing this code for the country of Italy, so we need to check if the nationality matches. There are two ways of doing this. The first one is nesting conditions:

def eligible_to_vote(age, nationality):
    if age >= 18:
        if nationality == 'Italian':
            return True
        else:
            return False
    else:
        return False
This approach works, but we can do better. We can reduce the number of lines and indentation levels by using the keyword and:

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    else:
        return False
Note

Extra: we can really make Donald Knuth proud by going one step further:

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    return False
Why are we able to leave out else here? Recall that a function does not proceed in executing its code after hitting a return statement, it immediately returns whatever we asked it to return.

We delivered the function and the government of Italy was satisfied with our work. However, voting laws were abruptly changed. This year, they will allow their Portuguese friends to vote in their election as well, but only from age 25. We find this very strange and somewhat confusing, but we're not ones to argue. Plus: it gives us an opportunity to introduce the elif keyword:

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    elif age >= 25 and nationality == 'Portuguese':
        return True
    else:
        return False
We can chain elif statements together indefinitely in case Italy decides to change their voting laws again, and we are also not limited to return statements either. Any valid Python code is allowed -- just make sure the indentation level is correct:

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        print('Bene!')
        return True
    elif age >= 25 and nationality == 'Portuguese':
        print('Sim!')
        return True
    elif age >= 31 and nationality == 'Dutch':
        print('Top!')
        return True
    elif age >= 19 and nationality == 'Malawian':
        print('Iya!')
        return True
    else:
        return False
To read more about if, else and elif, see:

Real Python -- Conditional Statements in Python

https://realpython.com/python-conditional-statements/#introduction-to-the-if-statement