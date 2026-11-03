import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

distance = 1000.0
cross_section = 6.652 * 10 ** (-25)
density = 10 ** 20
mfp = (1 /(cross_section * density)) / 100
x = 0.0
y = 0.0
time = 0.0
c = 3.0 * 10**8
x_vals = np.array(x)
y_vals = np.array(y)
t_vals = np.array(time)

rng = np.random.default_rng() 

free_path = -mfp * np.log(rng.random())
free_path = min(free_path, distance)

x += free_path
time += free_path / c

x_vals = np.append(x_vals,x)
y_vals = np.append(y_vals, y)
t_vals = np.append(t_vals,time)

while (x < distance) and (x >= 0.0):

  free_path = -mfp * np.log(rng.random())

  cos_theta = rng.uniform(-1.0,1.0)
  phi = rng.random() * 2 * np.pi

  x += free_path * cos_theta
  y += free_path * (1 - cos_theta**2)**0.5 * np.cos(phi)
  time += free_path / c

  x_vals = np.append(x_vals,x)
  y_vals = np.append(y_vals,y)
  t_vals = np.append(t_vals,time)

if (x_vals[-1] > 1000):
  extra_dist_x = x_vals[-1] - 1000.0
  extra_t = (extra_dist_x / (x_vals[-1] - x_vals[-2])) * (t_vals[-1] - t_vals[-2])
  extra_dist_y = (extra_dist_x / (x_vals[-1] - x_vals[-2])) * (y_vals[-1] - y_vals[-2])

  x_vals[-1] = x_vals[-1] - extra_dist_x
  t_vals[-1] = t_vals[-1] - extra_t
  y_vals[-1] = y_vals[-1] - extra_dist_y

elif (x_vals[-1] < 0):
  extra_dist_x = -x_vals[-1]
  extra_t = (extra_dist_x / (x_vals[-2] - x_vals[-1])) * (t_vals[-1] - t_vals[-2])
  extra_dist_y = (extra_dist_x / (x_vals[-2] - x_vals[-1])) * (y_vals[-1] - y_vals[-2])
  
  x_vals[-1] = x_vals[-1] + extra_dist_x
  t_vals[-1] = t_vals[-1] - extra_t
  y_vals[-1] = y_vals[-1] - extra_dist_y



fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-100, 1100), ylim=(min(y_vals)-100, max(y_vals)+100))

photon=plt.Circle((0,0),radius=10,facecolor='black')
ax.add_patch(photon)
path_line, = ax.plot([], [], 'b-', linewidth=1)
ax.axvline(0, color='red', linestyle='--')
ax.axvline(distance, color='red', linestyle='--')
# ax.set_aspect('equal', adjustable='box')
# ^ Optional setting to turn the axis scales equal

ax.set_xlabel("x position (m)")
ax.set_ylabel("y position (m)")
ax.set_title("Overhead View of Photon Path")

def init():
  photon.center = (0.0, 0.0)
  path_line.set_data([], [])
  return photon, path_line

ideal_time_step = 100.0*10**(-7) / 500
frames = int(t_vals[-1]/ideal_time_step)
time_step = t_vals[-1] / (frames - 1)

def animate(j):
  i = 0
  while ((i < len(t_vals)-2)) and ((j * time_step) >= t_vals[i+1]):
    i += 1
  vel_x = (x_vals[i+1] - x_vals[i]) / (t_vals[i+1] - t_vals[i])
  vel_y = (y_vals[i+1] - y_vals[i]) / (t_vals[i+1] - t_vals[i])
  t = j * time_step - t_vals[i]
  x = x_vals[i] + vel_x * t
  y = y_vals[i] + vel_y * t
  photon.center = (x, y)

  path_line.set_data(list(x_vals[:i+1]) + [x], list(y_vals[:i+1]) + [y])

  return photon, path_line

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=20, blit=False)

if x_vals[-1] <= 1.0:
  print("The photon was reflected backwards out of the slab in", t_vals[-1], "seconds")

if x_vals[-1] >= 999.0:
  print("The photon passed through the slab in ", t_vals[-1], "seconds")

plt.show()

