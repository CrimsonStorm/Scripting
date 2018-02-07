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
        s[assignedToPort].send('read ' + whichFile + ' ' + byteNum)

def dwrite(whichFile, whatToWrite):
        #send request to server to write file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send('write ' + whichFile + ' ' + whatToWrite)

def dopen(whichFile, permissions = 'r'):
        # send request to server to open file
        assignedToPort = hash(whichFile) % len(allHosts)
        s[assignedToPort].send('open ' + whichFile + ' ' + permissions)

def dclose(whichFile):
        # send request to server to close file
        assignedToPort = hash(whichFile) % len(allHosts)
	temp = 'close ' + whichFile
	print temp
        s[assignedToPort].send('close ' + whichFile)

def main():
	dInit(['pc47.cs.ucdavis.edu','pc48.cs.ucdavis.edu'],2500)
	dopen('testFile.txt','w')
	dwrite('testFile.txt','i am writing')
	print 'closing'
	dclose('testFile.txt')
	print 'closed'


if __name__ == '__main__':
	main()
