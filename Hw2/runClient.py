import sys, os, socket

s = []
allHosts = []

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

def dread(whichFile,byteNum = None):
        #send request to server to read file
        #f = open(whichFile,r)
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send("('read',whichFile,byteNum)") 
        return s[assignedToPort].recv(1024)

def dwrite(whichFile, whatToWrite):
        #send request to server to write file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send("('write',whichFile,whatToWrite)")
        return s[assignedToPort].recv(1024)

def dopen(whichFile, permissions = 'r'):
        # send request to server to open file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send("('open',whichFile)")
        return s[assignedToPort].recv(1024)

def dclose(whichFile):
        # send request to server to close file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send("('close',whichFile)")
        return s[assignedToPort].recv(1024)

def main():
	dInit(['pc6.cs.ucdavis.edu','pc16.cs.ucdavis.edu'],2500)
	dopen('testFile.txt')
	dwrite('testFile.txt','i am writing')
	dclose('testFile.txt')


if __name__ == '__main__':
	main()
