First off you need to open n windows to run runServer.py on our n hosts.
(If you are logged in as a user who can ssh into servers without a password, use sysStart in a different window 
with the hosts and port number and can bypass the first line.)
Then start runClient in python interactive and use dinit with hostnames and ports.
Then you can use dinit() dread(), dwrite(), dopen(), and dclose()