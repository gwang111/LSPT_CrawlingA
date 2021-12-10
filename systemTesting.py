from PriorityQueue import PriorityQueue
from SissiCrawler import SissiCrawler

import unittest

class SystemTestSuite(unittest.TestCase):

    # confirm all links from seed are visited
    def sys_1():
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # handle cycles
    def sys_2(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_3(): pass

    # robot txt
    def sys_4(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_5(): pass

    # TODO prio queue update not fully integrated with actual prio queue
    def sys_6(): pass

    # Handle un-accessible web pages
    def sys_7(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # TODO webpage page count not accounted for yet
    def sys_8(): pass

    # Crawling status during the crawl
    def sys_9():
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_10(): pass

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_11(): pass

    # TODO hyperparameter tuning not fully implemented yet
    def sys_12(): pass

    # Test crawl on different operating systems
    def sys_13(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # Large Webgraph test
    def sys_14():
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # PW protected websites
    def sys_15():
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # Test crawler recovery from errors
    def sys_16():
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_17(): pass

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_18(): pass

    # Wikipedia traversal
    def sys_19():
        seed = []
        a = SissiCrawler("wiki", seed, None, 30, None, None)

    # Reddit Traversal
    def sys_20(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # Github Traversal
    def sys_21(): 
        seed = []
        a = SissiCrawler("github", seed, None, 30, None, None)

    # RPI website traversal
    def sys_22():
        seed = []
        a = SissiCrawler("rpi", seed, None, 30, None, None)

    # TODO have not implemented multi processing yet
    def sys_23(): pass

    # Does not run out of resources when crawling a large webgraph
    def sys_24(): 
        seed = []
        a = SissiCrawler("wiki", seed, None, 30, None, None)

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_25(): pass

    # Crawl on multiple wikipedia webpages -> impartiality
    def sys_26():
        seed = []
        a = SissiCrawler("wiki", seed, None, 30, None, None)

    # Crawling across multiple reddit webpages
    def sys_27():
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # vary selection policy (i.e reddit crawl github crawl etc)
    def sys_28(): 
        seed = []
        a = SissiCrawler("reddit", seed, None, 30, None, None)

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_29(): pass

    # Disconnect from internet and see if we can keep running (infeasible in a test suite tho?)
    def sys_30(): pass

    # TODO skip -> we have not integrated prio queue and crawler together yet
    def sys_31(): pass

    # TODO prio queue not fully implemented for this yet
    def sys_32(): pass
