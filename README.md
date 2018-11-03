#Software As a Service - Rhel7

Step 1 - Install Apche Webserver on your server.

yum install httpd -y
setenfoce 0 (SeLinux Off)
systemctl stop firewalld (Stop Firewall)

Step 2 - Give sudo permission to user Apache

echo "apache       ALL=(ALL)       NOPASSWD: ALL" >> /etc/sudoers

Step 3 - pull the docker image from Docker hub
// The passwd for root user is 'q' for this image

yum install docker-ce
docker pull pankaj1234/firefox:latest    Or   docker pull pankaj1234/vlc:latest

Step 4 - Place the files.

put downloadsoft.py in /var/www/cgi-bin/
put saas.html in /var/www/html/

Step 5 - make downloadsoft.py executable
 
cd /var/www/cgi-bin
chmod +x downloadsoft.py

Step 6 - Make changes in downloadsoft.py and Saas.html  according to your ip address

Step 7 - Now use another system on the same network as client
