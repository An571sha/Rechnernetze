# making a version of a threshold sloppy counter made in C in python
# inorder to understand multithreading better in python

from threading import Thread, Lock


NUMCPUS = 5
ITERATIONS = 1000
THRESHOLD = 1024

globalLock = lock()
cpuLock0 = Lock()
cpuLock1 = Lock()
cpuLock2 = Lock()
cpuLock3 = Lock()
cpuLock4 = Lock()


class Counter_t (object):
	def _init_(self, glbl, thrshld):
		self.global = glbl 
		self.local = [None] * n
		self.threshold = thrshld


class Cthread (object):
	def _init_(self, thrdId, counter_t, amt):
		self.counter_t = counter_t
		self.threadId = thrdId
		self.amt = amt

class Updater(Thread):
	def _init_(self, Counter_t, Cthread):
		thread._init_(self)
		self.counter_t = Counter_t
		self.cthread = Cthread

	def run(self):
		# write a func  to increment local counter and global counter if all local counters have been incremented
	
