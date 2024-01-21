import numpy as np
import matplotlib.pyplot as plt
L=50
T=1
ising=np.zeros((L,L),dtype=float)

for i in range(L):
    for j in range(L):
        p=np.random.uniform(0,1)
        if (p<0.5):
            ising[i][j]=-1
        else:
            ising[i][j]=1

J=1
E=0
M=0
for i in range (L):
    for j in range (L):
        a,b,c,d=i+1,i-1,j+1,j-1
        if i==L-1:
            a=0
        if i==0:
            b=L-1
        if j==L-1:
            c=0
        if j==0:
            d=L-1
    
        M+=ising[i][j]
        E=E-J*float(ising[i][j]*(ising[a][j]+ising[b][j]+ising[i][c]+ising[i][d]))
print(M,E)

E*=0.5

N=10000
ener=[]
mag=[]
for n in range(N):
   

    for k in range(L):
        for l in range (L):
            
            r=np.random.uniform(0,1)
            i=int(r*(L-1))
            t=np.random.uniform(0,1)
            j=int(t*(L-1))
            a,b,c,d=i+1,i-1,j+1,j-1
            if i==L-1:
                a=0
            if i==0:
                b=L-1
            if j==L-1:
                c=0
            if j==0:
                d=L-1
            Ei=-J*float(ising[i][j]*(ising[a][j]+ising[b][j]+ising[i][c]+ising[i][d]))
            ising[i][j]=-ising[i][j]
            Ef=-J*float(ising[i][j]*(ising[a][j]+ising[b][j]+ising[i][c]+ising[i][d]))
            dE=Ef-Ei
            
            if(dE<=0.0):
                E+=dE
                M+=(2.0*float(ising[i][j]))
            else:
                u=np.exp(-dE/T)
                h=np.random.uniform(0,1)
                if(h<u):
                    E+=dE
                    M+=(2.0*float(ising[i][j]))

                else:
                    ising[i][j]=-ising[i][j]
        
    enspin=E/(L*L)
    Mspin=M/(L*L)
   
    ener.append(enspin)
    mag.append(Mspin)
num=np.arange(0,n+1,1)
plt.plot(num,mag,linewidth=1)
# plt.plot(num,ener,linewidth=1)
plt.show()




