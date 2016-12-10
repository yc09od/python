'''reference http://www.cnblogs.com/fuhuixiang/p/4103608.html
'''
import socket
import threading,getopt,sys,string

opts, args = getopt.getopt(sys.argv[1:],'hp:l:t:',["help","port=","list="])
print "opts = " + str(opts)
print "args=" + str(args)
list=50
port=8001
test = 'this_is_a_test'
def usage():
    print """
    -h --help             print the help
    -l --list             Maximum number of connections
    -p --port             To monitor the port number  
    -t --test		  just for test
    """
for op, value in opts:
    if op in ("-l","--list"):
        list = string.atol(value)
    elif op in ("-p","--port"):
        port = string.atol(value)
    elif op in ("-t","--test"):
        test = value
    elif op in ("-h"):
        usage()
        sys.exit()

print "list = " + str(list) + " port = " + str(port) + " test=" + test
