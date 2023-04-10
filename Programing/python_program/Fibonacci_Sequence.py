import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

n = 20
X,Y = [0,1],np.zeros(n+2)

for i in range(0,n):
    X.append(X[i]+X[i+1])

plt.figure()
plt.title("Fibonacci Sequence (Terms={})".format(n+1))
plt.scatter(X,Y,c="red")
plt.plot([-1,1.1*max(X)],[0,0],c="blue")
plt.savefig("Fibonacci Sequence (Terms={})".format(n+1))

fig = plt.figure()
ax = fig.gca()

def act(j):
    ax.scatter(X[:j+1],Y[:j+1])
    plt.plot([-1,1.1*max(X[:j+1])],[0,0],c="blue")

    plt.title("Fibonacci Sequence (Terms={})".format(j))

ani = animation.FuncAnimation(fig,act,range(n+2),interval=1000,repeat=False)
ani.save("Fibonacci Sequencen (Terms={}).mp4".format(n+1), fps=10, dpi=80)
plt.show()
