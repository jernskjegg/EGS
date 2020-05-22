import requests
import json
import urllib

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=NO&allowCountries=NO"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

def extract_values(obj, key):
    #Function ̶b̶l̶a̶t̶a̶n̶t̶l̶y̶ ̶s̶t̶o̶l̶e̶n̶ borrowed from Todd Birchard https://gist.github.com/toddbirchard/b6f86f03f6cf4fc9492ad4349ee7ff8b
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

games = extract_values(data, "title")
images = extract_values(data, "url")
images = images[2:4]
  
finalDict = dict(zip(games, images))
for key in list(finalDict.keys()):
    if key == "Mystery Game":
        finalDict.pop(key)
        
finalStr = str(finalDict)
finalStr = finalStr.replace("'", "").replace('"', '')

webhookUrl = "yourWebhookURLHere"
slackNotif = {"text": pfinalStr.strip("{}")}

response = requests.post(webhookUrl, data=json.dumps(slackNotif))
error = ("Request returned error code {}, the response is: {}").format(response.status_code, response.text)
if response.status_code != 200:
    raise ValueError(error)