from sympy import cos,pi,diff,Symbol
i=1
TOL=0.00000001
p0=pi.evalf()/4
def f(x):
    return cos(x)-x
x=Symbol('x')
df=diff(f(x),x)
N=10
while i<N:
    print(p0)
    p = p0 - f(p0) / (df.subs(dict({x:p0})))
    if abs(p-p0)<TOL:
        #print(p)
        break
    i+=1
    p0=p



print(p)