import tweepy
import json

consumer_key , consumer_secret = '7e6cuJ8kohdLmariUITYVwOAX' , 'xgaEqH3HhwX6ETlJKX4bqeDTQSyyYBGvnjmHQb4zQPBXrdyewo'
access_token , access_token_secret = '741791745818517504-ldNlf05F9DN420vvfAmcUhr7DVPInIn' , 'iMtDaxgc7UPdLuPFbyeS9w53TySK6Ib6XzFmXjZPfkYfK'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True,wait_on_rate_limit=True)

user = api.me()
name,ID = user.name,user.id_str
#sname = '@Marco_Rdz121199'
sname = '@charlycarmona00'
print(sname)
print(ID)

print("Wich information do you want? \n",
      "a) Settings \n",
      "b) Search \n",
      "c) Search2 \n",
      "d) Favorites \n",
      "e) Retweets \n",
      "f) SearchTweet \n",
      "g) User_Followers \n",
      "h) User_Followers2 \n",
      "i) SavedSearches \n",
      "j) Geolocalization \n",
      "k) PlaceTrends \n")
answer = input()

if answer=="a":
    print("------------------------------Settings")
    sett = api.get_settings()
    print(sett) 

elif answer=="b":
    print("------------------------------Search")
    favorites = api.favorites()

    for status in favorites:
        print(status.user.screen_name)

elif answer=="c":
    print("------------------------------Search2")
    search = api.user_timeline(screen_name = sname, count = 100, include_rts = True) 

    for i in range(0,5):
        try:
            print (i,"-Tweet text:", search[i].text)
        except:
            print(i,"+Tweet text: UnicodeEncodeError")

elif answer=="d":
    print("------------------------------Favorites")
    fav = api.favorites(screen_name = sname, count = 100, include_rts = True) 

    for i in range(0,5):
        try:
            print (i,"-Favorite text:", fav[i].text)
        except:
            print(i,"+Tweet text: UnicodeEncodeError")

elif answer=="e":
    print("------------------------------Retweets")
    retweet = api.retweets_of_me(screen_name = sname, count = 100, include_rts = True) 

    for i in range(0,5):
        try:
            print (i,"-Retweet text:", retweet[i].text)
        except:
            print(i,"+Retweet text: UnicodeEncodeError")

elif answer=="f":
    print("------------------------------SearchTweet")
    searchtweet = api.search("te amo persona con vibra bonita y contagiosa" , include_rts = True)

    print(searchtweet[0])

    print(searchtweet[0].text)
    print(searchtweet[0].id)
    #print(searchtweet['favourites_count'])
    print(api.get_status(searchtweet[0].id)['favourites_count'])

elif answer=="g":
    print("------------------------------User_Followers")
    followers = api.followers_ids(screen_name = sname, count = 5)

    for follow in followers:
        try:
            user_i = api.get_user(follow)
            print(user_i.name,"[ID={}]".format(follow))
        except:
            print("Not recognized","[ID={}]".format(follow))

elif answer=="h":
    print("------------------------------User_Followers2")
    followers_2 = api.followers_ids(screen_name = sname, count = 5)

    for follow in followers_2:
        try:
            user_i = api.get_user(follow)
            print(user_i.name,"[ID={}]".format(follow))
        except:
            print("Not recognized","[ID={}]".format(follow))

elif answer=="i":
    print("------------------------------SavedSearches")
    saved = api.saved_searches()
    print(saved)

#print("------------------------------Get_list")

#for status in favorites:
#    tweeter_list = api.lists_all(screen_name=status.user.screen_name)
#    print(tweeter_list)

elif answer=="j":
    print("------------------------------Geolocalization")
    geo = api.reverse_geocode(25.6751 , -100.3185) #Monterrey, N.L., Mexico
    print(geo) #Falta obtener id!!!

elif answer=="k":
    print("------------------------------PlaceTrends")
    trends = api.trends_place(110978) #Woeid: Mexico, https://codebeautify.org/jsonviewer/f83352

    for value in trends:
        for trend in value['trends']:
            print(trend['name'])

else:
    print("------------------------------SearchTweet2")
    for tweet in tweepy.Cursor(api.search, "te amo persona con vibra bonita y contagiosa").items(1):            #    for tweet in tweepy.Cursor(api.search, palabra, geo).items(numero_de_Tweets):
        for t in tweet.items():
            print(t)
            
#        print(tweet.favorite_count)

    print(searchtweet[0])

    print(searchtweet[0].text)
    print(searchtweet[0].id)
    #print(searchtweet['favourites_count'])
    print(api.favorites(searchtweet[0].id).favorite_count)
