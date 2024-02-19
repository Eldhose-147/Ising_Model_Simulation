import numpy as np
import matplotlib.pyplot as plt
from RandomSpin import randomIsing
from InitEnergy import Ener
from Montecarlo import MCS
L=20
T=2.1
ising=randomIsing(L)         
J=1
M,E=Ener(ising,L,J)
print(M,E)
E*=0.5
N=100000
ener=[]
mag=[]
for n in range(N):
    ising,E,M=MCS(ising,L,T,J,E,M)
    enspin=E/(L*L)
    Mspin=M/(L*L)
   
    ener.append(enspin)
    mag.append(Mspin)
num=np.arange(0,n+1,1)
plt.plot(num,mag,linewidth=1)
plt.show()




