import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


n = int(input("Give the number of steps "))
m,a = 0.0,1.0

A_null = np.zeros(n)
X,Y = np.random.normal(m,a,n),np.random.normal(m,a,n)
X_data,Y_data = [],[]
Delta,DeltaT = 0.001,0.000001

for i in range(0,n):
    x0,y0 = sum(X[:1]),sum(Y[:1])
    X_data.append(sum(X[:i])),Y_data.append(sum(Y[:i]))

def Xhistoriagram(X,name):
    plt.figure()
    plt.title("Historiagram of {}_data".format(name))
    plt.xlabel("Number"),plt.ylabel(name)
    plt.hist(X)

def Yhistoriagram(Y,name):
    plt.figure()
    plt.title("Historiagram of {}_data".format(name))
    plt.xlabel(name),plt.ylabel("Number")
    plt.hist(Y)

def TotalFigure(X_data,Y_data):
    plt.figure()
    plt.title("Normal Distribution")
    plt.xlabel("X"),plt.ylabel("Y")
    plt.scatter(X_data,Y_data,c="blue")
    plt.plot(X_data,Y_data,c="blue")

Xhistoriagram(X,"X")

Yhistoriagram(Y,"Y")

TotalFigure(X_data,Y_data)

fig = plt.figure()
ax = fig.gca()
def act(j):
    ax.plot(X_data[:j+1],Y_data[:j+1])
    plt.grid()

    plt.title("Normal Distribution")
    plt.xlabel("X"),plt.ylabel("Y")
    #plt.plot(X_data,A_null,c="black") #Eje x
    #plt.plot(A_null,Y_data,c="black") #Eje y
    

ani = animation.FuncAnimation(fig,act,range(n),interval=10,repeat=False)


#plt.savefig("RandomWalk{}".format(n))
plt.show()
