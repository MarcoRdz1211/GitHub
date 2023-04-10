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

def ObtenerTweets(palabra="",times=100):
    #Se define las listas que capturan la popularidad
    geo = '25.724903, -100.311564,1000' #UANL, Monterrey, Nuevo León, México, radio: 1000km
    user,tweet_list = [],[]
    fav_list,popular_list,num_list,num = [],[],[],1
    n = 1
    All_data = []
    #tweepy.cursor(api.search, palabra, lang [idioma], geo [especifico por tweeter], )
    for tweet in tweepy.Cursor(api.search, palabra).items(numero_de_Tweets):            #    for tweet in tweepy.Cursor(api.search, palabra, geo).items(numero_de_Tweets):
        sleep_on_rate_limit=False
        print(n)
        try:
            num += 1
            ID = tweet.id
            print("ID={}".format(ID))
            User = tweet.user.name
            print("User={}".format(User))
            Text = tweet.text
            print("Text={}".format(ascii(Text)))
            Fav = api.get_status(ID).favorite_count
            print("Number of favs={}".format(Fav))
            Feeling = TextBlob(Text).sentiment.polarity
            print("Feelings={}".format(Feeling))

            print("-----------")

            data_set = {"User": User, "ID": ID, "Text": Text, "Favorites": Fav, "Sentiment": Feeling}
            All_data.append(data_set)

        except tweepy.TweepError as e:
            print("This is an error: {}".format(e.reason))

        except StopIteration:
            break

        n += 1

    return All_data

def ImprimirDatos(Data,numero_de_Tweets):
    for i in range(0,numero_de_Tweets):
        print(Data[i])
        TextTweet = ascii(Data[i].Text)
        f.write("{} [ID: {}]: {} ({} favorites),Popularity={} \n".format(Data[i].User,Data[i].ID,Data[i].Text,Data[i].Favorites,Data[i].Sentiment))

Data = ObtenerTweets(palabra,numero_de_Tweets)

f = open("Anlisis.txt","w")

ImprimirDatos(Data,numero_de_Tweets)

#GraficarDatos(palabra,numeros_list,popularidad_list,numero) 
f.close()
