import socket

HOST = '173.255.237.230'
#HOST = ''
PORT = 1989

conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect((HOST,PORT))
while 1:
	data = conn.recv(1024)
	message = raw_input("input messge\n")
	if message == 'end' : break
	conn.send(message)
conn.close()

