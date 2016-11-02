import time
import threading
import thread

exitFlag = 0
t = 1
exit1 = False
exit2 = False

class myThread1(threading.Thread) : 
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		addTime()
		
class myThread2(threading.Thread) : 
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		showTime()

def addTime() :
	while 1:
		global exit1
		global t
		if exit1 :
			thread.exit()
		time.sleep(1)
		t = time.ctime(time.time())
		
		
def showTime () :
	while 1 :
		global exit1
		global t
		i = int(raw_input("number\n"))
		if i == 0:
			exit1 = True
			thread.exit()
		print "time is " + t
			
	

t1 = myThread1()
t2 = myThread2()

t1.start()
t2.start()

print "exiting main"
