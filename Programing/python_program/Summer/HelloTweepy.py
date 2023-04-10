import tweepy
import json

consumer_key , consumer_secret = 'zJYUlDo4mUGiEwKE5NzXCphfd' , 'c0BwfJvrMw2wz21xI6PZl3xLALyhuZK2KqC9C1tpDEzxTWwaT7'
access_token , access_token_secret = '741791745818517504-jVDQdYon0vpcg3a3gwM4qaPWttt5XEG' , 'wpi6xVT4167Aql78oF6HkTeeNN1ub2s3pALDR6HhZ43uV'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify=True,wait_on_rate_limit=True)

user = api.me()
name,ID = user.name,user.id_str
print(name)
print(ID)

print("------------------------------NumberOfFollowers")
print("My number of followers is: {}".format(user.followers_count))
#for followers in user.followers():
#    print(followers.screen_name)

print("------------------------------NumberOfFriends")

print("My number of friends is: {}".format(user.friends_count))
#for friend in user.friends():
#       print(friend.screen_name)
