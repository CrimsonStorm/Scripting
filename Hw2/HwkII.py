import os
import socket


def sysStart(hostList,portNum):
    sList = [socket.socket(socket.AF_INET, socket.SOCK_STREAM)] * len(hostList)
    for i in range(0,len(sList)):
        sList[i].bind((hostList[i],portNum))
        sList[i].listen(1)
        connection,address = sList[i].accept()
        print 'made it here'

def sysStop(hostList):
    for i in range(0,len(hostList)):
        sList[i].close()


def dInit(hostList):
    global allHosts 
    allHosts = hostList[:]
    

def dread():
	return 0

def dwrite():
	return 0

def dopen():
	return 0

def dclose():
	return 0
