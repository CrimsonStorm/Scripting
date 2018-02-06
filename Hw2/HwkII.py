import os
import socket
#hello
def sysStart(hostList,portNum):
    username = 'dmdickin'
    password = ''
    print "hostList: "
    print hostList
    j = 0
    con_adr = [None]*len(hostList)
    for host in hostList:
        os.system('ssh %(username)s@%(host)s ' %{'username': username, 'host': host})
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, portNum))
        s.listen(1)
        con_adr[j] = s.accept()
	con_adr[j][0].setblocking(0)
        print 'loop'
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
        s[j].connect((host,port))
        j = j + 1
        
def dread():
        return 0

def dwrite():
        return 0

def dopen():
        return 0

def dclose():
    end_session = true
    for i in range(0, num_hosts):
        s[i].close()
