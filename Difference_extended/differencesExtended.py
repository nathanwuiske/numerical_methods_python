
f = lambda x: (-0.1*(x)**4)-(0.15*(x)**3)-(0.5*(x)**2)-(0.25*(x))+1.2

x = 0.5
h1 = 0.5
h2 = 0.25
centreh1 = (f(x+h1) - f(x-h1))/(2*h1)
centreh2 = (f(x+h2) - f(x-h2))/(2*h2)
richardson = centreh2 + (1/3*(centreh2 - centreh1))

print(centreh1, " ", centreh2, " ", richardson)



