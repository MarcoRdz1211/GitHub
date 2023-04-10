import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def func(V0,R0,a0,r):
    return -V0/(1+np.exp((r-R0)/a0))

a,b = 0,3
V0,R0,A=1,1,[10**(-1),10**(-2),10**(-3)]
n = 1000
R = np.linspace(a,b,n)
V = []

for a0 in A:
    V.append(func(V0,R0,a0,R))

def plot_function(R,V,j):
    plt.title("Saxon-Woods Potential")

    rgb = [random.random(),random.random(),random.random()]

    plt.grid()
    plt.xlabel("r"),plt.ylabel("V(r)")
    plt.plot(R,np.zeros(n),c="black")
    plt.plot(np.zeros(n),V,c="black")
    plt.plot(R,V,c=rgb,label="-{}/(1+np.exp((r-{})/{}))".format(V0,R0,A[j]))

plt.figure()
for j in range(0,len(A)):
    plot_function(R,V[j],j)

plt.legend()
plt.savefig('Saxon-Woods Potentials')

fig = plt.figure()
ax = fig.gca()

plt.plot(R,np.zeros(n),c="black")
plt.plot(np.zeros(n),V[0],c="black")

def act(j):
    for k in range(0,len(A)):
        ax.plot(R[:j+1],V[k][:j+1])
        
    plt.grid()

    plt.title("Saxon-Woods Potential ({}<x<{})".format(R[0],R[j]))
    plt.xlabel("r"),plt.ylabel("V(r)")

ani = animation.FuncAnimation(fig,act,range(n),interval=1,repeat=False)
ani.save('Saxon-Woods Potentials.mp4', fps=10, dpi=80)
plt.show()
