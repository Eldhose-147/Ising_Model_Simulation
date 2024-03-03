import numpy as np
import matplotlib.pyplot as plt
from RandomSpin import randomIsing
from InitEnergy import Ener
from Montecarlo import MCS
T=1.4
J=1
Len=[]
for L in range(10,40,10):
    ising=randomIsing(L)         
    M,E=Ener(ising,L,J)
    print(M,E)
    E*=0.5
    N=100000
    # ener=[]
    mag=[]
    for n in range(N):
        ising,E,M=MCS(ising,L,T,J,E,M)
        # enspin=E/(L*L)
        Mspin=M/(L*L)
    
        # ener.append(enspin)
        mag.append(Mspin)

    Len.append(mag)

num=np.arange(0,n+1,1)
plt.plot(num,Len[0],color='r',label='L=10')
plt.plot(num,Len[1],color='g',label='L=20')
plt.plot(num,Len[2],color='b',label='L=30')
plt.title('M/N vs MCS')
plt.xlabel('MCS')
plt.ylabel('M/N')
plt.legend()
plt.show()