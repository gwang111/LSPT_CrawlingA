import requests, time, string, pickle, os, random, threading
from bs4 import BeautifulSoup

class crawlThread (threading.Thread):
    def __init__(self, threadID, crawl, counter = None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.counter = counter
        self.crawl = crawl

    def run(self):
        print("Starting " + self.name)
        self.crawl(self.counter)
        print("Exiting " + self.name)

class redditCrawler:
    def __init__(self, thread = None, counter = None, crawledUrls = None):
        self.credential = {}
        self.getCredentials()
        self.token = self.oAuth2()
        self.headers = {"Authorization": self.token, "User-Agent": "APP-NAME by REDDIT-USERNAME"}        
        self.base_url = "https://oauth.reddit.com"
        self.bookmark = {}
        self.crawledUrls = {} if crawledUrls == None else crawledUrls
        self.communities = []
        self.loadCommunities()
        self.counter = counter
        self.thread = thread
        random.seed(time.time())

    def getCredentials(self):
        #Get all reddit api credentials, make sure "redditCredential.pickle" exists
        with open(r"redditCredential.pickle", "rb") as input_file:
            self.credential = pickle.load(input_file)

    # OAuth2 process
    def oAuth2(self):
        base_url = 'https://www.reddit.com/'
        data = {'grant_type': 'password', 'username': self.credential["username"], 'password': self.credential["password"]}
        auth = requests.auth.HTTPBasicAuth(self.credential["appID"], self.credential["secret"])
        r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': 'APP-NAME by REDDIT-USERNAME'},auth=auth)
        return r.json()["token_type"] + " " + r.json()["access_token"]

    def politeness(self, response):
        #Refresh token if expired
        if response.status_code != 200:
            self.token = self.oAuth2()
            self.headers = {"Authorization": self.token, "User-Agent": "APP-NAME by REDDIT-USERNAME"}        
        if int(float(response.headers["X-RateLimit-Remaining"])) == 0:
            resetTime = int(response.headers["X-RateLimit-Reset"])
            time.sleep(int(resetTime))

    def getCommunities(self):
        alphabets = list(string.ascii_lowercase) + ["0"]
        for i in alphabets:
            r = requests.get(f"https://www.reddit.com/subreddits/{i}-1/")
            soup = BeautifulSoup(r.text, 'html.parser')
            commLinks = soup.find_all('a', {"class": "community-link"})
            for j in commLinks:
                self.communities.append(j.text)

    def loadCommunities(self):
        # Get all communities on Reddit
        if os.path.exists(r"communities.pickle"): # if cached, use cache
            with open(r"communities.pickle", "rb") as input_file:
                self.communities = pickle.load(input_file)
        else: # if not, search and create cache
            self.getCommunities()
            with open(r"communities.pickle", "wb") as output_file:
                pickle.dump(self.communities, output_file)

    def crawl(self):
        if self.thread == None:
            self.crawlSingle(self.counter)
        else:
            threads = []
            for i in range(self.thread):
                thread = crawlThread(1, self.crawlSingle, self.counter)
                thread.start()
                threads.append(thread)
            for t in threads:
                t.join()

    def crawlSingle(self, counter = None):
        params = {"limit": 100}
        while len(self.communities) != 0:
            # randomly pick a community to crawl from
            community = self.communities[random.randint(0, len(self.communities) - 1)]
            if community in self.bookmark.keys():
                params["after"] = self.bookmark[community]
            else:
                params = {"limit": 100}
            r = requests.get(self.base_url + f"/r/{community}/new", headers=self.headers, params=params)
            self.politeness(r)
            if r.json()["data"]["dist"] == 0:
                # finished crawling a community
                indexCommunity = self.communities.index(community)
                self.communities.remove(indexCommunity)
            for i in range(r.json()["data"]["dist"]): # for each subreddit
                name = r.json()["data"]["children"][i]["data"]["name"].split("_")[1]
                title = r.json()["data"]["children"][i]["data"]["title"]
                url = f"https://www.reddit.com/r/{community}/comments/{name}/{title}/"
                print(url)
                if counter != None and len(self.crawledUrls.keys()) >= counter:
                    return                
                self.crawledUrls[url] = time.time()
                self.bookmark[community] = r.json()["data"]["after"] # record where to start next time

if __name__ == "__main__":
    a = redditCrawler(2, 500)
    a.crawl()
    print("crawledUrsl:", len(a.crawledUrls))
