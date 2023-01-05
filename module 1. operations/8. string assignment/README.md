# Assignment: Strings

wincpy start 71dd124b4a6e4d268f5973db521394ee

You need to master the following to complete this assignment:

Printing text and variables;
Casting types to other types;
Using and manipulating strings.
We're going to do some reporting on a soccer match: the UEFA Euro 1988 Final, which was (at the time of writing) the last time the Dutch team became the champions. You can find all the information you're going to need on Wikipedia:

UEFA Euro 1988 Final
Part 1

Create a variable for every player that scored, for example:

example = 'Gut von Examplestein'
Create a variable for each minute of the match that a goal was scored in, for example:

goal_0 = 32
Using the +-operator, create a string that reports on who scored when, according to the format:

<scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
The result should be stored in a variable scorers

Use f-strings or the +-operator to create a single string with information about who scored when in the format:

<scorer_name> scored in the <when_they_scored>nd minute
<scorer_name> scored in the <when_they_scored>th minute
The result should be stored in a variable report.

Tip

The character to create a new line, aptly named the newline character, is '\n'. Also: beware that it's 32nd and 54th!

Part 2

Store the following values in the given variable. You can create temporary variables, like last_name to help you.

Choose a player that played in the soccer match and store his name as a string in the variable player.

first_name: use slicing and the find-method (help) to isolate and store the player's first name.

last_name_len: use find, slicing and len to isolate and store the length of their last name.

name_short: isolate and store the player's name in this format:

G. von Examplestein
chant: this is what the crowd chants when it looks like your player is going to score a goal -- their first name plus an exclamation mark(!), x-times, where x is the number of characters in their first name. Because Gut has 3 letters in his name, we repeat his name 3 times. Make sure the last character of this string is not a space! For our example player:

Gut! Gut! Gut!
good_chant: Make super-sure the last character of chant is not a space by using the inequality operator (!=). This variable needs to be a boolean, not a string. You can create the value for this variable by comparing the last character of chant with a space character. Try this in your REPL for an example: print(2 != 3). Also try: print(2 != 2).

Wincpy Check

Use wincpy check strings to see if you met all of the requirements for this assignment. Did you pass the test?