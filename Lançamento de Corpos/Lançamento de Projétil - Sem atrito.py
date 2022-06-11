import numpy as np
import matplotlib.pyplot as plt


g = 10
m = 5
kAt = 1
theta = 0.9
H = 1000

DT = 0.01
t = [DT]
T = 10
DS = 0

v = [0]
DV = 0

S = [H]

i = 1


for j in np.arange(DT, T, DT): 

  DV = g*DT # 10 * 0.01 = 0.1
  
  DS = v[i-1] * DT # v[0]
  
  print(f"v: {t[i - 1] + DT}")
  v.append(v[i - 1] + DV) # v[0] + 0.1 = 0.1
  
  print(f"S: {t[i - 1] + DT}")
  S.append(S[i-1] - DS) # v[0] - V[0] = 0

  print(f"t: {t[i - 1] + DT}")
  t.append(t[i - 1] + DT) # t[0] + 0.01 = 0.02

  i = i + 1



plt.plot(t, S)
plt.show()
