x0=1.0
x1=1.3
x2=1.6
x3=1.9
x4=2.2
f0=0.7651977
f1=0.6200860
f2=0.4554022
f3=0.2818186
f4=0.1103623
x=[x0,x1,x2,x3,x4]
f=[[f0,0,0,0,0],[f1,0,0,0,0],[f2,0,0,0,0],[f3,0,0,0,0],[f4,0,0,0,0]]
for i in range(len(x)):
    for j in range(1,i+1):
        f[i][j]=(f[i][j-1]-f[i-1][j-1])/(x[i]-x[i-j])
for i in range(5):
    print(f[i][i])