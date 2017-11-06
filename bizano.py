a=1
b=2
POL=0.00001
NO=100000
i=0
def f(x):
	return x**3+4*x**2-10
while b-a>POL and i<NO:
	if f(a)*f((a+b)/2)>0:
		a=(a+b)/2
	else:
		b=(a+b)/2
	i+=1
print(a)

