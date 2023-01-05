# Error: you asked us to add a string and a number, but this is just not a thing."
# print('Hey!' + 1)

# this is supported:
print('Hello, ' + 'world!')
print('Jump! ' * 5)

# One very useful operator is the membership operator: in.
print('Samuel' in 'We went out for dinner with with Anne, Samuel and Bob.')
print('Shane' in 'We went out for dinner with with Anne, Samuel and Bob.')
# print(5 in 'We were lucky that they had a table for 5.')
print(str(5) in 'We were lucky that they had a table for 5.')


# To compare values we have the ==-operator, which works for numbers, but also for strings:

'Me' == 'Me'
'You' == 'Me'
'Me' == 'me'

'''
What if we don't want the whole string, but just one character from it? The solution is to index into the string. 
'''

letter_grades = 'ABCDF'
print(letter_grades)
print(letter_grades[0])
print(letter_grades[3])


# An expansion on indexing is slicing.

waltz = 'onetwothree'
print(waltz)
print(waltz[0:3])
# We don't need to specify the 0 if we start at the beginning
print(waltz[:3])
print(waltz[3:6])
print(waltz[6:11])
# Same goes for the end -- we can leave it empty
print(waltz[6:])
# We can specify a step size if we don't want a continuous slice
# The pattern here is waltz[start:stop:step]. . Note that the stopping point itself is not included in the slice.
print(waltz[0:11:2])


# When we need the length of a string we have the len-function:
sentence = 'The length of this string is:'
print(sentence, len(sentence))
print('Wait.. You just made it longer!')


# If we want to insert a variable into a string we do it like this:
answer = 42
qa = f'The answer is.. {answer}'
print(qa)
