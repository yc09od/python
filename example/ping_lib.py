""" Python 3.6 """
import pyping
import sys
from datetime import datetime

hostname = str(sys.argv[1])

try:
    numberToPing = int(str(sys.argv[2]))
except:
    numberToPing = 1

r = pyping.ping(hostname)

for i in range(numberToPing):
    des = r.destination
    max = r.max_rtt
    min = r.min_rtt
    avg = r.avg_rtt
    ip = r.destination_ip
    template = "Host:{0}\tMax:{1}\tMin:{2}\tAvg:{3}\tIP:{4}\tTime:{5}"
    print(template.format(des, max, min, avg, ip, datetime.utcnow()))
    r = pyping.ping(hostname)
