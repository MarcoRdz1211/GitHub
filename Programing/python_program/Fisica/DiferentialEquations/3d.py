import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return np.sin(5.5*np.power(x,1))*np.cos(5*np.power(y,1))+np.power(x,2)+1

fig = plt.figure()
ax = plt.axes(projection='3d')

X0,Y0 = np.linspace(-1,1,100), np.linspace(-1,1,100)
X,Y = np.meshgrid(X0,Y0)
Z = f(X,Y)

ax.set_xlabel("t")
ax.set_ylabel("x")
ax.set_zlabel("psi(x,t)")
ax.plot_surface(X,Y,Z,cmap="viridis")

plt.show()
