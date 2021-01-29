import requests
import json
import urllib

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=NO&allowCountries=NO"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
games=[]
images=[]
for i in range(0,25):
    try:
        games.append(data["data"]["Catalog"]["searchStore"]["elements"][i].get("title"))
        images.append(data["data"]["Catalog"]["searchStore"]["elements"][i].get("keyImages")[1].get("url"))
    except (IndexError, TypeError):
        pass

finalDict = dict(zip(games, images))
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
