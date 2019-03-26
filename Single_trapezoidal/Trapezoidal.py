import sympy as sp
from scipy.integrate import quad

def f(x):
    return 0.2 + (25*(x)) - (200*(x)**2) + (675*(x)**3) - (900*(x)**4) + (400*(x)**5)

x = sp.Symbol('x')

a = 0
b = 0.8
integral = (b-a)*((f(a)+f(b))/2)
i = quad(f, 0, 0.8)
print("Symbolic Representation: ",sp.integrate(f(x)))
print("Actual value is: ", i[0])
print("Estimated Value is: ", integral)

err = (i[0] - integral)/i[0] * 100
print("Percent error is: ", err, "%")

