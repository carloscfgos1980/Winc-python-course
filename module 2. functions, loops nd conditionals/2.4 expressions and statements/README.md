Expressions and Statements

An expression is something that represents a value. For example:

# Represents 2
1 + 1

# Represents "Hello, Preeti!'
greet('Preeti')
A statement is any complete instruction that the Python interpreter can execute. Statements can consist of one or more expressions. For example: number = 3 is one statement, and so is this:

number = (1 + 2 + 3 +
     4 + 5 + 6 + 
     int('5'))
Ambiguity in Natural Languages

Preeti: One coke, please.
Cashier: small, medium or large?
Preeti: yes.
Cashier sighs
The cashier sighs because Preeti intentionally picked the wrong one from these two possible interpretations of the cashier's question:

(small), (medium) or (large)?
(small, medium or large)?
In interpretation A, the 'or' is exclusive. The question is: "which one of these three options would you like?" Preeti jokingly used interpretation B, where the question turns into: "Would you like one of these three?". By jumbling the expressions, Preeti changed the meaning of the cashier's statement.

These kinds of little ambiguity problems arise all the time in natural languages. In programming languages, however, there are rules to remove any and all ambiguity from the equation. The most important one is precedence.

Precedence

The concept of precedence in programming works much like it does in mathematics: if you have addition (+) and multiplication (*) in the same statement, multiplication binds more strongly.

>>> 1 + 2 * 3
7
>>> (1 + 2) * 3
9
In Python, parentheses (( )) are the most binding. Next in line is the indexing operator ([ ]). Here's the rest of the hierarchy ordered from most to least binding, limited to the terms that we discussed so far. As usual, don't trouble yourself with learning this by heart. Just scan this list to see if anything catches your eye, and know that it is there for later reference.

Operator	Description
( )	Parenthesizing
[ ]	Indexing/slicing
**	Exponentiation
*, /, //, %	Multiplication, division, floor division and modulus
+, -	Addition and subtraction
in, is, <, ==, !=, etc.	Relational operators and tests for membership
not	Boolean NOT
and	Boolean AND
or	Boolean OR