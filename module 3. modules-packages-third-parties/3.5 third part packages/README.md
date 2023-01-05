Third Party Packages

In the land of Python it is very easy to use code that wasn't written by the Python developers or yourself, but by a third party. You just need to download such a module, import it into your own code and you're off to the races. Because there are so many Python programmers sharing their code, there's usually at least three popular third party packages solving a problem you're facing.

Danger

BEWARE: when you run third party code, that code is giving the same power over your machine as your own code. It can create or delete your files or send them over the internet to someone else. You have to somehow make sure you trust that code before you run it. And then you have to make sure you trust each updated version of that package, too. Since third party packages often include thousands of lines of code, this is not easy to do in practice.

Instead of manually downloading packages containing Python modules, we have pip, which stands for package installer for Python. pip comes with the official Python installation since 3.4, so you should already have it on your machine. In fact: you used it when you installed Wincpy.

pip -- The Python Package Installer
https://pip.pypa.io/en/stable/

pip is a program to install packages, and unless otherwise instructed it collects the packages to install from a package repository called PyPi, the Python Package Index.

PyPi -- The Python Package Index
https://pypi.org

To install a third party package you simply enter the command:

pip install example

Danger

Did you copy and paste this pip install command? Then you already have some third party code on your machine that you probably did not check for security issues. The example word is really an example word here, so we do not suggest really installing a package by that name.

Then read the package's own documentation (which you can usually find on its website) to find out how to use it in code. It probably starts with importing a package by the same name.

import example

example.do_a_thing()
To find packages that are useful to you, one of the best ways is to search GitHub. Popular packages -- with many stars on their project page -- are usually popular for a reason, and these popular packages are also the ones that are often documented well enough for you to use them.