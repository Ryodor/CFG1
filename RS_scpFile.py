import paramiko

#hostname = '10.57.29.175'
hostname = '10.57.29.175'
password = 'coding'
username = "coding4"
port = 22

mypath='/Users/alan/Desktop/my_file'
remotepath='/Users/coding4/my_file'


t = paramiko.Transport((hostname, 22))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)


def trasnfer_file(path):
    """ Tranfer file in other computer

    Args:
        path(String): path for tranfer file

    """

    sftp.put(path, mypath);
