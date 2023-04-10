import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tweepy
import time
import json
from time import sleep
from datetime import datetime
from textblob import TextBlob

t0 = time.time()

consumer_key , consumer_secret = '7e6cuJ8kohdLmariUITYVwOAX' , 'xgaEqH3HhwX6ETlJKX4bqeDTQSyyYBGvnjmHQb4zQPBXrdyewo'
access_token , access_token_secret = '741791745818517504-ldNlf05F9DN420vvfAmcUhr7DVPInIn' , 'iMtDaxgc7UPdLuPFbyeS9w53TySK6Ib6XzFmXjZPfkYfK'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True,wait_on_rate_limit=True)
name,ID = api.me().name,api.me().id

print(name)

palabra = input("Buscar [Cada palabra separada por comas]: ").split(",")
numero_de_tweets = int(input(u"Número de tweets a capturar: "))
#Continue---------------------------------------------------------------

def DataFrameTweets(palabra="",times=100):
    #Se define las listas que capturan la popularidad
    geo = '25.724903, -100.311564,100' #UANL, Monterrey, Nuevo León, México, radio: 100km
    Datos,IDs = [],[]
    Names = ["created_at","id","text","truncated","entities","metadata","source",
             "in_reply_to_status_id","in_reply_to_status_id_str","in_reply_to_user_id",
             "in_reply_to_user_id_str","in_reply_to_screen_name","user","geo",
             "coordinates","place","contributors","is_quote_status","retweet_count",
             "favorite_count","favorited","retweeted","lang","popularity"]
    
    n = 1
    #tweepy.cursor(api.search, palabra, lang [idioma], geo [especifico por tweeter], )
    for tweet in tweepy.Cursor(api.search, palabra, lang="es").items(numero_de_tweets):#geo="25.6866,100.3161,500"            #    for tweet in tweepy.Cursor(api.search, palabra, geo).items(numero_de_Tweets):
        sleep_on_rate_limit=False

        if n%10==0:
            print(n)
            print("---- {:.2f} minutes ---- ".format((time.time()-t0)/60))
        
        try:
            IDs.append(tweet._json["id"])
            X = []

            try:
                analisis = TextBlob(tweet._json["text"]).translate(from_lang="es", to="en").sentiment #HTTP Error 403: Forbidden Problem
                popularity = analisis.polarity

            except:
                popularity = None  
            
            for Items in Names:
                try:
                    X.append(tweet._json[Items])

                except:
                    X.append(None)

            X[-1] = popularity
            Datos.append(X)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

        n += 1
    
    return Names,Datos,IDs


def TratedData(palabra,numero_de_tweets):
    Data_names,JsData,JsIndex = DataFrameTweets(palabra,numero_de_tweets)
    print(len(JsData),len(Data_names),len(JsIndex))
    PdData = pd.DataFrame(data=JsData,columns=Data_names,index=JsIndex)

    print(PdData)

    PdData.to_csv('pandas_data_tweepy_{}.csv'.format(*palabra)) #¡Pendiente!
    PdData.to_excel('pandas_data_tweepy_{}.xlsx'.format(*palabra),sheet_name="{}".format(*palabra))

    print("------------------------------------------------------------")

    data_set = PdData.to_dict("index")

    print(data_set)

    print("------------------------------------------------------------")

    json_dump = json.dumps(data_set)

    with open('json_data_tweepy_{}.json'.format(*palabra), 'w') as outfile:
        json.dump(json_dump, outfile)

TratedData(palabra,numero_de_tweets)

print("---- {:.2f} minutes ---- ".format((time.time()-t0)/60))
