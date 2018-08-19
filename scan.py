
# -*- coding: utf-8 -*-
import re
import sys
from socket import *
# portscan.py <host> <start_port>-<end_port>
import getopt
try:
    options,args = getopt.getopt(sys.argv[1:],"",["host=","port="])
except:
    print("Parameter Error")

dict_op = dict(options)
host = dict_op['--host']

    
if not  re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$",host):
    print("Parameter Error")


portstrs = dict_op['--port'].split('-')

start_port = int(portstrs[0])
try:
    end_port = int(portstrs[1])
except:
    end_port = start_port
target_ip = gethostbyname(host)

for port in range(start_port,end_port+1):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((target_ip,port))
    if result ==0:
        print(port, " open")
    else:
        print(port, " closed")


