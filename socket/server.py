import socket

HOST = '173.255.237.230'
#HOST = ''
PORT = 1989

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
while 1:
	conn.send('Hi this is server')
	data = conn.recv(1024)
	if not data : break
	if data == 'Yes' :
		print "He said yes"
	print addr
	print 'I got your message = ' + data
conn.close()
s.close()

