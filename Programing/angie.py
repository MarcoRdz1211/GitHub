import math
import random
import numpy as np
import matplotlib.pyplot as plt

n = 20
S_tigre,S_mwo,Residual = [],[],[]
a,b = 0.5,0.1

for i in range(0,n):
    if i%3==0:
        S_tigre.append(i/n+b)
    else:
        S_tigre.append(i/n)

for i in range(0,n):
    S_mwo.append(a*i+b),Residual.append(a*i-b)

limit_Stigre,limit_Smwo,limit_Residual = [0,1],[0.15,0.15],[0.15,0.15]
curve1 = np.polyfit(S_tigre,S_mwo,1)
f1 = np.poly1d(curve1)

fig = plt.figure()
gs = fig.add_gridspec(2, hspace=0)
axs = gs.subplots(sharex=True, sharey=True)
fig.suptitle("Taste")
axs[1].set_xlabel("S_tigre")

axs[0].set_ylabel("S_mwo")
axs[0].scatter(S_tigre,S_mwo)
axs[0].plot(limit_Stigre,limit_Smwo,linestyle="--")
axs[0].plot(curve1,f1)

axs[1].set_ylabel("Residual")
axs[1].scatter(S_tigre,Residual)
axs[1].plot(limit_Stigre,limit_Residual,linestyle="--")

#plt.savefig("ConstantFunctionByFourier2.png")

plt.show()
