import numpy as np
def MCS(ising,L,T,J,E,M):
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
        
    return(ising,E,M)