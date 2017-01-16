# -*- coding: ascii -*-
import curses
import traceback
import time
import sys

class myScreen :
	__stdscr = ''
	__windows = {}
	def __init__ (self,stdscr) : 
		self.__stdscr = stdscr 
		self.maxHeight , self.maxWeight = self.__stdscr.getmaxyx()
		self.__stdscr.keypad(1)
	
	def createWindow(self,h,w,y,x,name) : 
		if (not (name in self.__windows)) : 
			self.__windows[name] = self.__stdscr.subwin(h,w,y,x)
			self.__windows[name].border()
			self.__windows[name].refresh()
		else : 
			exit("error : window id exit")
		

	def getScreen (self) :
		return self.__stdscr


def main(myscreen) : 
	myscreen.createWindow(10,10,0,0,"main")	
	while True : 
		pass

try :
	
    if __name__ == "__main__" :

	myscreen = myScreen(curses.initscr())
	
	curses.noecho()
	curses.cbreak()
	main(myscreen)
	curses.echo()
	curses.nocbreak()
	curses.endwin()

except :
	curses.echo()
	curses.nocbreak()
	curses.endwin()
	traceback.print_exc()
