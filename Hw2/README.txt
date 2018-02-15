First off you need to open n windows to run runServer.py on our n hosts.
Then start runClient in python interactive in a separate window and use dinit with hostnames as a list and port.
Then you can use dinit() dread(), dwrite(), dopen(), and dclose()
dread, dwrite, dopen, and dclose all take at minimum a filename as a string as an argument.