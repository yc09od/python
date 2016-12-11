import thread
import threading
import time
import random

def myTime(id) :
	for i in range(0,10) :
		print 'Thread-' + str(id) + " is now in " + str(i) + '\n'
		time.sleep(random.randint(1,10))

def main() :
	for i in range(3) :
		t = threading.Thread(target=myTime,args=(i,))
		t.start()

if __name__ == '__main__' : 
	main()
