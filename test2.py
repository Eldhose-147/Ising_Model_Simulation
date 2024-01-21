import numpy as np
import matplotlib.pyplot as plt
t=100000
hbar = 1.0545718e-34  # Planck's constant / 2*pi
k_B = 1.380649e-23   # Boltzmann constant
m = 1e-26            # mass of oscillator
omega = 1e9          # frequency of oscillator
def energy(n):
    y= ((n+(1/2))*hbar*omega)
    return(y)

def prob(n):
    y=np.exp(-energy(n)/(k_B*300))
    return(y)


n1=0
total=[]
ener=0
for i in range (1,t):
    n=np.random.randint(0,1000)
    if energy(n)<=energy(n1):
        ener+=energy(n)/i
        total.append(energy(n))
        
        n1=n
    else:
        k=np.random.uniform(0,1)
        R=prob(n)/prob(n1)
        if R>=k:
            ener+=energy(n)/i
            total.append(energy(n))
            
            n1=n
        else:
            ener+=energy(n1)/i
            total.append(energy(n1))
            
            n1=n1

num=np.arange(1,t,1)
plt.plot(num,total)
plt.show()
