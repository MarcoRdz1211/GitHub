import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

n = 4
Data_names = ["Name","Age","Profession"]
names = ["Marco","Ricardo","Liz","Madian"]
ages = [22,21,22,24]
professions = ["LF","LM","LID","LF"]

print("-------------------------Arrays Data-------------------------")

JsData = []
print("The Data in Array's format is:") #Datos en formato de arreglo
for i in range(0,4):
    data = [names[i],ages[i],professions[i]]
    JsData.append(data)
    print(*data)

print("-------------------------Pandas Data-------------------------")

PdData = pd.DataFrame(data=JsData,columns=Data_names)

print("The Data in panda's format is: \n",PdData) #Simil a una tabla de excel

print("-------------------------Dictionary Data-------------------------")

data_set = dict.fromkeys(range(1,4+1),[])
i=0

for dat in data_set.keys():
    data_set[dat] = dict(zip(Data_names,JsData[i]))
    i += 1

print("The Data in Json's dump format is: \n",data_set) #Forma de diccionario

print("-------------------------Save Data-------------------------")

json_dump = json.dumps(data_set)

with open('Try_data1-json.json','w') as outfile:
    json.dump(json_dump,outfile)

with open("Try_data1-text.txt","w")  as f:
    for data in data_set.items():    
        f.write(" ".join(map(str, data))+"\n")

PdData.to_excel("SegundoIntento.xlsx",sheet_name="Primer_Intento")
