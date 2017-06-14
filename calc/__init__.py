from math import *
del pi
from calc.constants import *
from functools import reduce

# Functions missing from math.
# Negative One To The n, where n is an integer.
def nott(n):
    return 1 - 2*(n & 1)
# Divide a by b, ignoring any divides by zero.
def div_ignore(a, b):
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        return a/b
# Factor n.
def factor(n):
    l = []
    while n != 1:
        for i in range(2, n+1):
            if n%i == 0:
                n //= i
                l.append(i)
                break
    return l

# Evaluate, and print. I just can't think of a way to do this without an 
# eval(). Besides just feeling dirty, it also means syntax errors that can 
# only be caught at runtime, so keep the expression in the input string as 
# simple as possible and watch out for side effects. Example:
# x = big_calculation()
# eprint('x')
def eprint(s):
    # dirtiness
    import inspect
    stack = inspect.stack()
    g = stack[1][0].f_globals
    l = stack[1][0].f_locals
    res = str(eval(s, g, l))
    # dirtiness is done, string representation of s is in res.

    # If there are newlines in the string representation of s, it's probably a 
    # good idea to separate the 's = ' from the rest, since the code that 
    # generated the string representation is expecting indentation to be 
    # constant for all lines.
    if '\n' in res:
        res = '\n' + res

    print('{} = {}'.format(s, res))

def time2str(t):
    years = int(t//year)
    t %= year
    days = int(t//day)
    t %= day
    hours = int(t//hour)
    t %= hour
    minutes = int(t//minute)
    t %= minute
    seconds = t%minute
    l = []
    if years != 0:
        l.append(str(years) + ' years')
    if days != 0:
        l.append(str(days) + ' days')
    if hours != 0:
        l.append(str(hours) + ' hours')
    if minutes != 0:
        l.append(str(minutes) + ' minutes')

    l.append(str(floor(seconds)) + ' seconds')

    if l == []:
        return '0 seconds'
    s = ''
    while True:
        s += l.pop(0)
        if l == []:
            return s
        s += ', '
# Print a time.
def tprint(t):
    print(time2str(t))

def readiter():
    while True:
        s = input()
        if s == '':
            return
        yield s

def read(f):
    for s in readiter():
        f(s)

def repl(f):
    for s in readiter():
        print(f(s))

# For entering a lot of data at once at a keyboard.
def readlist():
    return list(readiter())
# Parsing shortcuts.
def parseints():
    return [int(n) for n in readlist()]
def parsefloats():
    return [float(x) for x in readlist()]

# Returns a new sequence with i missing. Mysteriously missing from the 
# standard library.
def seq_del(s, i):
    return s[:i] + s[i+1:]

# These were mysteriously missing from the standard library.
def foldl(f, x, l):
    z = x
    for n in range(len(l)):
        z = f(z, l[n])
    return z
def foldr(f, l, x):
    z = x
    for n in range(len(l) - 1, -1, -1):
        z = f(l[n], z)
    return z
# Apply binary operator f, right associative, i.e. f(a0, f(a1, a2)).
def reduce_r(f, args):
    assert len(args) >= 2
    return foldr(f, args[:-1], args[-1])

# Function composition. Also, effectively a matrix multiply for linear 
# operators in a function representation.
def comp2(a, b):
    return lambda v: a(b(v))
def comp(*args):
    return reduce_r(comp2, args)

# Programs that do a lot of imports before starting can execute this function 
# after the imports are done.
def loaded():
    print('Program is loaded.')
