import tweepy
import random
import emoji
import threading

#Twitter API keys and tokens
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#List of emojis
#You can edit the list as you please, here's a full list of emojis (https://www.webpagefx.com/tools/emoji-cheat-sheet/)
emojis = [':boom:', ':star:', ':fire:', ':sweat_drops:', ':pray:', ':droplet:', ':tongue:', ':pouting_cat:', ':guardsman:', ':umbrella:', ':sunny:', ':cloud:', ':zap:', ':snake:', ':honeybee:', ':four_leaf_clover:', ':palm_tree:', ':earth_americas:', ':full_moon:', ':tada:', ':hourglass_flowing_sand:', ':phone:', ':key:', ':moneybag:', ':toilet:', ':bath:', ':gun:', ':pill:', ':chart_with_upwards_trend:', ':notebook:', ':shoe:', ':tea:', ':briefcase:', ':eyeglasses:', ':beers:', ':baby_bottle:', ':pizza:', ':fries:', ':hamburger:', ':sushi:', ':bread:', ':honey_pot:', ':peach:', ':sunrise:', ':recycle:' ]

#Enter your base name here (Emoji will be after it)
default_name_base = "Andrei "

def emoji_picker():
    #Picks a random emoji from the list
    random_emoji = emoji.emojize(random.choice(emojis), use_aliases=True)
    
    #Makes sure the length is not more than 20 (twitter's default username limit)
    if (len(random_emoji) and len(default_name_base) > 20):
        emoji_picker()
        
    else:
        
        #Updates your profile to show your default_name_base and random emoji
        api.update_profile(default_name_base + random_emoji)
        print('Random emoji added to name!', random_emoji)
    threading.Timer(30.0, emoji_picker).start()


emoji_picker()
