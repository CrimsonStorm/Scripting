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

	while(1):
		data = con.recv(1024)
		if data == '':
			con.close()
			break
		print 'data is ' + data
		print 'here'
		data = data.split()
		print 'after' 
		print data
		f = getFile(data[1])
		if   data[0] == 'read'  and f != None:
			if data[2] == None:
				f.read()
			else:
				f.read(data[2])
		elif data[0] == 'write' and f != None:
			print 'writing'
			data = [data[0], data[1], data[2:]]
			write(data[2])
		elif data[0] == 'open'  and f == None:
			f = open(data[1],data[2])
		elif data[0] == 'close' and f != None:
			fileList.remove(f)
			f.close()

if __name__ == '__main__':
    main()
