import thread 
import time

#defining a function for thread

def print_time(threadName, delay):
	count = 0
	while count<5:
		time.sleep(delay)
		count+=1
		print "%s: %s" %( threadName, time.ctime(time.time()))

#creating two threads

try:
	thread.start_new_thread(print_time,("thread-1",2,))
	thread.start_new_thread(print_time,("thread-2",4,))
except:
	print "error: ,something went wrong while creating a new thread"

while 1:
	pass

 
