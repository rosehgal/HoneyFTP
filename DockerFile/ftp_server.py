#!/usr/bin/python

import os,sys
import logging
import ConfigParser
from random import randint

from pyftpdlib.authorizers import DummyAuthorizer
from handlers import FTPHandler
from pyftpdlib.servers import FTPServer

BASE_LOCATION = "/home/ftp/"
FTP_DIRECTORY = BASE_LOCATION + "drive"

if __name__ == "__main__":

	authorizer = DummyAuthorizer()
	config = ConfigParser.RawConfigParser()
	config.read(BASE_LOCATION + 'config.cfg')

   	usernames =  [i.strip() for i in config.get('users','usernames').split(',')]
   	passwords = [i.strip() for i in config.get('users','password').split(',')]

   	if len(usernames) != len(passwords):
   		print "User name Password length Mismatch ... Quitting"
   		sys.exit(0);

   	for i in range(len(usernames)):
   		authorizer.add_user(usernames[i],passwords[i],FTP_DIRECTORY,perm='elradfmwM')

	authorizer.add_anonymous(os.getcwd())
	handler = FTPHandler
	handler.authorizer = authorizer

	f=open(BASE_LOCATION + 'banners/banner'+str(randint(0,5))+'.dat')

	s=""
	for line in f:
		s=s+line

	f.close()

	handler.banner = s

	logging.basicConfig(filename=BASE_LOCATION+'logs/ftp.log', level=logging.INFO)
	handler.log_prefix = '[%(username)s]@%(remote_ip)s'
	address = ('',21)
	server = FTPServer(address, handler)
	server.max_cons = 256
	server.max_cons_per_ip = 1

	server.serve_forever()
