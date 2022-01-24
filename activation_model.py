import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [0,0]                                # 0 mRNA and 0 protein

t = np.linspace(0, 200, num=100)          # creates an array of 100 evenly spaced values over the range from 0 to 200

k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.05
K_d = 5
n = 5

params = [k_1, gamma_1, k_2, gamma_2, n, K_d]

def sim(variables, t, params):              # ODE function with parameters (y, t, ...) as required by odeint()

    G1 = variables[0]
    G2 = variables[1]

    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    K_d = params[5]

    dG1dt = k_1 - gamma_1 * G1
    dG2dt = k_2 * (G1**n/(K_d**n + G1**n)) - gamma_2 * G2
    
    return([dG1dt,dG2dt])

y = odeint(sim, y0, t, args=(params,))      # ODE solver

f,ax = plt.subplots(1)                      # plotting function

line1, = ax.plot(t,y[:,0], color = 'b', label = 'G1')
line2, = ax.plot(t,y[:,1], color = 'r', label = 'G2')

ax.set_ylabel("Concentration")
ax.set_xlabel("Time")

ax.legend(handles=[line1,line2])

plt.show()