import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

n = 4
names = ["Marco","Ricardo","Liz","Madian"]
ages = [22,21,22,24]
professions = ["LF","LM","LID","LF"]

Data_names = ["Name","Age","Profession"]
JsData = []

for i in range(0,4):
    JsData.append([names[i],ages[i],professions[i]])

PdData = pd.DataFrame(data=JsData,columns=Data_names)

print(PdData)

data_set = PdData.to_dict("index")
print(data_set)

json_dum = json.dumps(data_set)

