import socket
import threading

HOST = ''
PORT = 1989

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()

def getMsg(conn,addr) :
	while True :
		data = conn.recv(1024)
		print str(addr) + " : output --" + str(data) + "\nInput : "
		if not data : continue
		if data == "end" : break

def sendMsg(conn,addr) :
	while True :
		data = raw_input('Input :\n')
		conn.send(data)
		if not data : continue
		if data == 'end' : break

if 1:
	print_msg = threading.Thread(target=getMsg,args=(conn,addr,))
	print_msg.start()
	write_msg = threading.Thread(target=sendMsg,args=(conn,addr,))
	write_msg.start()
#	sendMsg(conn,addr)

#conn.close()
#s.close()

