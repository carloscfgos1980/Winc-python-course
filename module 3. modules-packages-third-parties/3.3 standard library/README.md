## Standard Library

The Python interpreter you installed has a lot of functionality built into it. You can use various types like int, float and str without importing anything extra, just like you can use things like print and len.

Additionally there are a good number of modules that are included in the Standard Library that are installed. You only need to import these modules before using them. Examples are the math module for -- you guessed it -- doing math and random for pseudo-random number generation (which is surprisingly hard to do yourself).

Here's a link to a (very dry) list of everything that is in the standard library, and a fun Module of the Week website that you may be interested in:

The Python Standard Library
https://docs.python.org/3/library/

Python 3 Module of the Week
https://pymotw.com/3/

# Pros and Cons

Scrolling down the list of things in the standard library you might think that everything is in there. That's not entirely true, and even if some functionality is covered, there might be a better package out there for it. A classic example is the urllib.request module, which in practice is often replaced by the popular third-party module requests:

urllib.request
https://docs.python.org/3/library/urllib.request.html

requests
https://requests.readthedocs.io/en/latest/

Because Python is distributed to millions of people around the world, the developers of the Python language are very deliberate about updates to the language. They tend to limit included functionality to a set of features everyone needs. On one hand this means you won't encounter a lot of fancy stuff in the standard library. Kenneth Reitz, long-time Python contributor and developer of popular modules like Requests, said in a talk (only half joking):

"The standard library is where modules go to die".
On the other hand this makes Python very stable and reliable. Judging when to use which module is something you get better at over time.