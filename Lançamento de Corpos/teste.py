from cmath import cos, sin
import numpy as np
import matplotlib.pyplot as plt
import math

x = 0
x0 = 0
y = 0
y0 = 0
vx = 0
v0x = 0
vy = 0
v0y = 0
g = 10
kAt = 1

pi = math.pi
v0 = 10
theta = pi/4
t = 0
tm = 10  # tempo máximo
DT = 0.01

v0x = v0*math.cos(theta)
v0y = v0*math.sin(theta)

x0 = 0
y0 = 0

x = np.array([], dtype=np.float)
y = np.array([], dtype=np.float)


for j in np.arange(DT, tm, DT):
    
    vx = v0x + DT*(-kAt*v0x)

    vy = v0y + DT*(-g-kAt*v0y)

    x = x0 + DT*v0x

    new_x = np.append(x, x)

    y = y0 + DT*v0y

    new_y = np.append(y, y)

    x0 = x
    y0 = y
    v0x = vx
    v0y = vy


plt.plot(new_x, new_y)
plt.show()
