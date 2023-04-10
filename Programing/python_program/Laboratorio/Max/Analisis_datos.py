import random
import numpy as np
import matplotlib.pyplot as plt

#text = ["Directo","Directo_Alcohol","Horno_6_dias",
#        "OxGraf_pendiente","Sample08","Sample09",
#        "Vacio_72_hrs"]

text = ["Y2LGO","Y2LGOT","Y2MGO"]
text_name = ["Less Graphene Oxide","Less Graphene Oxide Trasmitance",
             "More Graphene Oxide"]

color = ["red","blue","green","yellow","black","pink","orange"]

def graph(text,color,i):
    f = open("{}.txt".format(text), "r")
    
    X,Y = [],[]
    
    for x in f:
        a,b = x.split()
        a,b = float(a),float(b)

        X.append(a),Y.append(b)
            
    f.close()
    
    X_axis = [[0,max(X)],[0,0]]
    Y_axis = [[0,0],[0,max(Y)]]

    plt.plot(X,Y,c=color,label=text_name[i])
    plt.xlabel('Longitud de onda (nm)'),plt.ylabel("Absorbancia")
    plt.plot(X_axis[0],X_axis[1],c="black")
    plt.plot(Y_axis[0],Y_axis[1],c="black")
    plt.xlim(290,max(X))

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

    plt.title("Oxido de Grefeno, Grafeno (Horno 72hrs y 6 dias)")
    plt.xlabel('Longitud de onda (nm)'),plt.ylabel("Absorbancia")
    plt.legend()
    plt.savefig("All_data")
    plt.show()

one_graph(text,color)
all_graph(text,color)
