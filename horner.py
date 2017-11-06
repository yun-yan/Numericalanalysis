def P(x):
    return 2*x**4-3*x**2+3*x-4
a4=2
a3=0
a2=-3
a1=3
a0=-4
x0=-2
y=a4
z=a4
y=x0*y+a3
z=x0*z+y
y=x0*y+a2
z=x0*z+y
y=x0*y+a1
z=x0*z+y
y=x0*y+a0
print(y,z)