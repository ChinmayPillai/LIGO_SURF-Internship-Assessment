import control as ct
import numpy as np
import matplotlib.pyplot as plt


a = -1 / (8935 * 100)
sys = ct.ss(a, -a, 1, 0)

time = [i*1000 for i in range(10000)]
input = np.random.normal(loc = 300.0, scale = 10.0, size = 10000)

t, x = ct.input_output_response(sys, time, U = input , X0 = 300.0)

fig, axs = plt.subplots(2)

axs[0].plot(t, x)
axs[0].set_title("T_cop vs Time")
axs[0].set_xlabel("Time (10^7 sec)")
axs[0].set_ylabel("T_cop (Kelvin)")

axs[1].plot(t, input)
axs[1].set_title("T_env vs Time")
axs[1].set_xlabel("Time (10^7 sec)")
axs[1].set_ylabel("T_env (Kelvin)")

plt.show()