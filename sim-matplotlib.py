import matplotlib.pyplot as plt
import matplotlib.animation as animation
from variables import *
from physics import *
phistory = run_simulation(p, v, m, t, dt, l, rc, k, r0)


fig = plt.figure()

ax = fig.add_subplot(projection='3d')

ax.set_xlim(0, l)
ax.set_ylim(0, l)
ax.set_zlim(0, l)


x = phistory[0, :, 0]
y = phistory[0, :, 1]
z = phistory[0, :, 2]

scat = ax.scatter(x, y, z, color='blue', s=50)


def update(frame):
    x = phistory[frame, :, 0]
    y = phistory[frame, :, 1]
    z = phistory[frame, :, 2]

    scat._offsets3d = (x, y, z)

    return(scat)

ani = animation.FuncAnimation(fig, update, frames=t, interval=20)

plt.show()