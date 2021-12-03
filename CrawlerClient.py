from SissiCrawler import SissiCrawler
#import JessePriorityQueue
import multiprocessing as mp

class CrawlerClient():

    def __init__(self): pass

    def startCrawl(self, seed):
        # parallel via processes
        # initial crawl from seed using sissicrawler -> non-blocking
        crawler = SissiCrawler(website="", seeds = [], thread = None, counter = None, crawledUrls = None, badUrls = None)

        # start a new SissiCrawler for our initial crawl
        crawler.crawl()

        JessePriorityQueue recrawl = None
        while(True):
            recrawl = self.getPriority()

            # via multiprocessing Pool, we can create x amount of crawling processes for each recrawl URL

            # collect finished crawls with blocking join maybe



    def getPriority(self): 
        # get jesse priority queue
        # maybe through provided helper method, get URLs from priority queue that are due for a recrawl
        # return as list of these URLS
        return recrawl_list
