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
    #tweepy.cursor(api.search, palabra, lang [idioma], geo [especifico por tweeter], )
    for tweet in tweepy.Cursor(api.search, palabra).items(numero_de_Tweets):            #    for tweet in tweepy.Cursor(api.search, palabra, geo).items(numero_de_Tweets):
        sleep_on_rate_limit=False
        print(n)
        try:
#            print("The number of favs in the tweet is: {}".format(api.get_status(tweet.id).favorite_count))
            user.append(tweet.id)
            tweet_list.append(tweet.text)
            fav_list.append(api.get_status(tweet.id).favorite_count)
#            print("Favorite count = {}".format(api.get_status(tweet.id).favorite_count))
            analisis = TextBlob(tweet.text).translate(from_lang="es", to="en").sentiment #HTTP Error 403: Forbidden Problem
            popular_list.append(analisis.polarity)
            num_list.append(num)
            num += 1

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
        n += 1

    return (user,tweet_list,fav_list,num_list,popular_list,num)

def GraficarDatos(palabra,numeros_list,popularidad_list,numero):
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
    
    plt.title("Sentimientos sobre {} en twitter".format(*palabra))
    plt.xlabel("Numero de tweets"),plt.ylabel("Sentimiento")
    plt.savefig("{}".format(*palabra))
    plt.show()

user_list,tweet_list,fav_list,numeros_list,popularidad_list,numero = ObtenerTweets(palabra,numero_de_Tweets)

Data = [[],[]]

for i in range(0,numero_de_Tweets):
    Data[0].append(user_list[i])
    Data[1].append([ascii(tweet_list[i]),fav_list[i],popularidad_list[i]])

data_set = dict.fromkeys(Data[0],[])
i = 0
for dat in data_set.keys():
    data_set[dat] = dict(zip(["Tweet","favs_count","popularity"],Data[1][i]))
    i += 1

#print(data_set)

json_dump = json.dumps(data_set)
#print(json_dump)
#json_object = json.loads(json_dump)

with open('json_data_tweepy_{}.json'.format(*palabra), 'w') as outfile:
    json.dump(json_dump, outfile)

with open("Analisis_{}.txt".format(*palabra),"w")  as f:
    for i in range(0,numero_de_Tweets):
        f.write(data_set[i])
#        f.write("{} [ID: {}]: {} ({} favorites),Popularity={} \n".format(numeros_list[i],user_list[i],TextTweet,fav_list[i],popularidad_list[i]))


#GraficarDatos(palabra,numeros_list,popularidad_list,numero)
