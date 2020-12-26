import requests
import json
import urllib, time
import datetime as dt
from datetime import date

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=NO&allowCountries=NO"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

try:
    check = data["data"]["Catalog"]["searchStore"]["elements"][0]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0].get("endDate")
except IndexError:
    print("Game1's vaulted, no date assigned. Giving check an empty value")
    check = []
isGameVaulted = check
try:
    check1 = data["data"]["Catalog"]["searchStore"]["elements"][1]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0].get("endDate")
except IndexError:
    print("Game2's vaulted, no date assigned. Giving check1 an empty value")
    check1 = []
isGameVaulted1 = check1
try:
    check2 = data["data"]["Catalog"]["searchStore"]["elements"][2]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0].get("endDate")
except IndexError:
    print("Game3's vaulted, no date assigned. Giving check2 an empty value")
    check2 = []
isGameVaulted2 = check2
try:
    check3 = data["data"]["Catalog"]["searchStore"]["elements"][3]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0].get("endDate")
except IndexError:
    print("Game4's vaulted, no date assigned. Giving check3 an empty value")
    check3 = []
isGameVaulted3 = check3

timeNow = dt.datetime.today()
timeNowForm = str(timeNow.strftime("%Y-%D%H%M%SZ"))


def FixTime(listFixed, listEGS):
    year1 = str(listFixed)[2] + str(listFixed)[3]
    month1 = str(listFixed)[5] + str(listFixed)[6]
    day1 = str(listFixed)[8] + str(listFixed)[9]
    date1 = str(day1+"/"+month1+"/"+year1)
    year2 = str(listEGS[2]) + str(listEGS[3])
    month2 = str(listEGS[5]) + str(listEGS[6])
    day2 = str(listEGS[8]) + str(listEGS[9])
    date2 = str(day2+"/"+month2+"/"+year2)
    if date2 > date1 == False:
        return False
try:
    Bool = FixTime(timeNowForm, check)
except IndexError:
    print("Ignoring vaulted game")
try:
    Bool1 = FixTime(timeNowForm, check1)
except IndexError:
    print("Ignoring vaulted game")
try:
    Bool2 = FixTime(timeNowForm, check2)
except IndexError:
    print("Ignoring vaulted game")
try:
    Bool3 = FixTime(timeNowForm, check3)
except IndexError:
    print("Ignoring vaulted game")

try:
    if not Bool == True:
        try:
            game = data["data"]["Catalog"]["searchStore"]["elements"][0].get("title")
            image = data["data"]["Catalog"]["searchStore"]["elements"][0].get("keyImages")
            image = image[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game1 has been vaulted.")
except NameError:
    game = ""
    image = ""
    pass
try:
    if not Bool1 == True:
        try:
            game1 =  data["data"]["Catalog"]["searchStore"]["elements"][1].get("title")
            image1 = data["data"]["Catalog"]["searchStore"]["elements"][1].get("keyImages")
            image1 = image1[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game2 has been vaulted.")
except NameError:
    game1 = ""
    image1 = ""
    pass
try:
    if not Bool2 == True:
        try:
            game2 = data["data"]["Catalog"]["searchStore"]["elements"][2].get("title")
            image2 = data["data"]["Catalog"]["searchStore"]["elements"][2].get("keyImages")
            image2 = image2[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game3 has been vaulted.")  
except NameError:
    game2 = ""
    image2 = ""
    pass        
try:
    if not Bool3 == True:
        try:
            game3 = data["data"]["Catalog"]["searchStore"]["elements"][3].get("title")
            image3 = data["data"]["Catalog"]["searchStore"]["elements"][3].get("keyImages")
            image3 = image3[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game4 has been vaulted.")
except NameError:
    game3 = ""
    image3 = ""
    pass

allImages = [image, image1, image2, image3]
allGames = [game, game1, game2, game3]

finalDict = dict(zip(allGames, allImages))
for key in list(finalDict.keys()):
    if key == "Mystery Game":
        finalDict.pop(key)
    elif key == "":
        finalDict.pop(key)

       
finalStr = str(finalDict)
#finalStr2 = finalStr.replace(":", "").replace('"', '')

webhookUrl = "yourWebhookUrlHere"
slackNotif = {"text": finalStr.strip("{}")}

response = requests.post(webhookUrl, data=json.dumps(slackNotif))
error = ("Request returned error code {}, the response is: {}").format(response.status_code, response.text)
if response.status_code != 200:
    raise ValueError(error)
