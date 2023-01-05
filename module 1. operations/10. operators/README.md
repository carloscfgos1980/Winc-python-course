## Operators

In the unit about strings we briefly mentioned the terms operator and operand. We discuss them a bit more in-depth here, but please don't trouble yourself with trying to learn this by heart. It's more important to understand the underlying regularities and then keep the reference material in your back pocket.

Arithmetic

Here are some of the operators available to us in Python to do arithmetic:

Arithmetic Operators
Operator	Operation	Example
+	Addition	3 + 2
-	Subtraction	3 - 2
*	Multiplication	3 * 2
/	Division	3 / 2
%	Modulo	3 % 2
**	Exponentiation	2 ** 3
//	Floor division	3 // 2
About Operators in general

All of the operators in the table above are infix binary operators. This sounds complicated, but let's break it down so we can understand this word for word:

Operation: very general term -- doing something with something.
Operator: a symbol (one or more characters) that signifies the operation.
Operand: one of the items that the operation is done on.
Infix: the operator sits in between its operands.
Binary: the operation works with two operands.
For example: in 3 / 2 the operation is 'division' because we see a specific operator: the division sign (/). This operator sits in between the two operands 3 and 2. These are the only two values it takes in, making it a binary operator.

As we've seen before in the unit about strings, not every combination of operators and operands is valid. For example, what should 'Hi' / True mean? The quickest way to find out if something works the way you think it does is to try it out in a REPL.

One of the combination that works is string + string. Perhaps, you find it quite logical that it should concatenate (glue together) the strings (which is indeed what it does), but if you think about it: not too long ago you may not have known about strings at all! You only used addition with numbers, but now you're also using it with this new datatype (the Python str) with the familiar operator (the +-operator). The name for reusing operators with new datatypes is called operator overloading.

Relational Operators

In addition to arithmetic operators there are also a number of operators that tell us something about the relation between two values.

Relational Operators
Operator	Operation	Example
==	Equality	2 == 3
!=	Inequality	2 !=3
<	Less than	2 < 3
>	Greater than	2 > 3
<=	Less than or equal to	2 <= 3
>=	Greater than or equal to	2 >= 3
And then we also have the logical operators:

Logical Operators
Operator	Operation	Example
and	True if both operands are true	True and False
or	True if either one of the operands are true	True or False
not	negation; reverses the truth value of its operand	not True
What's interesting about the not operator is that it has only one operand, so this operator is what we call a unary operator.

Unlike arithmetic operators -- which can return a host of datatypes like numbers and strings -- these relational operators produce only the Boolean values True or False. For example, try this in a REPL:

True is False
True or False
not True
not False
== is not is

You may have noticed we now have two operators that compare two things and return a boolean: == and is. What's the difference? The technical explanation is:

is will return True if the operands point to the same object
== will return True if the operands point to objects that are equal
If this makes sense for you: great, you can work with this knowledge. If not: don't worry about it and follow this rule of thumb:

Use is only if what follows it is a boolean.
# Followed the rule of thumb:
'Example' is True
# Did not follow the rule of thumb:
'Example' is 'incorrect'
# Followed the rule of thumb:
'Example' == 'correct'
As usual, here's a longer-form explanation of this material where you can also find a number of extra operators. There's no need to memorize them, you will learn to use them over time when needed. Some you might never use!

Real Python -- Operators and Expressions in Python

https://realpython.com/python-operators-expressions/