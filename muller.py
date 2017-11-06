p0=0.5
p1=1
p2=1.5
TOL=0.001
N=10
h1=p1-p0
h2=p2-p1
def f(x):
    return x**4-3*x**3+x**2+x+1
delta1 = (f(p1)-f(p0))/h1
delta2 = (f(p2)-f(p1))/h2
d = (delta2-delta1)/(h1+h2)
i=3
while i<N:
    b=delta2+h2*d
    D=(b**2-4*f(p2)*d)**0.5
    if abs(b-D)<abs(b+D):
        E=b+D
    else:
        E=b-D
    h=-2*f(p2)/E
    p=p2+h
    if abs(h)<TOL:
        print(p)
        break
    p0=p1
    p1=p2
    p2=p
    h1=p1-p0
    h2=p2-p1
    delta1 = (f(p1) - f(p0)) / h1
    delta2 = (f(p2) - f(p1)) / h2
    d = (delta2 - delta1) / (h1 + h2)
    i += 1
print("Method failed after N iteration,N=",N)

