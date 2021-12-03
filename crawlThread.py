import threading
import time

exitFlag = 0

class crawlThread (threading.Thread):
   def __init__(self, threadID, name, counter, function):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.function = function
      
   def run(self):
      print("Starting " + self.name)
      self.function(self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def hello(name):
   print(name)

# Create new threads
thread1 = crawlThread(1, "Thread-1", 1, hello)
thread2 = crawlThread(2, "Thread-2", 2, hello)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")