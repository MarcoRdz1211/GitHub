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

palabra = str(input("Buscar: "))
numero_de_Tweets = int(input(u"Número de tweets a capturar: "))
#today = datetime.datetime.now()
#today = today.replace(hour=23, minute=59, second=59, microsecond=999999)
#time_to_the_past = 7
#before = today - datetime.timedelta(time_to_the_past)

#Continue---------------------------------------------------------------
#for tweet in tweepy.Cursor(api.search, palabra).items(numero_de_Tweets):
#    sleep_on_rate_limit=False

#    try:
#        if api.search(tweet.text)==[]:
#            pass
#        else:
#           searchtweet = api.search(tweet.text)
#            ID = searchtweet[0].id
#            sname = api.get_user(ID)
#            loc = tweet.get('user',{}).get('location',{})

#    except tweepy.TweepError as e:
#        print(e.reason)

#    except StopIteration:
#        break

#Continue---------------------------------------------------------------

def ObtenerTweets(palabra="",times=100):
    #Se define las listas que capturan la popularidad
    user,tweet_list = [],[]
    popular_list,num_list,num = [],[],1
    for tweet in tweepy.Cursor(api.search, palabra).items(numero_de_Tweets):
        sleep_on_rate_limit=False
        try:
            #Se toma el texto, se hace el analisis de sentimiento y se agrega el resultado a las listas
            user.append(tweet.id)
            tweet_list.append(tweet.text)
            analisis = TextBlob(tweet.text).sentiment
            popular_list.append(analisis.polarity)
            num_list.append(num)
            num += 1
#                df2 = pd.DataFrame(data=[[tweet.id]])

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break

#    user,tweet_list,
    return (user,num_list,popular_list,num)

def GraficarDatos(numeros_list,popularidad_list,numero):
    axes = plt.gca()
    axes.set_ylim([-1, 2])
    
    plt.scatter(numeros_list, popularidad_list)
    plt.plot(numeros_list,np.zeros(len(numeros_list)))
    popularidadPromedio = (sum(popularidad_list))/(len(popularidad_list))
    popularidadPromedio = "{0:.0f}%".format(popularidadPromedio * 100)
    time = datetime.now().strftime("Time : %H:%M\n Date: %m-%d-%y")
    plt.text(len(numeros_list)/2, 1.25, 
             "Sentimiento promedio:  " + str(popularidadPromedio) + "\n" + time, 
             fontsize=12, 
             bbox = dict(facecolor='none', 
                         edgecolor='black', 
                         boxstyle='square, pad = 1'))
    
    plt.title("Sentimientos sobre " + palabra + " en twitter")
    plt.xlabel("Numero de tweets"),plt.ylabel("Sentimiento")
    plt.show()

#user,tweet_list
user,numeros_list,popularidad_list,numero = ObtenerTweets(palabra,numero_de_Tweets)

GraficarDatos(numeros_list,popularidad_list,numero) 
