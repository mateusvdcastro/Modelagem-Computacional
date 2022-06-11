import numpy as np
import matplotlib.pyplot as plt
import math

g = -10
m = 5
kAt = 5
pi = math.pi
theta = pi / 6
DT = 0.001
t = [0]
T = 10

vetResultV = [10]  # ex: 10 m/s

vetX = [vetResultV[0]*math.cos(theta)]

# print(vetX)

vetY = [vetResultV[0]*math.sin(theta)]

# print(vetY)

vetSx = [0]
vetSy = [0]
vetResultS = []

Sy = vetSy[0]

Ec = [(((vetResultV[0])**2) * m) /2]
Ep = [abs((m * g * vetSy[0]))]
Em = [Ec[0] + Ep[0]]


i = 1


for j in np.arange(DT, T, DT):
  vX = vetX[i - 1] + ((-kAt * vetX[i - 1])/m) * DT
  vetX.append(vX)

  if (Sy >= 0):
    vY = vetY[i - 1] + (g - (kAt/m) * vetY[i - 1]) * DT
    vetY.append(vY)
  else:
    vY = -1 * (vetY[i - 1] + (g - (kAt/m) * vetY[i - 1]) * DT)
    vetY.append(vY)

  Sx = vetSx[i - 1] + vetX[i] * DT
  vetSx.append(Sx)

  Sy = vetSy[i - 1] + vetY[i] * DT
  vetSy.append(Sy)

  vetV = math.sqrt((vetX[i])**2 + (vetY[i])**2)
  vetResultV.append(vetV)

  vetS = math.sqrt((vetSx[i])**2 + (vetSy[i])**2)
  vetResultS.append(vetS)

  Ec.append((((vetResultV[i])**2) * m) /2)

  Ep.append(abs((m * g * vetSy[i])))

  Em.append(Ec[i] + Ep[i])

  t.append(t[i - 1] + DT)

  i = i + 1


# plt.plot(t, vetX) 

#plt.plot(t, vetY)

# plt.plot(vetSx)

# plt.plot(vetSy)

# plt.plot(vetSx, vetSy)

# plt.plot(t, vetSx)

# plt.plot(t, Ep)

# plt.plot(t, vetResult)

# plt.plot(t[1:], vetResultS)

plt.show()
