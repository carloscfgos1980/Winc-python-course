Modules

Module (noun): one of a set of separate parts that, when combined, form a complete whole.
Cambridge Dictionary entry for 'module'

https://dictionary.cambridge.org/dictionary/english/module

A lot of programming challenges are common to many programs, for example:

Fetching something from a web server;
Searching for a piece of text in a string;
Reading a file from the local file system.
In theory these problems really only need to be solved once and then everyone could just use that solution, regardless of whether they are building a pizza ordering app, messaging service or camera app. This idea is called modularization.

Python does this in the form of modules. The default data types and functions you have available to you when you start Python are already pretty powerful, but you can pull in an extra module if you need extra stuff.

Say you want to use the local time on the machine that your Python script is running on, when it's running. You can use the time-module for that.

import time

time.asctime()
As you saw in this example, you can import modules with the import statement. Module imports are usually done at the top of a file to ensure their availability throughout the code in that file, and so that we can quickly see what is (and isn't) being imported.

Read this to learn more about importing modules up to (so excluding) the part titled: 'The dir() Function':

Real Python -- Python Modules and Packages

https://realpython.com/python-modules-packages/
