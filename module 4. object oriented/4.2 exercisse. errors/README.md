Exercise: Errors

wincpy start 534d85ea1ab14924a91f9eccf6f3f30d

One of the many ongoing discussions within programming is Look Before You Leap (LBYL) versus Easier to Ask for Forgiveness than Permission (EAFP). The classic example to illustrate this discussion is a situation where you need to check a dictionary for the presence of a key.

ages = {'Alice': 21, 'Bob': 42}
# Look before you leap (LBYL)
if 'Charlie' in ages:
    print("Charlie's age:", ages['Charlie'])
else:
    print("I don't know what Charlie's age is.")

# Easier to ask for forgiveness than permission (EAFP)
try:
    print("Charlie's age:", ages['Charlie'])
except KeyError:
    print("I don't know what Charlie's age is.")
Which one do you like better? On one hand, you might find the LBYL implementation more readable. On the other hand, it uses two dictionary look-ups to print Charlie's age, while the EAFP implementation needs only one. But the error handling also incurs some overhead. Is EAFP still faster if you factor that in?

Whichever one you prefer, in this exercise you will convert some LBYL code to EAFP code. Run the wincpy start command at the top of this page to obtain the starting point, where there are three functions implementated LBYL-style. Convert them all to EAFP-style implementations without changing the functionality.

Tip

The EAFP version of these functions should all make use of a try..except statement. A good way to learn what error you need to catch is to just try the code you would like to run in most cases. Then read the error message. You'll want to look for something like:

ValueError: This is a value error.
Wincpy Check

Use wincpy check errors to see if you met all of the requirements for this exercise. Did you pass the test?