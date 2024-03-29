import sys, os, socket

s = []
allHosts = []

def sysStop(hostList):
        #Close all the sockets for the hosts
        for i in s:
                i.close()
                
def dInit(hostList,portNum):
        #Tell the server(manager) to start sysStart with the hostList and portnum
        global allHosts
        global s
        map(lambda x: allHosts.append(x), hostList)
        #for each hostlist, connect to each port
        s = [None]*len(hostList)
        j = 0
        for host in hostList:
                s[j] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s[j].connect((host,portNum))
                j = j + 1

def dread(whichFile,byteNum = 0):
        #send request to server to read file
        #f = open(whichFile,r)
        assignedToPort = hash(whichFile) % len(allHosts)
        strByte = str(byteNum)
        s[assignedToPort].send('read ' + whichFile + ' ' + strByte)
        returnData = ''
        #while 1:
	returnData = s[assignedToPort].recv(4096)
        #        if(returnData!=None):
        #                break
              
        return returnData
def dwrite(whichFile, whatToWrite):
        #send request to server to write file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send('write ' + whichFile + ' ' + whatToWrite)
        while 1:
                if(s[assignedToPort].recv(1024) == 'doneWriting'):
                        break
                
def dopen(whichFile, permissions = 'a+'):
        # send request to server to open file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send('open ' + whichFile + ' ' + permissions)
        while 1:
                if(s[assignedToPort].recv(1024) == 'doneOpening'):
                        break
                
def dclose(whichFile):
        # send request to server to close file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send('close ' + whichFile)
 
