import os
import logging
from pyftpdlib.authorizers import DummyAuthorizer
from handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():

	authorizer = DummyAuthorizer()

	authorizer.add_user('user','12345','.',perm='elradfmwM')
	authorizer.add_user('system','system','.',perm='elradfmwM')
	authorizer.add_user('ubuntu','ubuntu','.',perm='elradfmwM')
	authorizer.add_user('admin','admin','.',perm='elradfmwM')
	authorizer.add_anonymous(os.getcwd())

	handler = FTPHandler
	handler.authorizer = authorizer
	
	f= open('./banner.dat')
	s=""
	for line in f:
		s=s+line
	
	f.close()
	    
	handler.banner = s
	
	f11=open('./logs/ftp.log','w')
	f11.write("#########################################################################################\n")
	f11.close()
	logging.basicConfig(filename='./logs/ftp.log', level=logging.INFO)
	handler.log_prefix = '[%(username)s]@%(remote_ip)s'
	address = ('',21)
	server = FTPServer(address, handler)
	server.max_cons = 256
	server.max_cons_per_ip = 1
	
	server.serve_forever()
	

if __name__ == '__main__':
	main()
