import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import random

G1 = [0]
G2 = [0]
G3 = [0]
t = [0]

t_end = 1000

k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.1
k_3 = 0.5
gamma_3 = 0.1
K_d = 1                              # K_d and same for everything for simplicity
n = 3

while t[-1] < t_end:
    
    current_G1 = G1[-1]
    current_G2 = G2[-1]
    current_G3 = G3[-1]

    rates = [k_1 * (K_d**n/(K_d**n + current_G3**n)), gamma_1 * current_G1, \
        k_2 * (current_G1**n/(K_d**n + current_G1**n)), gamma_2 * current_G2, \
        k_3 * (current_G2**n/(K_d**n + current_G2**n)), gamma_3 * current_G3]

    rate_sum = sum(rates)

    tau = np.random.exponential(scale=1/rate_sum)

    t.append(t[-1] + tau)

    rand = random.uniform(0,1) 

    if rand * rate_sum <= rates[0]:
        G1.append(G1[-1] + 1)
        G2.append(G2[-1])
        G3.append(G3[-1])               # value of G1 increases, values of G2 and G3 stay the same
    
    elif rand * rate_sum > rates[0] and rand * rate_sum <= sum(rates[:2]):
        G1.append(G1[-1] - 1)
        G2.append(G2[-1])
        G3.append(G3[-1])

    elif rand * rate_sum > sum(rates[:2]) and rand * rate_sum <= sum(rates[:3]):
        G1.append(G1[-1])
        G2.append(G2[-1] + 1)
        G3.append(G3[-1])

    elif rand * rate_sum > sum(rates[:2]) and rand * rate_sum <= sum(rates[:3]):
        G1.append(G1[-1])
        G2.append(G2[-1] + 1)
        G3.append(G3[-1])

    elif rand * rate_sum > sum(rates[:3]) and rand * rate_sum <= sum(rates[:4]):
        G1.append(G1[-1])
        G2.append(G2[-1] - 1)
        G3.append(G3[-1])

    elif rand * rate_sum > sum(rates[:4]) and rand * rate_sum <= sum(rates[:5]):
        G1.append(G1[-1])
        G2.append(G2[-1])
        G3.append(G3[-1] + 1)

    elif rand * rate_sum > sum(rates[:5]) and rand * rate_sum <= sum(rates[:6]):
        G1.append(G1[-1])
        G2.append(G2[-1])
        G3.append(G3[-1] - 1)

f, (ax1,ax2,ax3) = plt.subplots(3, sharex = True, sharey = False)                      # plotting function

line1, = ax1.plot(t, G1, color = 'b', label = 'G1')
line2, = ax2.plot(t, G2, color = 'r', label = 'G2')
line3, = ax3.plot(t, G3, color = 'g', label = 'G3')

ax2.set_ylabel("Concentration")
ax3.set_xlabel("Time")

ax1.legend(handles=[line1,line2,line3])

plt.show()
