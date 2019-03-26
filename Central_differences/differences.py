from math import *
f = lambda x: (-0.1*(x)**4)-(0.15*(x)**3)-(0.5*(x)**2)-(0.25*(x))+1.2

x = 0.5
h = 0.25
forward = (f(x+h)-f(x))/h
backward = (f(x)-f(x-h))/h
centre = (f(x+h) - f(x-h))/(2*h)
print(forward, " ", backward, " ", centre)
