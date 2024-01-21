
import numpy as np
import matplotlib.pyplot as plt
t=10000
h=1.05457*pow(10,-34)
Kb=1.380649*pow(10,-23)
w=pow(10,9)
# h=1
# Kb=1
# w=1
P=[]
for j in range(1,500):
    T=j

    def energy(n):
        y= ((n+(1/2))*h*w)
        return(y)

    def prob(n):
        y=np.exp(-energy(n)/(Kb*T))
        return(y)


    n1=0
    total=[]
    
    for i in range (t):
        n=np.random.randint(0,100)
        if energy(n)<=energy(n1):
            total.append(energy(n))
          
            n1=n
        else:
            k=np.random.uniform(0,1)
            R=prob(n)/prob(n1)
            if R>=k:
                total.append(energy(n))
                
                n1=n
            else:
                #total.append(energy(n1))
                
                n1=n1


    # E=total[3000:-1]
    avgenergy=np.mean(total)
    P.append(avgenergy) 

temp=np.arange(1,499,1)
# plt.plot(temp,P)
# plt.show()
f=np.copy(P[1:len(P)])
r=np.copy(P[0:len(P)-1])

d=r-f
plt.plot(temp,d)
plt.show()
    

