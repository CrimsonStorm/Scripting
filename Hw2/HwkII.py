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

def dread(whichFile):
        #send request to server to read file
        dopen(whichFile)
        s.send('read')
        s.send(whichFile)
        return 0

def dwrite(whichFile):
        #send request to server to write file
        s.send('write')
        s.send(whichFile)
        return 0

def dopen(whichFile):
        # send request to server to open file
        s.send('open')
        return 0

def dclose(whichFile):
        # send request to server to close file
        s.send('close')
        return 0
