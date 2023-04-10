import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd
import random

n,m = 5,25
St_data = list(range(1,n+1))
St_data.append("Final")

#print(*St_data)

JsData = []

for i in range(0,m):
    data = np.random.randint(0,100,size=n)
    data = np.append(data,sum(data)/n)
    JsData.append(data)
#    print(*data)

PdData = pd.DataFrame(data=JsData,columns=St_data,index=range(194100,194100+m)).add_prefix("Grade ")

print(PdData)

print("--------------------------------------------")

data_set = PdData.to_dict("index")
print(data_set)

print("--------------------------------------------")

PdData.to_excel("Taste_GradeAnalysis.xlsx",sheet_name="Grades")

