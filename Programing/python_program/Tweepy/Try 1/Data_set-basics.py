import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

n = 4
Data_names = ["Name","Age","Profession"]
names = ["Marco","Ricardo","Liz","Madian"]
ages = [22,21,22,24]
professions = ["LF","LM","LID","LF"]

JsData = []
for i in range(0,4):
    JsData.append([names[i],ages[i],professions[i]])

print("The Data in Array's format is:") #Simil a 
for data in JsData:
    print(*data)

print("-------------------------")

PdData = pd.DataFrame(data=JsData,columns=Data_names)

print("The Data in panda's format is: \n",PdData) #Simil a una tabla de excel

print("-------------------------")

data_set = dict.fromkeys(range(1,4+1),[])
i=0

for dat in data_set.keys():
    data_set[dat] = dict(zip(Data_names,JsData[i]))
    i += 1

print("The Data in Json's dump format is: \n",data_set) #Forma de diccionario

print("-------------------------")

json_dump = json.dumps(data_set)

with open('Try_data1-json.json','w') as outfile:
    json.dump(json_dump,outfile)

with open("Try_data1-text.txt","w")  as f:
    for data in data_set.items():    
        f.write(" ".join(map(str, data))+"\n")

PdData.to_excel("SegundoIntento.xlsx",sheet_name="Primer_Intento")
