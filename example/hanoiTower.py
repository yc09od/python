import sys
sys.setrecursionlimit(10000)

def oneP(n,size) : 
	list1 = [' ' for x in range(0,size - n)] + ['-' for x in range(0,n)]
	list2 =  list1[:]
	list2.reverse()
	list1.append("|")
	return list1 + list2

def lTos(array) : 
	result = ""
	for i in array : 
		result += i
	return result

def oneL(l,c,r,size) :
	return oneP(l,size) + oneP(c,size) + oneP(r,size)

def printAll(_l,_c,_r,size) :
	result = "";
	l,c,r = _l[:] , _c[:] , _r[:]
	#l.reverse(),c.reverse(),r.reverse()
	l += [0 for x in range(0,size - len(l))]	
	c += [0 for x in range(0,size - len(c))]	
	r += [0 for x in range(0,size - len(r))]	
	for i in range(size-1,-1,-1) : 
		result = result + lTos(oneL(l[i],c[i],r[i],size)) + '\n'
	return result

def move(f,t,l,c,r) :
	mf = ""
	mt = ""
	if f == "L" :
		mf = l
	elif f == "C" :
		mf = c
	else :
		mf = r
	if t == "L" :
		mt = l
	elif t == "C" :
		mt = c
	else :
		mt = r
	mt.append(mf[len(mf)-1])
	mf.pop()

def hanluoT(n,l,c,r,_l,_c,_r,size) : 
	if n == 1 :
		print "move " + str(n) + " From " + l + " to " + r
		move(l,r,_l,_c,_r)
		print printAll(_l,_c,_r,size)
	else :
		hanluoT(n-1,l,r,c,_l,_c,_r,size)
		print "move " + str(n) + " From " + l + " to " + r
		move(l,r,_l,_c,_r)
		print printAll(_l,_c,_r,size)
		hanluoT(n-1,c,l,r,_l,_c,_r,size)
		
size = raw_input("how many size tower you want?")
size = int(size)

l = [x for x in range(size,0,-1)]
c = []
r = []

hanluoT(len(l),"L","C","R",l,c,r,len(l))


		

