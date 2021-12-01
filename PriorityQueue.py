from math import exp, tanh
from random import random
import datetime
import heapq

class PriorityItem:
	def __init__(self, URL, lam, alpha, crawl_time):
		self.URL = URL
		self.lam = lam
		self.alpha = alpha
		self.crawl_time = crawl_time
		self.calculatePriority()

	def calculatePriority(self):
		self.priority = self.crawl_time + datetime.timedelta(days=self.lam)

	def update(self, current_time, updated_time, bounds=[0.9, 1.1], weight=[1, 1]):
		"""
		Update lambda and alpha hyperparameters

		Inputs:
		current_time - current time
		updated_time - last known website update time
		bounds - minimum and maximum values for alpha
		weights - weights to apply to an increase or decrease in lambda, respectively
		
		Side-effects:
		lambda and alpha hyperparameters are tuned

		Notes:
		new lambda = lambda / age()
		new alpha increases if lambda decreases
		new alpha decreases if lambda increases
		"""
		self.crawl_time = current_time
		a = current_time - updated_time
		if a > 0:
			new_lam = self.lam / (1 + a)
		else:
			new_lam = lam / (1 + tanh(a))
		if new_lam > lam:
			new_lam *= weight[0]
		else:
			new_lam *= weight[1]

		new_alpha = max(min(bounds[1], self.alpha * (1 + tanh(1 + a))), bounds[0])
		self.lam = new_lam
		self.alpha = new_alpha

class PriorityQueue:
	def __init__(self, initial=None, key=lambda x:x):
		"""
		Builds the initial priority queue for our crawler.

		Inputs:
		initial - initialize data if we already have data (default None)
		key - comparator operation (default lambda x:x)

		Notes:
		- FOR OUR USE ::: Set key=lambda x:x.priority (x.calculatePriority MUST BE CALLED)
		"""
		self.key = key
		self.index = 0
		if initial:
			self.__data__ = [(key(item), i, item) for i, item in initial]
			self.index = len(self.__data__)
			heapq.heapify(self.__data__)
		else:
			self.__data__ = []

	def push(self, item):
		"""
		Add item to queue

		Inputs:
		item - object to be added to queue

		Side-effects:
		heapq.heappush called to add item to queue
		self.index incremented by 1
		"""
		heapq.heappush(self.__data__(self.key(item), self.index, item))
		self.index += 1

	def pop(self):
		"""
		Get top priority item

		Side-effects:
		- index decremented by 1

		Outputs:
		- item at the top of the queue
		"""
		self.index -= 1
		return heapq.heappop(self.__data__)[-1]
