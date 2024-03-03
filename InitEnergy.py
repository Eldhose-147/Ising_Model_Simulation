def Ener(ising,L,J):
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
    return (M,E)