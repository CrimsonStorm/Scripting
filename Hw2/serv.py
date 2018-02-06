import os, socket, sys

#globals
con_adr = None

def sysStart(hostList,portNum):
    j = 0
    global con_adr
    con_adr = [None]*len(hostList)
    for host in hostList:
        pipe = os.popen('cat Start_A_Server.py | ssh dmdickin@' + host + ' python - ' + str(portNum))
        print 'before read'
	con_adr[j] = pipe.read()
	print 'after read'
        print con_adr[j]
        j = j + 1
    print 'end loop'

def sysStop(hostList):
    for i in range(0,len(hostList)):
        con_adr[i][0].close()

def dInit(hostList,port):
    global allHosts
    global num_hosts
    global files
    global end_session
    allHosts = hostList[:]
    num_hosts = len(hostList)
    files = [None]*num_hosts
    end_session = False
    s = [None]*num_hosts
    j = 0
    for host in hostList:
        s[j] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print host
	print port
        s[j].connect((host,port))
        j = j + 1
        
def dread():
        return 0

def dwrite():
        return 0

def dopen():
        return 0

def dclose():
    end_session = True
    for i in range(0, num_hosts):
        s[i].close()

def main():
    sysStart(sys.arv[1],sys.argv[2])
    g = 0
    while(1):
        #receive and process commands
	#if received '' then break
	print 'hey im loopn'
	g = g + 1
	if g > 20:
	    break

    sysStop(sys.argv[1])

#if __name__ == '__main__':
#    main()
