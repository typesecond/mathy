import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation
def dy_dt(y, t):
    """
    Compute dy/dt = -2y + sin(t)
    """
    return -2 * y + np.sin(t)

# Initial condition
y0 = 1

# Time points where we want the solution
t = np.linspace(0, 10, 100)  # From t=0 to t=10, with 100 points

# Solve the ODE
solution = odeint(dy_dt, y0, t)

# Plot the solution
plt.figure(figsize=(8, 5))
plt.plot(t, solution, label="y(t)", color="blue")
plt.title("Solution of dy/dt = -2y + sin(t)")
plt.xlabel("Time t")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()






