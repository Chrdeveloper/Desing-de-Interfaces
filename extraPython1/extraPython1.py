import numpy

def max(a, b):
    if (b > a):
        return b
    else:
        return a

def max_de_tres(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if (b > c):
            return b
        else:
            return c



