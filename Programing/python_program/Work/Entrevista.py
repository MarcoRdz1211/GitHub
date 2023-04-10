import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

excel_data = pd.read_excel("Dataset Entrevistas.xlsx",sheet_name="Sheet1")
Data = pd.DataFrame(excel_data)

#print("All data: \n", Data)

clients,industry = set(Data["client_id"]),set(Data["industry"])
n = len(clients)
#print(clients)
#print(industry)
Data_set = Data.to_dict("index")
print("-----------------------")

writer = pd.ExcelWriter("Dataset Entrevistas.xlsx")
Data.to_excel(writer,sheet_name="All")

for i in clients:
    print("{}/{}".format(i,n))
    Data_new = Data.loc[Data["client_id"]==i]
    Data_new.to_excel(writer,sheet_name="{}".format(i))

writer.save()
