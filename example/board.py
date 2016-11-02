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


#for z in range(0,3):
#	myscreen.clear()
#	myscreen.border(0)
#	for i in range(1+z,10+z):
#		for j in range(1+z,10+z):
#			myscreen.addstr(i,j,str(i-z))
#	time.sleep(1)	
#	myscreen.refresh()
	
	

#myscreen.getch()

#curses.endwin()

total = []

for i in range(0,10) :
	total.append((getNum(),getNum()))

while 1 :
	myscreen.clear()
	myscreen.border(0)
	total_ = []

	for i in total :
		myscreen.addstr(i[0],i[1],'*')
		total_.append((getNext(i[0]),getNext(i[1])))

	total = total_
	myscreen.refresh()
	time.sleep(1)
	


myscreen.getch()

curses.endwin()
