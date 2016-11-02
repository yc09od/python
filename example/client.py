import socket

HOST = '173.255.237.230'
#HOST = ''
PORT = 1989

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while 1:
	data = conn.recv(1024)
	message = raw_input("input messge")
	if message == 'end' : break
	conn.send(message)
	

conn.close()
s.close()

