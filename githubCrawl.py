import requests, os, time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class githubCrawler:
    def __init__(self, counter = None, crawledUrls = None):
        self.token = os.getenv('Github_token') # you need to set your env var
        self.headers = {'Authorization': f'token {self.token}'}        
        self.usersUrl = "https://api.github.com/search/users"
        self.repos_url = "https://api.github.com/search/repositories"
        self.crawledUrls = {} if crawledUrls == None else crawledUrls
        self.counter = counter        

    def politeness(self, response):
        # check rate limit of api
        if response.headers["X-RateLimit-Remaining"] == '0':
            resetTime = int(response.headers["X-RateLimit-Reset"])
            while time.time() <= resetTime:
                pass

    def crawl(self):
        logging.info("[START CRAWL] (github)")
        tmpFollowers = 200000
        rangeFollowers = 200000 # cap maximum followers in Github
        stop = False
        # Crawled Urls are stored in (key, value) pair of (url, last update time)
        while not stop:
            rangeFollowers = tmpFollowers # adjust range in search for the next 1000 results
            for i in range(10): # since github api only allow 1000 output per search, we need to page through 10 times
                users_params={"sort":"followers", "q":f"followers:0..{rangeFollowers}", "page":i+1, "per_page":100}
                usersRes = requests.get(self.usersUrl, headers=self.headers, params=users_params)
                self.politeness(usersRes)
                if len(usersRes.json()['items']) == 0:
                    # no more users left uncrawled in github
                    stop = True        
                for j in range(len(usersRes.json()['items'])): # for each user
                    username = usersRes.json()['items'][j]["login"]
                    self.crawledUrls[usersRes.json()['items'][j]["html_url"]] = time.time()
                    print(usersRes.json()['items'][j]["html_url"])
                    # crawl the first 1000 (at most) repos of a user, sorting by number of stars
                    for k in range(10):
                        repos_params={"sort":"stars", "q":f"user:{username}", "page":k+1, "per_page":100}
                        reposRes = requests.get(self.repos_url, headers=self.headers, params=repos_params)
                        self.politeness(reposRes)
                        if len(reposRes.json()['items']) == 0:
                            break
                        for l in range(len(reposRes.json()['items'])):
                            self.crawledUrls[reposRes.json()['items'][l]["html_url"]] = time.time()
                            if self.counter != None and len(self.crawledUrls.keys()) >= self.counter:
                                return
                    # record the num of followers of last user in the batch, used in query ajustment
                    if j == len(usersRes.json()['items']) - 1:
                        userUrl = f"https://api.github.com/users/{username}"
                        userRes = requests.get(userUrl, headers=self.headers)
                        self.politeness(userRes)
                        tmpFollowers = userRes.json()["followers"]

if __name__ == "__main__":
    a = githubCrawler(30)
    a.crawl()
    print("crawledUrsl:", len(a.crawledUrls))
