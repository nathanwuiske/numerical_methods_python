import math

def f(x):
    return x*math.sin(x)



def multiTrap(n, a, b):
    t = (b - a) / (2 * n)
    h = (b - a) / n
    s = (f(a) + f(b))
    for i in range(1, n):
        s += 2 * f(a+i*h)
    r = s * t
    return r

print(multiTrap(10, 0, math.pi/2))