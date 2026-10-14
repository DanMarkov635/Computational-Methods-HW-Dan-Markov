import matplotlib.pyplot as plt
from astropy.io import fits
from numpy import zeros
from cmath import exp,pi 

# General name
filename = "tic0000627436.fits"

# Specific name for my computer
# filename = r"C:\Users\DanMa\Downloads\tic0000627436.fits"

# Time Range
t_start = 1439
t_end = 1449

# Extracting Data from the File
hdul = fits.open(filename)
times = hdul[1].data['times']
fluxes = hdul[1].data['fluxes']
ferrs = hdul[1].data['ferrs']

# Cutting the Arrays Down to the Desired Size
truth_array = (times >= t_start) & (times <= t_end)
new_times = times[truth_array]
new_fluxes = fluxes[truth_array]

# Finding the Fourier Coefficients
N = len(new_times)
c = zeros(N, dtype = complex)
for k in range(N):
  for n in range(N):
    c[k] += new_fluxes[n]*exp(-2j*pi*k*n/N) 

power = abs(c)

# Plotting
plt.plot(range(1, N), power[1:N])
plt.xlabel("k")
plt.ylabel("Power")
plt.title("Fourier Power Spectrum")
plt.show()
