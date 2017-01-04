import curses
import traceback
import time
import locale

def main(stdscr) :
	locale.setlocale(locale.LC_ALL, '')
	code = locale.getpreferredencoding()

	screen = stdscr.subwin(23,79,0,0)
	inputScreen = stdscr.subwin(1,77,21,1)
	subScreen = curses.newwin(10,10,0,79)
	screen.box()
	subScreen.box()
	screen.hline(20,1,curses.ACS_HLINE,77)
	subScreen.move(5,5)
	screen.refresh()
	subScreen.refresh()
	input_bar = []
	while True :
		ch = screen.getch()
		if (ch == 8) and len(input_bar) > 0 :
			input_bar.pop()	
		else :
			input_bar.append(chr(ch))
		inputScreen.erase()
		inputScreen.addstr(0,0,''.join(input_bar))
		inputScreen.refresh()
	
try :
	
    if __name__ == "__main__" :

	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()
	stdscr.keypad(1)
	main(stdscr)
	stdscr.keypad(0)
	curses.echo()
	curses.nocbreak()
	curses.endwin()

except :
	stdscr.keypad(0)
	curses.echo()
	curses.nocbreak()
	curses.endwin()
	traceback.print_exc()
