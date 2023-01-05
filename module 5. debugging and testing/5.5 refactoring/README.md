Exercise: Refactoring

wincpy start 9920545368b24a06babf1b57cee44171

Refactoring is rewriting and moving around code without changing any functionality. This sounds like a giant waste of time, right? Wrong! As code bases grow and new functionality requirements come in, you often find that you (or your team) has new insights on ways to structure the code. If done correctly, refactoring will significantly reduce the complexity of the code. This has huge benefits on the time spent fixing bugs, number of newly introduced bugs, time spent introducing (new) team members to (new parts of) the codebase. In this way, refactoring can be seen as a way to pay off technical debt that is accrued over time.

In this exercise we are going to do some refactoring of procedural code into object-oriented code. That is: we are going to take a program that is written in a top-to-bottom manner - with some lists and dictionaries defined and used along the way -, and rewrite it to use classes with instances that interact with each other.

Specialists and Homeowners

We have a start-up that connects homeowners to specialists like painters, plumbers and electricians. We raised millions in venture capital in our series A funding round but our code is still a bit of a mess.

Fortunately there's still time to fix things, as we don't have a lot of users yet. We have three specialists:

Alice the electrician.
Bob the painter.
Craig the plumber.
And three homeowners:

Alfred
Bert
Candice
The code we have so far is in main.py. Make sure you read and understand this code before you continue reading.

There are several problems with this (small) codebase:

We have to manually add a number of variables for homeowners and specialists.
We have to manually add the logic that matches them up every time.
It is very hard to add functionality to this, like a price comparison between different specialists. This is a great example of how technical debt can limit your progress as a company.
This is not ideal, especially as we are about to go viral with our top-notch marketing strategy that we spent a lot of money on. (Way more compared to our software development efforts. shhh).

Your job is to refactor this to object-oriented code. There is no wincpy check because the exercise is about using your creativity to improve and structure this code by yourself. To help you along, we suggest writing a number of classes:

Homeowner
A Specialist parent class with child classes:
Electrician
Painter
Plumber
The end result should be functionally equivalent to the orginal, but one should be able to add a homeowner, painter, plumber or electrician with one line. While you would usually put classes and logic in different files, it is fine to keep it in all in one file for this small project.

Bonus: add the ability to compare different specialist on pricing and automatically contract the best offer for the homeowners.