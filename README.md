# calc
###_for python_

Everything you've ever wanted in a scientific calculator, implemented with 
python. Supports SI prefixes, unit conversions, physical constants, output and 
formatting shortcuts like `hex()`, and addresses a few of the shortcomings of 
vanilla math from the python standard library. Comes with all of the fixin's 
of the python language, including ability to define variables, lists, and 
functions on the fly, as well as import numpy, pyplot, scipy, sympy, whatever. 
Imbued with awesomeness and miracles. Guaranteed to increase physicist 
happiness. Minimalist.

## installing
Installing is pretty standard python fare. Combine `./setup.py install 
--root=prefix` with the package manager of your choice. Some crazy person 
maintains an AUR package, so you Arch Linux users can do `pacaur -S 
python-calc`.

## using
Start the calculator with the calc command:
```
$ calc
>>>
```
Then do things.
```
>>> cos(tau)
1.0
>>> L = 300*milli*metre
>>> L/inch
11.811023622047244
>>> omega = sqrt(g/L)
>>> omega
5.717414917017422
>>>
```
Yeah, that's nice.

 vi:fo=atw
