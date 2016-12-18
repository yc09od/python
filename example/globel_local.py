#!/usr/bin/python
#-*- coding: UTF-8 -*-

import copy

g = 'this is globel var'


def test1() :
	g = 'this local var'
	print 'at local' + g

def test2() :
	g = 'this local2 var'
	print 'at local' + g

def test3() :
	g = 'this local3 var'
	print g
	if True :
		print 'in if' + g
		g = 'break'
	print g

def func_int(a) :
	a += 4
	
def func_list(l) :
	l[0] = 2

def func_copy() :
	l = range(0,3)
	l.append(range(0,3))
	l[3].append(range(0,3))
	print str(l)
	l1 = l
	l1[0] = 1
	print str(l)
	l2 = copy.copy(l)
	l[3][3][0] = 100
	print str(l2)
	l3 = copy.deepcopy(l)
	l[3][3][0] = 200
	print str(l3)

def main() :
	func_copy()
#	print 'at main : \t' + g

if __name__ == '__main__' :
	main()
