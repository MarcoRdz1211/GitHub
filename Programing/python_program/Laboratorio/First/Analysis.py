import random
import numpy as np
import matplotlib.pyplot as plt

#text = ["Directo","Directo_Alcohol","Horno_6_dias",
#        "OxGraf_pendiente","Sample08","Sample09",
#        "Vacio_72_hrs"]

text = ["Directo","Horno_6_dias",
        "Vacio_72_hrs"]

color = ["red","blue","green","yellow","black","pink","orange"]

def graph(text,color):
    f = open("{}.txt".format(text), "r")
    
    X,Y = [],[]
    X_zero,Y_zero = 5,5
    
    for x in f:
        a,b = x.split()
        a,b = float(a),float(b)

        if b>-0.1:
            X.append(a),Y.append(b)
            
        else:
            break

        if (Y_zero>=0 and a<500):
            X_zero,Y_zero = a,b
            
    
    f.close()
    
    X_axis = [[200,max(X)],[0,0]]
    Y_axis = [[200,200],[0,max(Y)]]    

#    plt.scatter(X,Y,c=color)
    plt.plot(X,Y,c=color,label=text)
    plt.xlabel('2'r'$\theta$°'),plt.ylabel("Absorbance")
    plt.plot(X_axis[0],X_axis[1],c="black")
    plt.plot(Y_axis[0],Y_axis[1],c="black")
    plt.scatter([X_zero],[Y_zero],c="black")

def one_graph(text,color):
    for i in range(0,len(text)):
        plt.figure()
        graph(text[i],color[i])

        plt.title("Data-{}".format(text[i]))
        plt.legend()
        plt.savefig("Data-{}".format(text[i]))
#        plt.show()

def all_graph(text,color):
    plt.figure()
    for i in range(0,len(text)):
        graph(text[i],color[i])

    plt.title("All_data")
    plt.xlabel('2'r'$\theta$°'),plt.ylabel("Absorbance")
    plt.legend()
    plt.savefig("All_data")
    plt.show()

one_graph(text,color)
all_graph(text,color)
