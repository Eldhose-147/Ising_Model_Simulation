# Python code to festimate the value of Pi using Monte carlo algorithm

import numpy as np
import matplotlib.pyplot as plt
iterations=int(10E5)
# generating random values of between -1 and 1
x=np.random.default_rng().uniform(-1, 1, iterations)
y=np.random.default_rng().uniform(-1, 1, iterations)
count=0
pi_value=[]
x_value=np.arange(0,iterations,1)

for i in range(iterations):  
    x1=x[i]
    y1=y[i]
    if (x1**2+y1**2<=1):
        count+=1
    else:
        count+=0
    x2=4*(count/(i+1))
    pi_value.append(x2)

# graph plotting between generated pi value and iteration number
plt.plot(x_value,pi_value,color='g',)
plt.ylabel('Pi value')
plt.xlabel('Number of interations')
plt.ylim(3.1,3.2)
plt.show()
print(pi_value[-1])