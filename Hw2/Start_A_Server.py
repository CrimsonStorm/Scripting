import os, socket, sys

def main():
    lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = sys.argv[1]

    lstn.bind(('',int(port)))
    lstn.listen(1)

    con, adr = lstn.accept()

    print (con, adr)

if __name__ == '__main__':
    main()
