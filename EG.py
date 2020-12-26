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
try:
    check4 = data["data"]["Catalog"]["searchStore"]["elements"][4]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0].get("endDate")
except IndexError:
    print("Game5's vaulted, no date assigned. Giving check4 an empty value")
    check4 = []
try:
    check5 = data["data"]["Catalog"]["searchStore"]["elements"][5]["promotions"]["promotionalOffers"][0]["promotionalOffers"][0].get("endDate")
except IndexError:
    print("Game6's vaulted, no date assigned. Giving check5 an empty value")
    check5 = []

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
    Bool4 = FixTime(timeNowForm, check4)
except IndexError:
    print("Ignoring vaulted game")
try:
    Bool5 = FixTime(timeNowForm, check5)
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
        print("Game #1 has been vaulted.")
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
        print("Game #2 has been vaulted.")
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
        print("Game #3 has been vaulted.")  
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
        print("Game #4 has been vaulted.")
except NameError:
    game3 = ""
    image3 = ""
    pass
try:
    if not Bool4 == True:
        try:
            game4 = data["data"]["Catalog"]["searchStore"]["elements"][4].get("title")
            image4 = data["data"]["Catalog"]["searchStore"]["elements"][4].get("keyImages")
            image4 = image4[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game #5 has been vaulted.")
except NameError:
    game4 = ""
    image4 = ""
    pass
try:
    if not Bool5 == True:
        try:
            game5 = data["data"]["Catalog"]["searchStore"]["elements"][5].get("title")
            image5 = data["data"]["Catalog"]["searchStore"]["elements"][5].get("keyImages")
            image5 = image5[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game #6 has been vaulted.")
except NameError:
    game5 = ""
    image5 = ""
    pass
try:
    if not Bool6 == True:
        try:
            game6 = data["data"]["Catalog"]["searchStore"]["elements"][6].get("title")
            image6 = data["data"]["Catalog"]["searchStore"]["elements"][6].get("keyImages")
            image6 = image6[1].get("url")
        except IndexError:
            print("You stare too deep into the void. The void stares back.")
    else:
        print("Game #7 has been vaulted.")
except NameError:
    game6 = ""
    image6 = ""
    pass
allImages = [image, image1, image2, image3, image4, image5, image6]
allGames = [game, game1, game2, game3, game4, game5, game6]

finalDict = dict(zip(allGames, allImages))
for key in list(finalDict.keys()):
    if key == "Mystery Game":
        finalDict.pop(key)
    elif key == "":
        finalDict.pop(key)

       
finalStr = str(finalDict)
#finalStr2 = finalStr.replace(":", "").replace('"', '')

webhookUrl = "yourWebhookURLHere"
slackNotif = {"text": finalStr.strip("{}")}

response = requests.post(webhookUrl, data=json.dumps(slackNotif))
error = ("Request returned error code {}, the response is: {}").format(response.status_code, response.text)
if response.status_code != 200:
    raise ValueError(error)
