import threading
import time
import random

ticketList = []
ticketLock = threading.RLock()
End = False

def makeOneTicket () :
	result = ""
	for i in range(0,10) : 
		result += str(random.randint(0,9))	
	return result


def makeTicket() :
	size = random.randint(1,4)
	for i in range(0,size):
		ticketList.append(makeOneTicket())

def printTicket () :
	print str(ticketList)

def sellTicket (seller) :
	if len(ticketList) > 0 :
		ticket = ticketList.pop()		
		print "Ticket : " + ticket + " is sold by Seller : " + seller
	else :
		pass
		#print  "The ticket pool is empty, Seller : " + seller + " do not get ticket"

def ticketProducter (name) :
	counter = 6
	key = True
	while key :
		#get lock
		ticketLock.acquire()
		if len(ticketList) < 10 :
			print "Producter " + name + " start make ticket"
			makeTicket()
			print "Purduction done "
			printTicket()
			counter -= 1
		else :
			print "Pool is full producter get reset"
		print "counter = " + str(counter)
		if counter == 0 :
			global End
			key = False
			End = True
		
		ticketLock.release()
		#relase lock
		time.sleep(random.randint(1,5))
	print "Producter : " + name + " exist"
		

def ticketSeller (name) :
	key = True
	while key :
		#get lock
		ticketLock.acquire()
		sellTicket(name)
		key = not End or len(ticketList) > 0
		ticketLock.release()
		#relase lock
		time.sleep(random.randint(3,10))
	print "seller : " + name + " done"
		
	

def main () :
	producter = threading.Thread(target=ticketProducter,args=('Yang',))
	seller = []
	seller.append(threading.Thread(target=ticketSeller,args=('horst',)))
	seller.append(threading.Thread(target=ticketSeller,args=('Annie',)))
	seller.append(threading.Thread(target=ticketSeller,args=('Tom',)))
	producter.start()
	seller[0].start()
	seller[1].start()
	seller[2].start()


if __name__ == '__main__' :
	main()
	
