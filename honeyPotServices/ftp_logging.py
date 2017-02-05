import datetime
import os

#if the file is not created create IT

LOG_LOCATION = '/home/ftp/logs/ftp.log'
f1 = open(LOG_LOCATION,'a+')

Lines=f1.readlines()
searchquery = '@'

for i in range(0,len(Lines)):
	if searchquery in Lines[i]:
		st=Lines[i].index('@')
		ed=Lines[i].index(' ')
		ip=Lines[i][st+1:ed]
		dir="./logs/"+ip
		if not os.path.exists(dir):
			os.makedirs(dir)

		x = datetime.datetime.now()
		dt=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
		addr=dir+'/'+dt+'.log'
		f2=open(addr,'a+')
		f2.write(Lines[i])
		f2.close()

f1.close()
#This will clean the file to start relogging
f1 = open(LOG_LOCATION,'w')
f1.close()
