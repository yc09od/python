import curses,time 
import random

def getNum() : 
	return int(random.random()*20)

def getNext(x):
	r =  int(random.random()*3) - 1 + x 
	if r < 0 :
		return 0
	else :
	        return r


myscreen = curses.initscr()


total = []

for i in range(0,10) :
	total.append((getNum(),getNum()))

try:
     while 1 :
	myscreen.clear()
	myscreen.border(0)
	total_ = []

	for i in total :
		myscreen.addstr(i[0],i[1],'*')
		total_.append((getNext(i[0]),getNext(i[1])))

	total = total_
	time.sleep(0.05)
	myscreen.refresh()
except:
	myscreen.getch()

	
myscreen.clear()
myscreen.getch()
curses.endwin()
