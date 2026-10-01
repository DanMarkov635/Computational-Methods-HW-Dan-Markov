import numpy as np
from astropy import constants as const

R = 3.844e8          # Distance from Earth to Moon
w = 2.662e-6         # Angular Velocity
M_moon = 7.348e22    # Mass of Moon
Guess = 3.0e8       # Initial Guess for Newton's method
epsilon = 1e-10        # Determines Error

# Defining the Function:
def F(r):
  fun = (const.G.value * const.M_earth.value / r**2) - (const.G.value * M_moon / (R - r)**2) - (w**2) * r
  return fun

# Defining the Derivative Function:
def F_prime(r):
  deriv = -2 * (const.G.value * const.M_earth.value / r**3) - 2 * (const.G.value * M_moon / (R - r)**3) - w**2
  return deriv

# Newton's Method: 
x = Guess

while abs(F(x))>epsilon:
  x = x - F(x) / F_prime(x)

print("The Lagrange point is at", int(x), "meters away from the Earth")

