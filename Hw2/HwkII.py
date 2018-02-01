import os
import socket


def sysStart(hostList,portNum):
    global sList = [socket.socket(socket.AF_INET, socket.SOCK_STREAM)] * len(hostList)
    for i in range(0,len(sList):
        sList[i].bind(host[i],portNum)
        sList[i].listen(1)
        connection,address = sList[i].accept()
        

def sysStop(hostList):
    for i in range(0,len(hostList)):
        sList[i].close()


def dInit(hostList):
    global allHosts = hostList[:]
    

def dread():

def dwrite():

def dopen():

def dclose():
    
