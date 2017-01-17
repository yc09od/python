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
	
	def createWindow(self,h,w,y,x,name,border = False) : 
		if (not (name in self.__windows)) : 
			self.__windows[name] = self.__stdscr.subwin(h,w,y,x)
                        if border :
            			self.__windows[name].border()
		else : 
			exit("error : window id exit")

        def setWindow(self,h,w,y,x,name,border = False) :
	        self.__windows[name] = self.__stdscr.subwin(h,w,y,x)	
                if border :
                    self.__windows[name].border()

        def refreshWindow(self,name = "") : 
                if len(name) > 0 :
                    if name in self.__windows :
                        self.__windows[name].refresh()
                    else :
                        exit("erro : window is not exit")
                else :
                    for i in self.__windows :
                        self.__windows[i].refresh()

	def getScreen (self) :
		return self.__stdscr

        def getWindow (self,name = '') :
                if len(name) > 0 :
                    if name in self.__windows :
                        return self.__windows[name]
                    else : 
                        exit("error : getWindow fail, because window not exit")
                else :
                    return self.__windows

        def delWindow (self,name = "") :
                if len(name) > 0 :
                    if name in self.__windows :
                        del self.__windows[name]
                    else : 
                        exit("error : delWindow fail, because window not exit")
                else :
                    self.__windows.clear()


        def clearWindow (self,name = "") :
                if len(name) > 0 :
                    if name in self.__windows :
                        self.__windows[name].clear()
                    else : 
                        exit("error : delWindow fail, because window not exit")
                else :
                    for i in self.__windows :
                       self.__windows[i].clear() 

        def getAllWindowsName (self) :
            return [i for i in self.__windows]


def main(myscreen) : 
        myscreen.createWindow(12,82,0,0,"outputScr",True)
        myscreen.createWindow(3,82,11,0,"inputScr",True)
        myscreen.refreshWindow()
        inputScr = myscreen.getWindow('inputScr')
        inputBar = []
        while True : 
            ch = inputScr.getch()
            inputBar.append(chr(ch))
            inputScr.addstr(1,1,''.join(inputBar))
            myscreen.refreshWindow()
             
            


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
