import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

X = [0]
t = [0]

t_end = 1000        #simulation end time

k = 2
gamma = 0.1         #gives steady state concentration of 20 since it's equal to k/gamma

while t[-1] < t_end:

    current_X = X[-1]

    rates = [k, gamma * current_X]
    rate_sum = sum(rates)

    tau = np.random.exponential(scale=1/rate_sum)     # scale = 1/lambda, which is equal to the mean of the exponential distribution

    t.append(t[-1] + tau)

    rand = random.uniform(0,1)
    
    # production event
    if rand * rate_sum > 0 and rand * rate_sum <= rates[0]:
        X.append(X[-1] + 1)

    # degradation event
    elif rand * rate_sum > rates[0] and rand * rate_sum <= rates[0] + rates[1]:
        X.append(X[-1] - 1)

plt.plot(t, X)
plt.xlabel('time')
plt.ylabel('mRNA concentration')
plt.show()


