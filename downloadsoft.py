#!/usr/bin/python36
import cgi
import subprocess
import os
print("content-type: text/html")
print("")

form=cgi.FieldStorage()
Username=form.getvalue('user')
Software=form.getvalue('soft')
Port=form.getvalue('port')
print(Username)
print(Software)
print(Port)
print(subprocess.getstatusoutput("sudo docker run -dit --name {0}_{1} -p {2}:22 -v /run/media/root/RHEL-7.5\ Server.x86_64:/dvd -v /media/sf_share/rhel7_5_rpm_extras:/sfshare {1}:latest".format(Username,Software,Port)))
print(subprocess.getstatusoutput("mkdir /var/www/cgi-bin/{0}_{1}".format(Username,Software)))
print(subprocess.getstatusoutput("sudo echo '#!/bin/bash' > /var/www/cgi-bin/{2}_{1}/{2}_{1}.sh".format(Port,Software,Username)))
print(subprocess.getstatusoutput("sudo echo 'ssh -o StrictHostKeyChecking=false 192.168.43.120 -p {0} -X {1}' >> /var/www/cgi-bin/{2}_{1}/{2}_{1}.sh".format(Port,Software,Username)))

print(subprocess.getstatusoutput("sudo echo 'q' > /var/www/cgi-bin/{2}_{1}/password".format(Port,Software,Username)))
print(subprocess.getstatusoutput("sudo chmod +x /var/www/cgi-bin/{0}_{1}/{0}_{1}.sh".format(Username,Software)))
print(os.chdir("/var/ftp/pub/"))
print(subprocess.getstatusoutput("sudo tar -cvf {0}_{1}.tar /var/www/cgi-bin/{0}_{1}/".format(Username,Software,Username,Software)))

print('<a href="ftp://192.168.43.120/pub/{0}_{1}.tar">Download file for your software</a>'.format(Username,Software))
