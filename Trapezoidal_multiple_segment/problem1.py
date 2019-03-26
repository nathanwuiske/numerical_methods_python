f = lambda x: 0.2 + (25*(x)) - (200*(x)**2) + (675*(x)**3) - (900*(x)**4) + (400*(x)**5)
a = 0
b = 0.8
n = 10
h = (b-a) / n
S = (f(a) + f(b))

for i in range(1, n):
    S += 2*f(a+i*h)

Integral = (h / 2) * S
print(Integral)

def multiTrap(n, a ,b):
    h = (b-a)/n
    x = a
    sum = f(x)
    for i in range(1, n):
        x = x + h
        sum = sum + 2 * f(x)
    sum = sum + f(b)
    return (b-a) * sum / (2 * n)

print(multiTrap(10, 0 ,0.8))
