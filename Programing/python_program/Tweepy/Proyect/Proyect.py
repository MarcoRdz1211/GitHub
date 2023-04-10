import tweepy
from time import sleep
from datetime import datetime
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

consumer_key , consumer_secret = '7e6cuJ8kohdLmariUITYVwOAX' , 'xgaEqH3HhwX6ETlJKX4bqeDTQSyyYBGvnjmHQb4zQPBXrdyewo'
access_token , access_token_secret = '741791745818517504-ldNlf05F9DN420vvfAmcUhr7DVPInIn' , 'iMtDaxgc7UPdLuPFbyeS9w53TySK6Ib6XzFmXjZPfkYfK'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True,wait_on_rate_limit=True)
name,ID = api.me().name,api.me().id

print(name)

palabra = input("Buscar [Cada palabra separada por comas]: ").split(",")
numero_de_Tweets = int(input(u"Número de tweets a capturar: "))
#Continue---------------------------------------------------------------

def DataFrameTweets(palabra="",times=100):
    #Se define las listas que capturan la popularidad
    geo = '25.724903, -100.311564,1000' #UANL, Monterrey, Nuevo León, México, radio: 1000km
    Datos = []
    n = 1
    #tweepy.cursor(api.search, palabra, lang [idioma], geo [especifico por tweeter], )
    for tweet in tweepy.Cursor(api.search, palabra, lang="es").items(numero_de_Tweets):#geo="25.6866,100.3161,500"            #    for tweet in tweepy.Cursor(api.search, palabra, geo).items(numero_de_Tweets):
        sleep_on_rate_limit=False
        print(n)
        try:
            analisis = TextBlob(tweet.text).translate(from_lang="es", to="en").sentiment #HTTP Error 403: Forbidden Problem
            Datos.append([tweet.id,
#                         tweet.user.name,
                          ascii(tweet.text),
                          tweet.favorite_count,
                          tweet.coordinates,
                          analisis.polarity])

            print("Id={}".format(tweet.id),
                  "\n Username={}".format(tweet.user.name),
                  "\n Text={}".format(ascii(tweet.text)),
                  "\n Favs={}".format(tweet.favorite_count),
                  "\n Coordinates={}".format(tweet.coordinates),
                  "\n Retweets={}".format(tweet.retweet_count),
                  "\n Popularity={}".format(analisis.polarity))

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
        n += 1
        input()

    return Datos

Data_names = ["ID","Tweet","favs_count","position","popularity"]
JsData = DataFrameTweets(palabra,numero_de_Tweets)
PdData = pd.DataFrame(data=JsData,columns=Data_names)

PdData.to_csv('pandas_data_tweepy_{}.csv'.format(*palabra)) #¡Pendiente!
PdData.to_excel('pandas_data_tweepy_{}.xlsx'.format(*palabra),sheet_name="{}".format(*palabra)) #¡Pendiente!

data_set = dict.fromkeys(range(1,numero_de_Tweets+1),[])
i = 0
for dat in data_set.keys():
    data_set[dat] = dict(zip(Data_names,JsData[i]))
    i += 1

#print(data_set)

json_dump = json.dumps(data_set)

with open('json_data_tweepy_{}.json'.format(*palabra), 'w') as outfile:
    json.dump(json_dump, outfile)

with open("Analisis_{}.txt".format(*palabra),"w")  as f:
    for t1,t2 in data_set.items():
        f.write(str(t1)+"-"+str(t2)+"\n")
