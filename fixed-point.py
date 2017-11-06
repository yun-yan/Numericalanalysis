i=1
TOL=0.00001
p0=1.5
N=30
def f(x):
    return x**3+4*x**2-10
def g1(x):
    return x-(x**3+4*x**2-10)
def g2(x):
    return (10/x-4*x)**0.5
def g3(x):
    return (1/2)*(10-x**3)**0.5
def g4(x):
    return (10/(4+x))**0.5
def g5(x):
    return x-(x**3+4*x**2-10)/(3*x**2+8*x)
while i< N:
    p=g5(p0)
    if abs(p-p0)<TOL:
        #print(p)
        break
    i+=1
    p0=p
print(p)