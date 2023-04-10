import math
import numpy as np
import matplotlib.pyplot as plt
 
def I(alpha,x):
    y = 0
    
    for n in range(0,30):
        y += ((x/2)**(2*n+alpha))/(math.gamma(n+1)*math.gamma(n+alpha+1))
        
    return y

def phi_k(k,r,z):
    y = 2*V*I(0,k*r)*np.sin(k*z)/(pi*k*I(0,k*a))
    
    return y

def phi(r,z):
    delta_k = 100/s
    y = 2*V*delta_k/pi
    
    for n in range(1,s):
        y += phi_k(n*delta_k,r,z)*delta_k

    return y

def data(DataR,DataZ,DataPhi):
    TextFile = open("Data-Potencial_cilindrico.txt","w+")

    TextFile.write(" z/r        "+"{}".format(DataZ))

    for i in range(0,len(DataZ)):
        TextFile.write("\n {:.8f}   {} ".format(DataR[i],DataPhi[i]))

    TextFile.close()

#Constants
s,pi = 10**4,math.pi
a,V = 1.97,10.3
z_lim = 10

print("phi(r,z)=2({})/pi int_0^infty I(0,kr)/I(0,k({})) sin(kz)/k dk ".format(V,a))
print("Interval=[0,{}]x[-{},{}]".format(a,z_lim,z_lim))

#MeshData
r_initial,z_initial = np.linspace(0,a),np.linspace(-z_lim,z_lim)
r_data,z_data = np.meshgrid(r_initial,z_initial)
phi_data = phi(r_data,z_data)

data(r_initial,z_initial,phi_data)

#3D-Plot
fig = plt.figure()

ax = fig.add_subplot(projection='3d')
ax.set_title("Problem of cylindrical potential")
ax.set_xlabel("r") , ax.set_ylabel("z") , ax.set_zlabel("phi(r,z)")
ax.plot_surface(r_data,z_data,phi_data,cmap="viridis")

#Save&ShowFigure
plt.savefig("Problema_potencial_cilindro.png")

plt.show()
