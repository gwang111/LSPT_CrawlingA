from bfsCrawl import bfsCrawler
from githubCrawl import githubCrawler
from redditCrawl import redditCrawler
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

class SissiCrawler:
    def __init__(self, website, seeds = None, thread = None, counter = None, crawledUrls = None, badUrls = None):
        self.website = website # rpi, wiki, github, reddit
        self.seeds = seeds
        self.thread = thread
        self.counter = counter
        self.crawledUrls = {} if crawledUrls == None else crawledUrls
        self.badUrls = set() if badUrls == None else badUrls
        self.crawler = self.pickCrawler()

    def pickCrawler(self):
        if self.website == "rpi":
            if str(type(self.seeds)) != "<class 'list'>":
                print("must provide a list of seed url for rpi crawler")
                return None
            logging.info("[INIT SISSICRAWLER] website: %s, seeds: %s, counter: %d, crawledURLs: %s, badURLs: %s", self.website, self.seeds, self.counter, self.crawledUrls, self.badUrls)
            return bfsCrawler("rpi", self.seeds, self.counter, self.crawledUrls, self.badUrls)
        elif self.website == "wiki":
            if str(type(self.seeds)) != "<class 'list'>":
                print("must provide a list of seed url for wiki crawler")
                return None
            logging.info("[INIT SISSICRAWLER] website: %s, seeds: %s, counter: %d, crawledURLs: %s, badURLs: %s", self.website, self.seeds, self.counter, self.crawledUrls, self.badUrls)
            return bfsCrawler("wiki", self.seeds, self.counter, self.crawledUrls, self.badUrls)
        elif self.website == "github":
            logging.info("[INIT SISSICRAWLER] website: %s, counter: %d, crawledURLs: %s", self.website, self.counter, self.crawledUrls)
            return githubCrawler(self.counter, self.crawledUrls)
        elif self.website == "reddit":
            logging.info("[INIT SISSICRAWLER] website: %s, thread: %d, counter: %d, crawledURLs: %s", self.website, self.thread, self.counter, self.crawledUrls)
            return redditCrawler(self.thread, self.counter, self.crawledUrls)
        elif self.website == "test":
            logging.info("[INIT SISSICRAWLER] website: %s, seeds: %s, counter: %d, crawledURLs: %s, badURLs: %s", self.website, self.seeds, self.counter, self.crawledUrls, self.badUrls)
            return bfsCrawler("test", self.seeds, self.counter, self.crawledUrls, self.badUrls)
        else:
            logging.info("[ERROR] Website not supported")
            print("website not supported!")
            return None

    def crawl(self):
        if self.crawler == None:
            print("please reconfigure crawler setting!")
            return
        self.crawler.crawl()

if __name__ == "__main__":
    rpiSeeds = ['https://rpi.edu', 'https://cipce.rpi.edu/index.html']
    wikiSeeds = ['https://en.wikipedia.org/wiki/Tiger', 'https://zh.wikipedia.org/wiki/%E8%99%8E']
    rpiSeed = ['https://rpi.edu']
    wikiSeed = ['https://en.wikipedia.org/wiki/Tiger']
    testSeed = ['http://localhost/ITWS-Cooking-Site/']
    # you can pass in {} or set() to the crawler creator if you want to set crawledUrls / badUrls to be global var
    a = SissiCrawler("rpi", testSeed, None, 30, None, None) # rpi crawler
    #a = SissiCrawler("rpi", rpiSeeds, None, 30, None, None) # rpi crawler, threaded
    #a = SissiCrawler("wiki", wikiSeed, None, 30, None, None) # wiki crawler
    #a = SissiCrawler("wiki", wikiSeeds, None, 30, None, None) # wiki crawler threaded
    #a = SissiCrawler("github", None, None, 30, None, None) # github crawler
    #a = SissiCrawler("reddit", None, None, 30, None, None) # reddit crawler
    #a = SissiCrawler("reddit", None, 2, 30, None, None) # reddit crawler, threaded
    a.crawl()
    print("crawledUrsl:", len(a.crawledUrls))
    print("badUrls:", len(a.badUrls))
