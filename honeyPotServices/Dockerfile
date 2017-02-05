#This ftp based docker is based on Ubuntu distribution
FROM ubuntu

MAINTAINER Rohit Sehgal (rsehgal@iitk.ac.in)

RUN apt-get update && apt-get install python2.7 -y
RUN apt-get install aptitude -y

#aptitude will install the dependencies related to python-pip
RUN aptitude install python-pip -y

RUN pip install pyftpdlib

#creating the directory for ftp user
RUN mkdir -p /home/ftp
RUN chmod 770 /home/ftp

#creating a user that will run ftp_client request
RUN useradd ftp
#RUN groupadd ftp

RUN chown :ftp /home/ftp

#Copy necessary file to ftpDocker !
COPY ftp_logging.py /home/ftp/ftp_logging.py
COPY ftp_server.py /home/ftp/ftp_server.py
COPY banners /home/ftp/banners
COPY handlers.py /home/ftp/handlers.py
COPY userPass.cfg /home/ftp/config.cfg

RUN mkdir /home/ftp/logs
RUN touch /home/ftp/logs/ftp.log

#copying ftp honeydrive Content
COPY ftpDrive /home/ftp/drive
RUN chown :ftp /home/ftp/drive

#Open ftp ports to Docker
EXPOSE 20 21

#Start Default service i.e FTP Server
ENTRYPOINT ["python"]
CMD ["/home/ftp/ftp_server.py"]
