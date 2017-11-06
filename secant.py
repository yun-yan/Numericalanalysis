from sympy import cos,pi
i=1
TOL=0.00000001
p0=0.5
p1=pi.evalf()/4
def f(x):
    return cos(x)-x
N=10
while i<N:
    print(p0)
    p2=p1-f(p1)*(p1-p0)/(f(p1)-f(p0))
    if abs(p2-p1)<TOL:
        break
    i+=1
    p0=p1
    p1=p2


print(p2)