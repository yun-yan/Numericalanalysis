from numpy import e
x0=0
x1=1
x2=2
x3=3
a0=1
a1=e**1
a2=e**2
a3=e**3
x=[x0,x1,x2,x3]
a=[a0,a1,a2,a3]
n=len(x)-1
h=[x[i+1]-x[i] for i in range(n)]
apha=[3/h[i]*(a[i+1]-a[i])-3/h[i-1]*(a[i]-a[i-1]) for i in range(1,n)]
apha.insert(0,0)
apha.append(0)
l=[0,0,0,0]
mu=[0,0,0,0]
z=[0,0,0,0]
for i in range(1,n):
	l[i]=2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
	mu[i]=h[i]/l[i]
	z[i]=(apha[i]-h[i-1]*z[i-1])/l[i]
b=[0,0,0,0]
c=[0,0,0,0]
d=[0,0,0,0]
for j in range(n-1,-1,-1):
    c[j]=z[j]-mu[j]*c[j+1]
    b[j]=(a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
    d[j]=(c[j+1]-c[j])/(3*h[j])
print('',a,'\n',b,'\n',c,'\n',d)




