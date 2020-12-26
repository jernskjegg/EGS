import requests
import json
import urllib

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=NO&allowCountries=NO"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

check = data["data"]["Catalog"]["searchStore"]["elements"][0].get("customAttributes")
check1 = data["data"]["Catalog"]["searchStore"]["elements"][1].get("customAttributes")
check2 =  data["data"]["Catalog"]["searchStore"]["elements"][2].get("customAttributes")
check3 =  data["data"]["Catalog"]["searchStore"]["elements"][3].get("customAttributes")
check4 = data["data"]["Catalog"]["searchStore"]["elements"][4].get("customAttributes")
check5 = data["data"]["Catalog"]["searchStore"]["elements"][5].get("customAttributes")
try:
    game = data["data"]["Catalog"]["searchStore"]["elements"][0].get("title")
    image = data["data"]["Catalog"]["searchStore"]["elements"][0].get("keyImages")
    image = image[1].get("url")
except IndexError:
    print("You stare too deep into the void. The void stares back.")
       
try:
    game1 =  data["data"]["Catalog"]["searchStore"]["elements"][1].get("title")
    image1 = data["data"]["Catalog"]["searchStore"]["elements"][1].get("keyImages")
    image1 = image1[1].get("url")
except IndexError:
    print("You stare too deep into the void. The void stares back.")
try:
    game2 = data["data"]["Catalog"]["searchStore"]["elements"][2].get("title")
    image2 = data["data"]["Catalog"]["searchStore"]["elements"][2].get("keyImages")
    image2 = image2[1].get("url")
except IndexError:
    print("You stare too deep into the void. The void stares back.")
try:
    game3 = data["data"]["Catalog"]["searchStore"]["elements"][3].get("title")
    image3 = data["data"]["Catalog"]["searchStore"]["elements"][3].get("keyImages")
    image3 = image3[1].get("url")
except IndexError:
    print("You stare too deep into the void. The void stares back.")
try:
    game4 = data["data"]["Catalog"]["searchStore"]["elements"][4].get("title")
    image4 = data["data"]["Catalog"]["searchStore"]["elements"][4].get("keyImages")
    image4 = image4[1].get("url")
except IndexError:
    print("You stare too deep into the void. The void stares back.")
try:
    game5 = data["data"]["Catalog"]["searchStore"]["elements"][5].get("title")
    image5 = data["data"]["Catalog"]["searchStore"]["elements"][5].get("keyImages")
    image5 = image5[1].get("url")
except IndexError:
    print("You stare too deep into the void. The void stares back.")

allImages = [image, image1, image2, image3, image4, image5]
allGames = [game, game1, game2, game3, game4, game5]

finalDict = dict(zip(allGames, allImages))
for key in list(finalDict.keys()):
    if key == "Mystery Game":
        finalDict.pop(key)
        
finalStr = str(finalDict)
webhookUrl = "yourWebhookURLHere"
slackNotif = {"text": finalStr.strip("{}")}
response = requests.post(webhookUrl, data=json.dumps(slackNotif))
error = ("Request returned error code {}, the response is: {}").format(response.status_code, response.text)
if response.status_code != 200:
    raise ValueError(error)
