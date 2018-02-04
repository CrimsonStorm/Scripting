import os
import socket


def sysStart(hostList,portNum):
        username = 'jlshaw'
        password = ''
        for i in hostList:
                os.system('ssh %(username)s@%(i)s ' %{'username': username, 'i': i})
                os.system('echo hello')
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
