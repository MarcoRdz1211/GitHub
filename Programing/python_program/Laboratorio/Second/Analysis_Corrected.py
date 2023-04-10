import random
import numpy as np
import matplotlib.pyplot as plt

#text = ["OGdirecto","GODirectoAlcohol","GO24horas",
#       "GO48horas","GO6dias"]

text = ["OGdirecto","GODirectoAlcohol","GO24horas",
        "GO48horas","GO6dias"]

               
text_name = ["Oxido de Grafeno","Grafeno (Alcohol)",
             "Grafeno (24 hrs)","Grafeno (48 hrs)",
             "Grafeno (6 dias)"]

color = ["red","blue","green","yellow","black","pink","orange"]

def graph(text,color,i):
    f = open("{}.txt".format(text), "r")
    
    X,Y = [],[]
    
    for x in f:
        a,b = map(float, x.split())
        X.append(a),Y.append(b)

    f.close()

    i0 = Y.index(max(Y))
    
    X_axis = [[200,600],[0,0]]
    Y_axis = [[200,200],[0,Y[i0]]]

    plt.plot(X[:i0],Y[:i0],c=color,label=text_name[i])
    plt.xlabel('Longitud de onda (nm)'),plt.ylabel("Absorbancia")
    plt.plot(X_axis[0],X_axis[1],c="black")
    plt.plot(Y_axis[0],Y_axis[1],c="black")

def one_graph(text,color):
    for i in range(0,len(text)):
        plt.figure()
        graph(text[i],color[i],i)

        plt.title("Datos: {}".format(text_name[i]))
        plt.legend()
        plt.savefig("Data-{}".format(text_name[i]))
#        plt.show()

def all_graph(text,color):
    plt.figure()
    for i in range(0,len(text)):
        graph(text[i],color[i],i)

    plt.title("Oxido de Grefeno, Grafeno (0,1,2,6 dias)")
    plt.xlabel('Longitud de onda (nm)'),plt.ylabel("Absorbancia")
    plt.legend()
    plt.savefig("All_data")
    plt.show()

one_graph(text,color)
all_graph(text,color)
