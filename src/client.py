import paramiko
from pathlib import Path

keyfile = "C:/Users/logan/.ssh/id_rsa"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname="24.254.180.168",
    port=1492,
    username="jellyfriend",
    key_filename=keyfile,
    password=None,
)

sftp = ssh.open_sftp()
sftp.chdir("/uploads")
print(sftp.getcwd())
print(sftp.listdir())
# print(sftp.mkdir("helloworld"))
