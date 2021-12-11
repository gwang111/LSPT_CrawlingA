from PriorityQueue import PriorityQueue
from SissiCrawler import SissiCrawler

import unittest

class SystemTestSuite(unittest.TestCase):

    # confirm all links from seed are visited
    def sys_1():
        seed = ['http://localhost/ITWS-Cooking-Site/']
        a = SissiCrawler("test", seed, None, 30, None, None)
        a.crawl()

    # handle cycles (the website from sys_1 also has cycles)
    def sys_2(): 
        seed = ['http://localhost/ITWS-Cooking-Site/']
        a = SissiCrawler("test", seed, None, 30, None, None)
        a.crawl()

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_3(): pass

    # robot txt hardcoded into reddit crawler
    def sys_4(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)
        a.crawl()

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_5(): pass

    # TODO prio queue update not fully integrated with actual prio queue
    def sys_6(): pass

    # Handle un-accessible web pages
    def sys_7(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)
        a.crawl()

    # webpage page count limiting
    def sys_8():
        seed = ['http://localhost/ITWS-Cooking-Site/']
        a = SissiCrawler("test", seed, None, 2, None, None)
        a.crawl()

    # Crawling status during the crawl (command line logging)
    def sys_9():
        seed = ['http://localhost/ITWS-Cooking-Site/']
        a = SissiCrawler("test", seed, None, 20, None, None)
        a.crawl()

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_10(): pass

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_11(): pass

    # TODO hyperparameter tuning not fully implemented yet
    def sys_12(): pass

    # Test crawl on different operating systems (could also just run test cases on a different OS)
    def sys_13(): 
        seed = ['http://localhost/ITWS-Cooking-Site/']
        a = SissiCrawler("test", seed, None, 20, None, None)
        a.crawl()

    # Large Webgraph test
    def sys_14():
        seed = []
        a = SissiCrawler("wiki", seed, None, 100000, None, None)
        a.crawl()

    # PW protected websites
    def sys_15():
        seed = ['http://localhost/project/auth/login.php']
        a = SissiCrawler("test", seed, None, 20, None, None, seed)
        a.crawl()

    # Test crawler recovery from errors
    # This one just test an incorrect seed, but broken URLs and exceptions that might
    # occur are also handled without stopping the crawler--those URLs are just ignored
    def sys_16():
        seed = ['http://localhst/ng-Site/']
        a = SissiCrawler("test", seed, None, 20, None, None)
        a.crawl()

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_17(): pass

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_18(): pass

    # Wikipedia traversal
    def sys_19():
        seed = ['https://en.wikipedia.org']
        a = SissiCrawler("wiki", seed, None, 30, None, None)
        a.crawl()

    # Reddit Traversal
    def sys_20(): 
        seed = ['https://www.reddit.com/r/RPI/']
        a = SissiCrawler("reddit", seed, None, 30, None, None)
        a.crawl()

    # Github Traversal
    def sys_21(): 
        seed = ['https://github.com/gwang111/LSPT_CrawlingA']
        a = SissiCrawler("github", seed, None, 30, None, None)
        a.crawl()

    # RPI website traversal
    def sys_22():
        seed = ['https://rpi.edu']
        a = SissiCrawler("rpi", seed, None, 30, None, None)
        a.crawl()

    # Test multiple threads
    def sys_23():
        seed = ['http://localhost/ITWS-Cooking-Site/', 'http://localhost/ITWS-Cooking-Site/', 'http://localhost/ITWS-Cooking-Site/']
        a = SissiCrawler("test", seed, None, 20, None, None)
        a.crawl()

    # Does not run out of resources when crawling a large webgraph
    def sys_24(): 
        seed = ['https://en.wikipedia.org']
        a = SissiCrawler("wiki", seed, None, 30000, None, None)
        a.crawl()

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_25(): pass

    # Crawl on multiple wikipedia webpages -> impartiality
    def sys_26():
        seed = ['https://en.wikipedia.org/wiki/Tiger', 'https://zh.wikipedia.org/wiki/%E8%99%8E']
        a = SissiCrawler("wiki", seed, None, 30, None, None)

    # Crawling across multiple reddit webpages
    def sys_27():
        seed = ['https://www.reddit.com/r/RPI/', 'https://www.reddit.com/r/rit/', 'https://www.reddit.com/r/ProgrammerHumor/']
        a = SissiCrawler("reddit", seed, None, 30, None, None)
        a.crawl()

    # TODO skip -> we haven't implemented prio queue/recrawler yet
    # vary selection policy (i.e reddit crawl github crawl etc)
    def sys_28(): pass

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_29(): pass

    # Disconnect from internet and see if we can keep running (infeasible in a test suite tho?)
    def sys_30():
        seed = ['https://en.wikipedia.org']
        a = SissiCrawler("wiki", seed, None, 30000, None, None)
        a.crawl()

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_31(): pass

    # TODO prio queue not fully implemented for this yet
    def sys_32(): pass
