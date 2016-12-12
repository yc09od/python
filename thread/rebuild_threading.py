import threading
import thread
import random
import time

class print_id(threading.Thread) :
	def __init__ (self,id) :
		threading.Thread.__init__(self)
		self.id = id
		self.thread_stop = False
	
	def run (self) :
		for i in range(10) :
			
			print "thread id = " + str(self.id) + " is at " + str(i)
			time.sleep(random.randint(0,10))
	def stop (self) :
		self.thread_stop = True

def main() :
	for i in range(0,3) :
		thread = print_id(i)	
		thread.start()
		
		
if __name__ == '__main__' :
	main()
