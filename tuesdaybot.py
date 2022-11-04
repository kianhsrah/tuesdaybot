from twython import Twython
import json
import datetime

#Loads keys into array from keys.json
keys = json.loads(open('keys.json').read())

#Account verification and Twython object initializer
API_key = keys[0]
API_secret_key = keys[1]
Access_token = keys[2]
Access_token_secret = keys[3]
TuesdayBot = Twython(API_key, API_secret_key, Access_token, Access_token_secret)

#Gets current date and time information
now = datetime.datetime.now()
day_of_week = now.strftime("%A")
day = int(now.strftime("%d"))

#Checks if the day of the week is Tuesday, tweets image if true
if day_of_week == "Tuesday":
    image = open('tuesdayrip.jpeg', 'rb')
    response = TuesdayBot.upload_media(media = image)
    TuesdayBot.update_status(status = 'when you look at the calendar and its only tuesday', media_ids = [response['media_id']])