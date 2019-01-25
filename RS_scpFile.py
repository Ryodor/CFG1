


import paramiko

#hostname = '10.57.29.175'
hostname = '10.57.29.175'
password = 'coding'
username = "coding4"
port = 22

mypath='/Users/selatniryad/my_file.txt'
remotepath='/Users/coding4/my_file.txt'


t = paramiko.Transport((hostname, 22))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(mypath, remotepath)
print("Ryad's File")