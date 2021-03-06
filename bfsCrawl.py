import requests, re, time, urllib.robotparser, threading
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class urlFetcher:
    def __init__(self, crawledUrls, badUrls):
        self.rpiRobot = urllib.robotparser.RobotFileParser()
        self.wikiRobot = urllib.robotparser.RobotFileParser()
        self.politeness(self.rpiRobot, "http://rpi.edu/robots.txt")
        self.politeness(self.wikiRobot, "https://en.wikipedia.org/robots.txt")
        self.crawledUrls = crawledUrls
        self.badUrls = badUrls

    def politeness(self, robot, robotsUrl):
        robot.set_url(robotsUrl)
        robot.read()

    def getUrls(self, url, robot, processUrl):
        urlsFound = set()
        try:
            if robot and not robot.can_fetch("*", url):
                # url in robots.txt
                logging.info("[URL IGNORED, IN ROBOTS.TXT] URL: %s", url)
                return urlsFound
            r = requests.get(url)
            self.crawledUrls[url] = time.time()
            print(len(self.crawledUrls.keys()))
            if r.status_code == 404:
                logging.info("[BAD URL: 404] URL: %s", url)
                self.crawledUrls.pop(url)
                self.badUrls.add(url)
                return urlsFound
            soup = BeautifulSoup(r.text, 'html.parser')
            for link in soup.find_all('a'):
                path = link.get('href')
                if (path is not None):
                    path = processUrl(url, path)
                    if path == "":
                        logging.info("[LINK NOT IN DOMAIN]\n%sFROM: %s\n%sTO: %s", str().rjust(26), url, str().rjust(26), urljoin(url, path))
                        # url not within domain
                        continue
                    if (robot is None or robot.can_fetch("*", path) and path not in self.badUrls):
                        urlsFound.add(path)
        except requests.exceptions.RequestException as err:
            print(url)
            self.badUrls.add(url)
            print (time.time(), "OOps: Something Else",err)
        except requests.exceptions.HTTPError as errh:
            print(url)
            self.badUrls.add(url)
            print (time.time(), "Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print(url)
            self.badUrls.add(url)
            print (time.time(), "Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print(url)
            self.badUrls.add(url)
            print (time.time(), "Timeout Error:",errt)
        return urlsFound

    def getRPIUrls(self, url):
        return self.getUrls(url, self.rpiRobot, self.processRPIUrls)

    def getWikiUrls(self, url):
        return self.getUrls(url, self.wikiRobot, self.processWikiUrls)
    
    def getTestUrls(self, url):
        return self.getUrls(url, None, self.processTestUrls)

    def processRPIUrls(self, url, path):
        if 'rpi' not in path:
            # url not in rpi domain
            return ""
        elif path.startswith('/'):
            # url is not complete
            index = url.rfind('/')
            path = url[0:index] + path
        elif not path.startswith('https:') and not path.startswith('http:'):
            # url is not complete
            index = url.rfind('/')
            path = url[0:index] + '/' + path     
        elif re.match('^https://www.+\.rpi\.edu/.+', path):
            # url should not have www, will trigger error
            tmp = path.split('www.')
            path = tmp[0] + tmp[1]
        elif re.match('^https://.+\.rpi\.edu/.+', path) is None:
            # url not in rpi domain
            return ""
        return path

    def processWikiUrls(self, url, path):
        if 'wiki' not in path:
            # url not in wiki domain
            return ""            
        elif path.startswith('//'):
            # switch of language
            if re.match('^//[a-z]+\.wikipedia\.org.+', path) is None:
                # url not in desired wiki domain
                return ""
            else:
                path = urljoin('https://en.wikipedia.org', path)
        elif path.startswith('/'):
            # stay within language
            path = urljoin('https://en.wikipedia.org', path)
        elif re.match('^https://[a-z]+\.wikipedia\.org.+', path) is None:
            # url not in desired wiki domain
            return ""
        return path
    
    def processTestUrls(self, url, path, root = "http://localhost/ITWS-Cooking-Site/"):
        joined_url = urljoin(url, path)
        if root not in joined_url:
            joined_url = ""
        return joined_url

class crawlThread (threading.Thread):
    def __init__(self, threadID, bfs, seedUrl, urlFetcher, counter = None):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.seedUrl = seedUrl
        self.urlFetcher = urlFetcher
        self.counter = counter
        self.bfs = bfs

    def run(self):
        print("Starting " + self.name)
        self.bfs(self.seedUrl, self.urlFetcher, self.counter)
        print("Exiting " + self.name)

class bfsCrawler:
    def __init__(self, website, seeds, counter = None, crawledUrls = None, badUrls = None):
        self.website = website # "wiki" or "rpi"
        self.seeds = seeds
        self.counter = counter
        self.crawledUrls = {} if crawledUrls == None else crawledUrls
        self.badUrls = set() if badUrls == None else badUrls
        self.visitedUrls = set()
        self.urlFetcher = urlFetcher(self.crawledUrls, self.badUrls)

    def crawl(self):
        if len(self.seeds) == 1:
            logging.info("[START CRAWL] Seed URL: %s", self.seeds[0])
            self.BFS(self.seeds[0], self.website, self.counter)
        else:
            logging.info("[START CRAWL THREADS] >1 URL")
            threads = []
            for threadID, url in enumerate(self.seeds):
                logging.info("[START CRAWL THREAD] ID: %d URL: %s", threadID, url)
                thread = crawlThread(threadID, self.BFS, url, self.website, self.counter)
                thread.start()
                threads.append(thread)
            for t in threads:
                logging.info("[JOIN CRAWL THREAD]")
                t.join()

    def BFS(self, seed, urlFilter = "wiki", counter = None):
        # Mark the source node as
        # visited and enqueue it
        urlqueue = []
        urlqueue.append(seed)
        self.visitedUrls.add(seed)
        if urlFilter == "rpi":
            getUrls = self.urlFetcher.getRPIUrls
        elif urlFilter == "wiki":
            getUrls = self.urlFetcher.getWikiUrls
        elif urlFilter == "test":
            getUrls = self.urlFetcher.getTestUrls
        else:
            print("website not supported!")
            return
    
        while urlqueue:
            logging.info("[CRAWLER COUNTER]: %d", counter)
            if counter == 0:
                return            
            if counter != None:
                counter -= 1
            
            # Dequeue a vertex from
            # queue and print it
            url = urlqueue.pop(0)
            logging.info("[CRAWLER VISITED URL] URL: %s", url)
            
            # This is where we would send data to link analysis, document data store, etc.
            # Also where we would send the url to JessePriorityQueue for recrawling
    
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            nextUrls = getUrls(url)
            for nextUrl in nextUrls:
                if nextUrl not in self.visitedUrls:
                    logging.info("[LINK FOUND AND ADDED]\n%sFROM: %s\n%sTO: %s", str().rjust(26), url, str().rjust(26), nextUrl)
                    urlqueue.append(nextUrl)
                    self.visitedUrls.add(nextUrl)

if __name__ == "__main__":
    rpiSeeds = ['https://rpi.edu', 'https://cipce.rpi.edu/index.html']
    wikiSeeds = ['https://en.wikipedia.org/wiki/Tiger', 'https://zh.wikipedia.org/wiki/%E8%99%8E']
    a = bfsCrawler("rpi", rpiSeeds, 30)
    a.crawl()
    print("crawledUrsl:", len(a.crawledUrls))
    print("badUrls:", len(a.badUrls))
