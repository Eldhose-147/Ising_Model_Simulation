import numpy as np
import matplotlib.pyplot as plt
iterations=int(10E5)
x=np.random.default_rng().uniform(-1, 1, iterations+1)
y=np.random.default_rng().uniform(-1, 1, iterations+1)
count=0
pivalue=[]
x_value=np.arange(1,iterations+1,1)


for i in range(1,iterations+1):
    
    x1=x[i]
    y1=y[i]
    if (x1**2+y1**2<=1):
        count+=1
    else:
        count+=0
    x2=4*(count/i)
    pivalue.append(x2)


plt.plot(x_value,pivalue)
plt.ylim(3.1,3.2)
plt.show()