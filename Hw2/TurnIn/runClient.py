import sys, os, socket

s = []
allHosts = []

def sysStart(hostList,portNum):
        #if assuming in csif already
        for i in hostList:
                os.system('ssh %(i)s python runServer.py %(portnum)s' %{'i': i,'portnum': portNum})
                
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
        while 1:
                returnData = s[assignedToPort].recv(4096)
                if(returnData!=None):
                        break
              
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
        if whichFile == 'stop':
                for i in s:
                        i.send('stop')
                for j in s:
                        j.close()
        else:
                s[assignedToPort].send('close ' + whichFile)
 
#def main():
#        dInit(['pc46.cs.ucdavis.edu','pc47.cs.ucdavis.edu'],2243)
#        dopen('testFile.txt')
#        #f = dread('testFile.txt')
#        #print f
#        dwrite('testFile.txt','i am writing')
#        dclose('testFile.txt')
#        dopen('testFile.txt')
#        f = dread('testFile.txt')
#        print f
#        dwrite('testFile.txt','something different')
#        dclose('testFile.txt')
#        dclose('stop')
#if __name__ == '__main__':
#        main()
