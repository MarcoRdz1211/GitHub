import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

excel_data = pd.read_excel("Taste_GradeAnalysis.xlsx",sheet_name="Grades") #Get all data
Dataf = pd.DataFrame(excel_data) #Transform data to dataframe

if input("If you want to see all data, write a")=="a":
    print("All data: \n",Data)
    
print("-------------------------Basic Information Data-------------------------")

data_names = list(Dataf.columns) #Get column names
n,m = len(Dataf),len(data_names) #n=Lines & m=Columns

if input("If you want the columns names, write b")=="b":
    print("Columns: \n",data_names)

print("-------------------------Array Data-------------------------")

JsData = Dataf.values #Get all values in array format

if input("")
    print("Los datos crudos son:")
    for data in JsData:
        print(*data)

print("-------------------------Dictionary Data-------------------------")

data_set = Dataf.to_dict("index")
print("Los datos en formato de diccionario son: \n ",data_set)

print("------------------------------------------------------------------------------------------------------------")
