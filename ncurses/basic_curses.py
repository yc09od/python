# -*- coding: ascii -*-
import curses
import traceback
import time
import locale

def main(stdscr) :
	locale.setlocale(locale.LC_ALL, '')
	code = locale.getpreferredencoding()

	screen = stdscr.subwin(23,79,0,0)
	inputScreen = stdscr.subwin(1,77,21,1)
        outputScreen = stdscr.subwin(19,77,1,1)
	subScreen = curses.newwin(10,10,0,79)
	screen.box()
	subScreen.box()
	screen.hline(20,1,curses.ACS_HLINE,77)
	subScreen.move(5,5)
	screen.refresh()
	subScreen.refresh()
	input_bar = []
        output_data = []
        name = ''
	while True :
            try:
		ch = screen.getch()
                #if ch is delete or backspace
		if (ch == 127 or ch == 8) and len(input_bar) > 0 :
		    input_bar.pop()	
                elif (ch == 127 or ch == 8) and len(input_bar) <=0 :
                    pass
                elif ch == 10 :
                    outputScreen.erase()
                    if ''.join(input_bar) == ':exit' :
                        break
                    elif ':name' in ''.join(input_bar) :
                        name = ''.join(input_bar)[len(':name') + 1 :] 
                    else :
                        output_data.append((name + ' : ' if len(name) > 0 else '') + ''.join(input_bar))
                    for i in range(0 if len(output_data) <= 19 else len(output_data) - 19 ,len(output_data)) :
                            outputScreen.addstr(i if len(output_data) <= 19 else i - len(output_data) + 19,0,output_data[i])
                    outputScreen.refresh()
                    input_bar = []
		else :
		    input_bar.append(chr(ch))
		inputScreen.erase()
		inputScreen.addstr(0,0,''.join(input_bar))
		inputScreen.refresh()
            except KeyboardInterrupt:
                break
            except :
                pass
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
