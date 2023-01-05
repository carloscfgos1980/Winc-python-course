## Reference and Mutability

Reference

Read this up to (not including) "Python Diversity":

Ned Batchelder -- Facts and myths about Python names and values
Mutability

https://nedbatchelder.com/text/names.html

As you now know, a variable is not an object. A variable points to an object. What object a variable points to can always be changed:

a = 'one'
a = 1
a = 42
a = 3.14
a = 'hi'
This leads us to the concept of mutability, which specifies whether or not the underlying object itself can be modified.

a = 'one'
a[0] = 42
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
Here we tried to change a part of the str-object that the a variable points to. This resulted in an error because str is not mutable. It does work for a list:

a = ['one', 'two', 'three']
a[0] = 42
Here's an overview for which types are mutable and which are not. As always, don't bother learning this by heart. Just look it up or try it in a REPL when you need to.

Type	Mutable
bool	no
int	no
float	no
list	yes
tuple	no
str	no
dict	yes