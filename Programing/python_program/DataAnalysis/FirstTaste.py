import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url,header=None)

n = 5
headers = ["symboling","normaized-losses","make","fuel-type","aspiration","num-of-doors",
           "body-style","drive-wheels","engine-location","wheel-base","length","width",
           "height","curb-wieght","engine-type","num-of-cylinders","engine-size",
           "fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm",
           "city-mpg","highway-mpg","price"]

df.columns = headers
df.to_csv("taste.csv")

print("All data frames: \n",df,"\n ------------------")
print("All columns names: \n",df.head(n),"\n ------------------")
print("All tails: \n",df.tail(n),"\n ------------------")
print("All data types: \n",df.dtypes,"\n ------------------")
print("Descriptions: \n",df.describe(include="all"),"\n ------------------")
print("All information: \n",df.info(),"\n ------------------")
