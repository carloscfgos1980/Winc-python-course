Exercise: Lists

wincpy start 6eb355e1a60f48a28a0bbbd0c88d9ab4

Composer John Williams has written a great many pieces for a lot of different films. He's written so many, in fact, that he has asked you to write a number of functions to help him keep it all organized.

Write a function alphabetical_order that takes one argument: a list of strings that represent film names. It returns a list of the same films in alphabetical order. We have not discussed sorting lists yet, so you should probably search the web to see if there's a good approach out there. Your solution should not be longer than a few lines.
Write a function won_golden_globe that takes a film name and returns True or False based on whether or not this movie won a Golden Globe.
This page will come in handy: Wikipedia -- List of awards and nominations received by John Williams
A nomination is not a win.
You are not allowed to do string-to-string comparisons in this function, so no string_a == string_b!
John is not very tidy with his archive, so the captitalization of the names might not be correct. Look into using the lower-function on the given film string.
John's son Joseph accidentally mixed in some of his own work as lead singer for Toto with a list of his dad's compositions. Write a function remove_toto_albums that takes a list of strings, removes Joseph's Toto albums from it and returns the tidy list.
Use this information: Wikipedia -- Joseph Williams (musician)
It is not certain that all of Joseph's Toto albums are in the list received by remove_toto_albums, but they might! Don't let your script run into any errors.
Joseph did not inherit his dad's sloppiness with capitalization, so his Toto albums would be listed correctly.
Search the web on how to remove an item from a list by value.
Note

You may assume all input to your function is of the correct type.

Wincpy Check

Use wincpy check lists to see if you met all of the requirements for this exercise. Did you pass the test?