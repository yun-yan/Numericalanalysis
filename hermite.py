x0=1.3
x1=1.6
x2=1.9
f0=0.6200860
f1=0.4554022
f2=0.2818186
df0=-0.5220232
df1=-0.5698959
df2=-0.5811571
x=[x0,x1,x2]
f=[f0,f1,f2]
df=[df0,df1,df2]
z=[0,0,0,0,0,0]
Q=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
for i in range(len(x)):
    z[2*i]=x[i]
    z[2*i+1]=x[i]
    Q[2*i][0]=f[i]
    Q[2*i+1][0]=f[i]
    Q[2*i+1][1]=df[i]
    if i!=0:
        Q[2*i][1]=(Q[2*i][0]-Q[2*i-1][0])/(z[2*i]-z[2*i-1])
for i in range(2,2*len(x)-1):
    for j in range(2,i+1):
        Q[i][j]=(Q[i][j-1]-Q[i-1][j-1])/(z[i]-z[i-j])
for i in range(2*len(x)-1):
    print(Q[i][i])
print(Q)
value=1.5
a=1
h=Q[0][0]
#print(Q[0][0]+Q[1][1]*(value-x[0])+Q[2][2]*(value-x[0])**2+Q[3][3]*(value-x[0])**2*(value-x[1])+Q[4][4]*(value-x[0])**2*(value-x[1])**2+Q[5][5]*(value-x[0])**2*(value-x[1])**2*(value-x[2]))
'''the below is equal to the last line printQ[0][0]...'''
for i in range(1,2*len(x)):
    a=a*(value-z[i-1])
    h=h+a*Q[i][i]
print(h)