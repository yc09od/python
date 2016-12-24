import socket
import threading

#HOST = '173.255.237.230'
HOST = ''
PORT = 1989


def getMsg(conn) :
	while True :
		data = conn.recv(1024)
		print "server output --" + str(data) + "\nInput :"
		if not data : continue
		if data == "end" : break

def sendMsg(conn) :
	while True :
		data = raw_input('Input :\n')
		conn.send(data)
		if not data : continue
		if data == "end" : break

def main():
	conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	conn.connect((HOST,PORT))
	print_msg = threading.Thread(target=getMsg,args=(conn,))
	print_msg.start()
	write_msg = threading.Thread(target=sendMsg,args=(conn,))
	write_msg.start()
#	sendMsg(conn)
#	getMsg(conn)
#	conn.close()

if __name__ == "__main__" :
	main()

