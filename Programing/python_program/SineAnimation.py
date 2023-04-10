import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a,b = -4,4
n = 1000
X = np.linspace(a,b,n)
Y = np.sin(np.power(X,3))

def plot_function(X_data,Y_data):
    plt.title("Sine function")
    plt.grid()
    plt.xlabel("X"),plt.ylabel("Y")
    plt.plot(X,Y,c="blue")

plt.figure()
plot_function(X,Y)

fig = plt.figure()
ax = fig.gca()

def act(j):
    ax.plot(X[:j+1],Y[:j+1])
    plt.grid()

    plt.title("Sine function ({}<x<{})".format(X[0],X[j]))
    plt.xlabel("X"),plt.ylabel("Y")

ani = animation.FuncAnimation(fig,act,range(n),interval=1,repeat=False)
ani.save('SquareSine.mp4', fps=10, dpi=80)
plt.show()
