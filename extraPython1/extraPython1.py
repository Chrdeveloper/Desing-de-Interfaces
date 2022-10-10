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

def longCad(n):
    aux = n[0]
    cont = 0
    while(aux != None):
        cont = cont + 1
        aux = n[cont]
    return cont





