import os
import socket

allHosts = []
sList = []
def sysStart(hostList,portNum):
        # Ssh into each host list and start a server
        #If not assuming in
        #username = 'jlshaw'
        #port = 'pc16.cs.ucdavis.edu'
        # os.system('ssh %(username)s@%(port)s ' %{'username': username, 'port': port})

        #if assuming in csif already
        for i in hostList:
                os.system('ssh %(i)s python HwkIIServer.py %(portnum)s' %{'i': i,'portnum': portNum})
def sysStop(hostList):
        #Close all the sockets for the hosts
        for i in sList:
                i.close()


def dInit(hostList,portNum):
        #Tell the server(manager) to start sysStart with the hostList and portnum
        global allHosts 
        map(lambda x: allHosts.append(x), hostList)
`       #for each hostlist, connect to each port

def dread(whichFile,byteNum = 0):
        #send request to server to read file
        #f = open(whichFile,r)
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send(('read',whichFile,byteNum)) 
        return s.recv(1024)

def dwrite(whichFile, whatToWrite):
        #send request to server to write file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send(('write',whichFile,whatToWrite))

def dopen(whichFile):
        # send request to server to open file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send(('open',whichFile))

def dclose(whichFile):
        # send request to server to close file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send(('close',whichFile))



#ServerCode
#x = s.recieve()
# if (x == 'read'):
# s.send(x.read())
# if (x == 'write'):
#   while(1):
#       f.write(x)
# if (x == 'close'):
# f.close()
# if (x == 'open'):
#   f = open(x)
