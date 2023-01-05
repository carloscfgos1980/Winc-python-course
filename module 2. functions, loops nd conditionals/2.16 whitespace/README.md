Whitespace

In languages like JavaScript and C, whitespace only serves to separate names and operators. You could write an abomination like this you wanted to:

#include <stdio.h>

// Abomination
void main (void){for(int i;i < 9;i++){printf("Hey!\n");printf("Ho!\n");}}

// Normal way
void main (void) {
    for (int i; i < 9; i++) {
        printf("Hey!\n");
        printf("Ho!\n");
    }
}
To the compiler these two versions are the same. The whitespace doesn't matter.

In Python this is not the case. Try this in a REPL and see what it says:

for i in range(9):
print('Hey!')
print('Ho!')
It's missing an indented block! The identation is how the Python interpreter knows which code belongs inside the for loop and which code belongs outside of it.

print('Start')
for i in range(9):
    print('Hey!')
    print('Ho!')
print('End')
To read more, see:

AskPython -- Python Indentation
https://www.askpython.com/python/python-indentation

Indentation in the Python REPL

The standard Python REPL will change its prompt from >>> to ... when it expects an indent.
You have to manually enter the indentation and repeat that indentation for each subsequent line you want to have at that indentation level.
To complete an indented block, use 'enter'.