import requests, time, string, pickle, os, random
from bs4 import BeautifulSoup

def politeness(response):
    #Refresh token if expired
    if r.status_code != 200:
        token = oAuth2()
        headers = {"Authorization": token, "User-Agent": "APP-NAME by REDDIT-USERNAME"}        
    if int(float(response.headers["X-RateLimit-Remaining"])) == 0:
        resetTime = int(response.headers["X-RateLimit-Reset"])
        time.sleep(int(resetTime))

# OAuth2 process
def oAuth2():
    base_url = 'https://www.reddit.com/'
    data = {'grant_type': 'password', 'username': credential["username"], 'password': credential["password"]}
    auth = requests.auth.HTTPBasicAuth(credential["appID"], credential["secret"])
    r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},auth=auth)
    return r.json()["token_type"] + " " + r.json()["access_token"]

def getCommunities():
    communities = []
    alphabets = list(string.ascii_lowercase) + ["0"]
    for i in alphabets:
        r = requests.get(f"https://www.reddit.com/subreddits/{i}-1/")
        soup = BeautifulSoup(r.text, 'html.parser')
        commLinks = soup.find_all('a', {"class": "community-link"})
        for j in commLinks:
            communities.append(j.text)
    return communities

#Get all reddit api credentials
with open(r"redditCredential.pickle", "rb") as input_file:
    credential = pickle.load(input_file)

#Get all communities on Reddit
if os.path.exists(r"communities.pickle"):
    with open(r"communities.pickle", "rb") as input_file:
        communities = pickle.load(input_file)
else:
    communities = getCommunities()
    with open(r"communities.pickle", "wb") as output_file:
        pickle.dump(communities, output_file)


#response.status_code
token = oAuth2()
headers = {"Authorization": token, "User-Agent": "APP-NAME by REDDIT-USERNAME"}
base_url = "https://oauth.reddit.com"

bookmark = {}
crawledUrls = {}
random.seed(time.time())
numCommunities = len(communities)
params = {"limit": 100}
print("start")
count = 0

while len(communities) != 0:
    community = communities[random.randint(0, len(communities) - 1)]
    if community in bookmark.keys():
        params["after"] = bookmark[community]
    else:
        params = {"limit": 100}
    r = requests.get(base_url + f"/r/{community}/new", headers=headers, params=params)
    politeness(r)
    if r.json()["data"]["dist"] == 0:
        indexCommunity = communities.index(community)
        communities.remove(indexCommunity)
    for i in range(r.json()["data"]["dist"]):
        name = r.json()["data"]["children"][i]["data"]["name"].split("_")[1]
        title = r.json()["data"]["children"][i]["data"]["title"]
        url = f"https://www.reddit.com/r/{community}/comments/{name}/{title}/"
        #print(url)
        crawledUrls[url] = time.time()
        bookmark[community] = r.json()["data"]["after"]
    count += 1
    if count == 4:
        break