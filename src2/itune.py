import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# prints out the json for one search result
res = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(res.json(), indent=2))

# prints out the track names of fice search results 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])