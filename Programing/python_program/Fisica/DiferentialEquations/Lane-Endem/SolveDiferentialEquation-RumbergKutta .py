import math
import random
import numpy as np
import matplotlib.pyplot as plt

def y1(t,y,v):
    return v

def y2(t,y,v):
    return -6*t

def f1(t):
    return 4*np.power(t,1)-np.power(t,3)

def f2(t):
    return 4-3*np.power(t,2)


t0,y0,v0 = input("Dar el valor inicial del tiempo, la funcion y(t) en ese tiempo, y su respectiva derivada en ese punto: y'(t) ").split()
t0,y0,v0 = float(t0),float(y0),float(v0)
tf = float(input("Dar el valor buscado de la funcion "))
t,y,v = [t0],[y0],[v0]
i,n = 0,200
h = abs(tf-t[0])/n

TextFile = open("FirstDiferentialEquation.txt","w+")
TextFile.write("     t       Y_real     Y_num     V_real      V_num  \n")
TextFile.write("{:.8f} {:.8f} {:.8f} {:.8f} {:.8f} \n".format(t[0],f1(t[0]),y[0],f2(t[0]),v[0]))


#print("     t       Y_real     Y_num     V_real      V_num  \n")
#print("{:.8f} {:.8f} {:.8f} {:.8f} {:.8f}".format(t[i],f1(t[i]),f2(t[i]),y[i],v[i]))
for i in range(0,n+2):
    t.append(t[0]+h*i)
    K = [5*[0],5*[0]]
    K[0][1],K[1][1] = y1(t[i],y[i],v[i]),y2(t[i],-y[i],v[i])
    K[0][2],K[1][2] = y1(t[i]+h/2,y[i]+(h/2)*K[0][1],v[i]+(h/2)*K[1][1]),y2(t[i]+h/2,y[i]+(h/2)*K[0][1],v[i]+(h/2)*K[1][1])
    K[0][3],K[1][3] = y1(t[i]+h/2,y[i]+(h/2)*K[0][2],v[i]+(h/2)*K[1][2]),y2(t[i]+h/2,y[i]+(h/2)*K[0][2],v[i]+(h/2)*K[1][2])
    K[0][4],K[1][4] = y1(t[i]+h,y[i]+h*K[0][1],v[i]+h*K[1][3]),y2(t[i]+h,y[i]+h*K[0][1],v[i]+h*K[1][3])
    y.append(y[i]+(h/6)*(K[0][1]+2*K[0][2]+2*K[0][3]+K[0][4]))
    v.append(v[i]+(h/6)*(K[1][1]+2*K[1][2]+2*K[1][3]+K[1][4]))

#    print("{:.8f} {:.8f} {:.8f} {:.8f} {:.8f}".format(t[i],f1(t[i]),y[i],f2(t[i]),v[i]))
    TextFile.write("{:.8f} {:.8f} {:.8f} {:.8f} {:.8f} \n".format(t[i],f1(t[i]),y[i],f2(t[i]),v[i]))

TextFile.close()

print("El valor analitico de: y({})={:.8f}, y'({})={:.8f} \n".format(t[i],f1(t[i]),t[i],f2(t[i])),
      "mientras que el valor numerico es: y({})={:.8f}, y'({})={:.8f} \n".format(t[i],y[i],t[i],v[i]),
      "con un error porcentual aproximado de: {:.8f}%, {:.8f}%, respectivamente".format(abs(y[i]-f1(t[i]))*100,abs(v[i]-f2(t[i]))*100))

plt.title("Solution of the equation: y''+6x=0")
plt.xlabel("x"),plt.ylabel("y")
plt.plot([min(t),min(t),max(t)],[max(y),min(y),min(y)],c="black")
plt.scatter(t,y,c="black",label="y_num(t)",s=1)
plt.plot(t,f1(t),c="green",label="y_real()")
#plt.xlim([1.1*min(t),1.1*max(t)])
#plt.ylim([1.1*min(y),1.1*max(y)])
plt.legend()

plt.savefig("First_Derivative_Solver.png")

plt.show()
