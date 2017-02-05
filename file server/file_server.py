import socket
import thread
import hashlib

serversock = socket.socket()
host = socket.gethostname();
port = 4545;
serversock.bind(('',port));
filename = ""
serversock.listen(10);
DOWNLOAD_LOCATION = "./ftp_uploads/"
print "Waiting for a connection....."

while True:
    clientsocket,addr = serversock.accept()
    print("Got a connection from %s" % str(addr))
    header=""
    while True:
        d = clientsocket.recv(1)
        if d == '\n':
            break
        header += d

    filesize = int(header.split()[-1])
    filename="".join(header.split()[1:-1])

    file_to_write=open(DOWNLOAD_LOCATION+filename,'wb')

    while filesize>0:
        chunk = clientsocket.recv(1024)
        filesize -= 1024
        file_to_write.write(chunk)

    file_to_write.close()

serversock.close()
