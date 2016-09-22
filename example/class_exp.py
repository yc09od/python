class person :
	name = None
	def __init__(self,name = None ):
		self.name = name

class student(person) :
	level = None
	def __init__(self,level = None) :
		self.level = level

test = student(6)

print "Is it have var name?\t" + str(hasattr(test,'name'))
print "It's name is \t" + str(getattr(test,'name')) 
setattr(test,'name',raw_input())
print "It's new name is " + str(getattr(test,'name')) 
delattr(test,'name')
print "del it's name"
print "It's name is \t" + str(getattr(test,'name')) 
