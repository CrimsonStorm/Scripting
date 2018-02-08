import os, socket, sys

fileList = []

def getFile(fileName):
	global fileList
	
	if len(fileList) == 0:
		return None
	else:
		for f in fileList:
			if f.name == fileName:
				return f
		return None

def main():
	global fileList

	lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	port = sys.argv[1]

	lstn.bind(('',int(port))) 
	lstn.listen(1)

	con, adr = lstn.accept()
	f = None
	
	while(1):
		data = con.recv(4096)
		if data == 'stop':
			print 'stop!!'
			con.close()
			break
		print 'data is ' + data
		print 'here'
		data = data.split()
		print 'after'
		print data
		sendData = ''
		print f
		if data != None:
			if data[0] == 'read'  and f != None:
				print 'reading'
				if data[2] == '0':
					sendData = f.read()
					con.send(sendData)
				else:
					myInt = int(data[2])
					sendData  = f.read(data[2])
					con.send(sendData)
			elif data[0] == 'write' and f != None:
				strData = data[2:]
				writeStr = ''
				for i in strData:
					writeStr += i
				f.write(writeStr )
				f.flush()
				con.send('doneWriting')
			elif data[0] == 'open'  and f == None:
				f = open(data[1],data[2])
				print 'opened'
				con.send('doneOpening')
			elif data[0] == 'close' and f != None:
				print 'a'
				f.close()
				print 'b'
				f = None
				print 'c'
				con.send('doneClosing')
				print 'd'

if __name__ == '__main__':
    main()
