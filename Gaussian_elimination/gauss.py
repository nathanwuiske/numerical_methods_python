from math import sqrt, exp, pi

def erf(a):
    return (2/sqrt(pi))*exp(-a**2)


def gauss2(a, b):

    n = 2
    xi = [-0.57735, 0.57735]
    ci = [1, 1]
    r = 0
    m = (b - a) / 2
    c = (b + a) / 2

    for i in range(1, n+1):
        r += ci[i - 1] * erf((m * xi[i - 1] + c))
    r = r * m
    return r

print(gauss2(0, 1.5))

