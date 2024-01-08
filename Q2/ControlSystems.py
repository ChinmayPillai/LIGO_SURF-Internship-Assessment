import control as ct
import matplotlib.pyplot as plt

a = -1 / (8935 * 100)
sys = ct.ss(a, -a, 1, 0)

time = [i*1000 for i in range(10000)]

t, x = ct.input_output_response(sys, time, U = 300.0, X0 = 400.0)

plt.plot(t, x)
plt.title("T_cop vs Time")
plt.ylabel('T_cop (Kelvin)')
plt.xlabel('Time (10^7 sec)')

plt.show()