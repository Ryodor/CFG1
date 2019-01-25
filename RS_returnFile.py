print("Ryad's File")

import paramiko

ip='10.57.29.175'
port=22
username='coding4'
password='coding'

cmd='say "Hello World Bitchies!!!"'

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)


# SCP

#hostname = '10.57.29.175'
#password = 'coding'
#username = "coding4"
#port = 22

#mypath='/Users/selatniryad/my_file.txt'
#remotepath='/Users/coding4/my_file.txt'


#t = paramiko.Transport((hostname, 22))
#t.connect(username=username, password=password)
#sftp = paramiko.SFTPClient.from_transport(t)
#sftp.put(mypath, remotepath)
#print("Ryad's File")

