import requests, os, time

token = os.getenv('Github_token')
headers = {'Authorization': f'token {token}'}
username = ""

tmpFollowers = 200000
rangeFollowers = 200000
users_url = f"https://api.github.com/search/users"

# Search will only return repos with issue enabled
repos_url = "https://api.github.com/search/repositories"
crawledUrls = {}
stop = False

def politeness(response):
    #print(response.headers["X-RateLimit-Remaining"])
    if response.headers["X-RateLimit-Remaining"] == '0':
        resetTime = int(response.headers["X-RateLimit-Reset"])
        print(time.time())
        print(resetTime)
        while time.time() <= resetTime:
            pass

# Crawled Urls are stored in (key, value) pair of (url, last update time)
while not stop:
    rangeFollowers = tmpFollowers
    for i in range(10):
        users_params={"sort":"followers", "q":f"followers:0..{rangeFollowers}", "page":i+1, "per_page":100}
        usersRes = requests.get(users_url, headers=headers, params=users_params)
        politeness(usersRes)
        if len(usersRes.json()['items']) == 0:
            stop = True        
        for j in range(len(usersRes.json()['items'])):
            username = usersRes.json()['items'][j]["login"]
            crawledUrls[usersRes.json()['items'][j]["html_url"]] = time.time()
            print(usersRes.json()['items'][j]["html_url"])
            # crawl the first 1000 (at most) repos of a user, sorting by number of stars
            for k in range(10):
                repos_params={"sort":"stars", "q":f"user:{username}", "page":k+1, "per_page":100}
                reposRes = requests.get(repos_url, headers=headers, params=repos_params)
                politeness(reposRes)
                if len(reposRes.json()['items']) == 0:
                    break
                for l in range(len(reposRes.json()['items'])):
                    crawledUrls[reposRes.json()['items'][l]["html_url"]] = time.time()
                    #print(reposRes.json()['items'][l]["html_url"])
            # record the num of followers of last user in the batch
            if j == len(usersRes.json()['items']) - 1:
                user_url = f"https://api.github.com/users/{username}"
                userRes = requests.get(user_url, headers=headers)
                politeness(userRes)
                tmpFollowers = userRes.json()["followers"]

