from math import sin, pi
f = lambda x: x*sin(x)
a = 0
b = pi/2
n = 10
h = (b - a) / n
S = (f(a) + f(b))
for i in range(1, n):
    S += 2 * f(a+i*h)
Integral = (h/2) * S
print(Integral)