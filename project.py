import numpy as np
import matplotlib.pyplot as plt
n=10000


ER=[]
for j in range(1,10):
    num1=7
    n0=0
    P=np.zeros(n,)

    def f(nu):
        y=np.exp(((-4.320185*pow(10,-8))*(nu+(1/2)))/j)
        return y

    p0=f(num1)
    for i in range(n):
        num=np.random.randint(n)
        p1=f(num)
        if p1<=p0:
            p0=p1
            P[num]+=f(num)
            
            
        
        else:
            k=np.random.uniform(0,1)
            R=p1/p0
            if R>=k:
                p0=p1
                P[num]+=f(num)
                n0+=1
            else:
                p0=p0
                

        



    N=np.arange(0,1000000,1)  
    energy=np.array(((-4.320185*pow(10,-8))*(N+(1/2))/j))
    Ener=energy*P
    totener=np.sum(Ener)/np.sum(P)
    ER.append(totener)

temp=np.arange(1,10,1)
plt.plot(temp,ER)
plt.show()



    

