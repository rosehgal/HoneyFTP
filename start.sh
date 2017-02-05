#!/bin/bash 

if [ "$EUID" -ne 0 ]
then
  echo "[*] Please run as root"
  exit
fi

docker -v
if [ $? -ne 0 ]
then
  aptitude install docker.io -y
else
  echo "[*] Docker Already Installed"
fi

docker build -t ftpserver honeyPotServices/

if [ $? -ne 0 ]
then
  echo "[*] unbale to build docker"
  exit
fi

docker run --name FTP -d -p 20:20 -p 21:21 -i ftpserver

if [ $? -ne 0 ]
then
  echo "[*] Docker with name FTP already running"
  echo "[*] Stopping FTP and rerunning"
  docker rm -f FTP
  docker run --name FTP -d -p 20:20 -p 21:21 -i ftpserver
fi

mkdir -p ./file_receiver/ftp_uploads
/bin/sh -c '/file_receiver/file_server.py &'
echo "[*] All the uploads will be monitored by service running @ 4545 port"
echo "[*] The ftp uploads will be logged in `pwd`/file_receiver/ftp_uploads/"
