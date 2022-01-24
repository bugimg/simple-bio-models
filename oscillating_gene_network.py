import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [0,0,0]                             

t = np.linspace(0, 200, num=100)         

k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.1
k_3 = 0.5
gamma_3 = 0.1
K_d = 1                                     # K_d and same for everything for simplicity
n = 3

params = [k_1, gamma_1, k_2, gamma_2, k_3, gamma_3, n, K_d]

def sim(variables, t, params):              # ODE function with parameters (y, t, ...) as required by odeint()

    G1 = variables[0]
    G2 = variables[1]
    G3 = variables[2]

    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    k_3 = params[4]
    gamma_3 = params[5]
    n = params[6]
    K_d = params[7]

    dG1dt = k_1 * (K_d**n/(K_d**n + G3**n)) - gamma_1 * G1
    dG2dt = k_2 * (G1**n/(K_d**n + G1**n)) - gamma_2 * G2
    dG3dt = k_3 * (G2**n/(K_d**n + G2**n)) - gamma_3 * G3
    
    return([dG1dt,dG2dt,dG3dt])

y = odeint(sim, y0, t, args=(params,))      # ODE solver

f, (ax1,ax2,ax3) = plt.subplots(3, sharex = True, sharey = False)                      # plotting function

line1, = ax1.plot(t,y[:,0], color = 'b', label = 'G1')
line2, = ax2.plot(t,y[:,1], color = 'r', label = 'G2')
line3, = ax3.plot(t,y[:,2], color = 'g', label = 'G3')

ax2.set_ylabel("Concentration")
ax3.set_xlabel("Time")

ax1.legend(handles=[line1,line2,line3])

plt.show()