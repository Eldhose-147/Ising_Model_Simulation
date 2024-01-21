import numpy as np
import matplotlib.pyplot as plt
N=10000
hbar = 1.0545718e-34  # Planck's constant / 2*pi
k_B = 1.380649e-23   # Boltzmann constant
m = 1e-26            # mass of oscillator
omega = 1e9          # frequency of oscillator
def energy(n):
        y= ((n+(1/2))*hbar*omega)
        return(y)
tot=[]
for j in range(1,300):
    T=j
    n1=0
    t=0
    E=np.zeros(N)
    for i in range (N):
        n=np.random.randint(0,100)
        if energy(n)<=energy(n1):
            E[i]=energy(n)
            
            
            n1=n
        else:
            k=np.random.uniform(0,1)
            R= np.exp( -(n - n1) / k_B*T )
            if R>=k:
                E[i]=energy(n)
                n1=n
                
                
            else:
                
                #E[i]=energy(n)
                n1=n1

    total=np.mean(E)
    tot.append(total)

temp=np.arange(1,300,1)
plt.plot(temp,tot)
plt.show()





   
   