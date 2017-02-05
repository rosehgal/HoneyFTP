FROM ubuntu

MAINTAINER Rohit Sehgal (rsehgal@iitk.ac.in)

RUN apt-get update && apt-get install python2.7 -y
RUN apt-get install aptitude -y
RUN aptitude install python-pip -y

RUN pip install pyftpdlib

RUN mkdir ftpServer
COPY ftp_logging.py ftpServer/ftp_logging.py
COPY ftp_server.py ftpServer/ftp_server.py
COPY banners ftpServer/banners
COPY handlers.py ftpServer/handlers.py
COPY userPass.cfg ftpServer/userPass.cfg

RUN mkdir ftpServer/logs
RUN touch ftpServer/logs/ftp.log
RUN chmod 666 ftpServer/userPass.cfg

EXPOSE 20 21

ENTRYPOINT ["python"]
CMD ["ftpServer/ftp_server.py"]

