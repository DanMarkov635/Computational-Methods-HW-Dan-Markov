import numpy as np
import matplotlib.pyplot as plt


# Define the Integrand Function:
def fun(t):
  f = np.exp(-t**2)
  return f

# Define the Function witht the Integral
def E(x,h = 0.01):

  # x = 0 should give E = 0
  if x == 0:
    return 0

  # Define number of steps and divide by 2 to use for Simpson's Rule
  steps = int(x/h)
  if steps % 2 != 0:
    steps += 1
  loop = int(steps/2)

  # Previous Step changes where the final x value is, so we adjust h to compensate                    
  h = x / steps


  # Here we follow Simpson's Rule:
  s = (fun(0) + fun(x))

  for i in range(1,loop):
    s += 4*fun((2*i-1) * h)
    s += 2*fun(2*i*h)

  s += 4*fun((2*loop-1) * h)

  s *= h/3

  return s

# Plotting:
x_vals = np.linspace(0,10,1000)
y_vals = np.array([E(x) for x in x_vals])

plt.scatter(x_vals,y_vals)
plt.show()
