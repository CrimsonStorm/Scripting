import os, socket, sys
from ast import literal_eval as make_tuple

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
		data = make_tuple(con.recv(1024))
		f = getFile(data[1])
		if   data[0] == 'read'  and f != None:
			if data[2] == None:
				con.send(f.read())
			else:
				con.send(f.read(data[2]))
		elif data[0] == 'write' and f != None:
			con.send(f.write(data[2]))
		elif data[0] == 'open'  and f == None:
			con.send(f.open(data[1],data[2]))
		elif data[0] == 'close' and f != None:
			fileList.remove(f)
			con.send(f.close())

if __name__ == '__main__':
    main()
