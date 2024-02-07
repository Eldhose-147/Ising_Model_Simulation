import numpy as np

def randomIsing(L):
    ising=np.zeros((L,L),dtype=float)
    for i in range(L):
        for j in range(L):
            p=np.random.uniform(0,1)
            if (p<0.5):
                ising[i][j]=-1
            else:
                ising[i][j]=1
    return (ising)

